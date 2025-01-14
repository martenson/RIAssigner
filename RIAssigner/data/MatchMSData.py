from .Data import Data
from matchms import Spectrum
from matchms.exporting import save_as_msp
from matchms.importing import load_from_msp
from typing import Optional, Iterable


class MatchMSData(Data):
    """ Class to handle data from filetypes which can be imported using 'matchMS'.

    Currently only supports 'msp'.
    """

    def read(self):
        """Load data into object and initialize properties.
        """
        self._read_spectra(self._filename)

        self._sort_spectra_by_rt()

        self._read_retention_times()
        self._read_retention_indices()

    def write(self, filename: str):
        save_as_msp(self._spectra, filename)

    def _read_spectra(self, filename):
        if filename.endswith('.msp'):
            self._spectra = list(load_from_msp(filename))
        else:
            raise NotImplementedError("Currently only supports 'msp'.")

    def _read_retention_times(self):
        """ Read retention times from spectrum metadata. """
        self._retention_times = Data.URegistry.Quantity([safe_read_key(spectrum, 'retentiontime') for spectrum in self._spectra], self._unit)

    def _read_retention_indices(self):
        """ Read retention indices from spectrum metadata. """
        self.retention_indices = [safe_read_key(spectrum, 'retentionindex') for spectrum in self._spectra]

    def _sort_spectra_by_rt(self):
        """ Sort objects (peaks) in spectra list by their retention times. """
        self._spectra.sort(key=lambda spectrum: safe_read_key(spectrum, 'retentiontime'))

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, MatchMSData):
            return False
        other: MatchMSData = o

        are_equal = (self.retention_times == other.retention_times).all()
        try:
            are_equal &= (self.retention_indices == other.retention_indices)
        except KeyError:
            pass
        are_equal &= self._spectra == other._spectra
        return are_equal

    @property
    def retention_times(self) -> Iterable[Data.RetentionTimeType]:
        """ Get retention times in seconds. """
        return self._retention_times.to('seconds')

    @property
    def retention_indices(self) -> Iterable[Data.RetentionIndexType]:
        """ Get retention indices. """
        return self._retention_indices

    @retention_indices.setter
    def retention_indices(self, values: Iterable[Data.RetentionIndexType]):
        """ Set retention indices. """
        if len(values) == len(self._spectra):
            self._retention_indices = values
            list(map(_assign_ri_value, self._spectra, values))
        else:
            raise ValueError('There is different numbers of computed indices and peaks.')


def safe_read_key(spectrum: Spectrum, key: str) -> Optional[float]:
    """ Read key from spectrum and convert to float or return 'None'.
    Tries to read the given key from the spectrum metadata and convert it to a float.
    In case an exception is thrown or the key is not present, returns 'None'.

    Parameters
    ----------
    spectrum:
        Spectrum from which to read the key.
    key:
        Key to be read from the spectrum metadata.

    Returns
    -------
        Either the key's value converted to float or 'None'.
    """

    value = spectrum.get(key, default=None)
    if value is not None:
        try:
            value = float(value)
        except ValueError:
            # RT is in format that can't be converted to float -> set rt to None
            value = None
    return value


def _assign_ri_value(spectrum: Spectrum, value: Data.RetentionIndexType):
    """Assign RI value to Spectrum object

    Args:
        spectrum (Spectrum): Spectrum to add RI to
        value (Data.RetentionIndexType): RI to be added to Spectrum
    """
    if value is not None:
        retention_index = ('%f' % float(value)).rstrip('0').rstrip('.')
        spectrum.set(key='retentionindex', value=retention_index)
