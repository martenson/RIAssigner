# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Added `__eq__` to `PandasData` and `MatchMSData` [#51](https://github.com/RECETOX/RIAssigner/pull/51)
- data/PandasData.py: Added reading `tsv` files. [#49](https://github.com/RECETOX/RIAssigner/pull/49)
### Changed
- data/MatchMSData.py: `_assign_ri_value` now converts all values to float and stores them as string in metadata field
- data/MatchMSData.py `_read_retention_indices` now calls retention_indices property setter to store values
### Removed

## [0.1.0] - 2021-07-12
### Added
- Reading data from `CSV` and `MSP` files [#8](https://github.com/RECETOX/RIAssigner/pull/8)[#15](https://github.com/RECETOX/RIAssigner/pull/15)[#36](https://github.com/RECETOX/RIAssigner/pull/36)
- Computing Kovats retention index [#25](https://github.com/RECETOX/RIAssigner/pull/25)
- Computing RI based on cubic splines [#33](https://github.com/RECETOX/RIAssigner/pull/33)
- Added CI actions to GitHub [#43](https://github.com/RECETOX/RIAssigner/pull/43)
- Added writing data back to memory for `MSP`, `CSV` and `tsv` files [#7](https://github.com/RECETOX/RIAssigner/pull/7)[#14](https://github.com/RECETOX/RIAssigner/pull/14)[#19](https://github.com/RECETOX/RIAssigner/pull/19)