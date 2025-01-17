[![Python package](https://github.com/RECETOX/RIAssigner/actions/workflows/python-package.yml/badge.svg)](https://github.com/RECETOX/RIAssigner/actions/workflows/python-package.yml)
[![Python Package using Conda](https://github.com/RECETOX/RIAssigner/actions/workflows/python-package-conda.yml/badge.svg?branch=main)](https://github.com/RECETOX/RIAssigner/actions/workflows/python-package-conda.yml)
[![Anaconda Build](https://github.com/RECETOX/RIAssigner/actions/workflows/anaconda.yml/badge.svg?branch=main)](https://github.com/RECETOX/RIAssigner/actions/workflows/anaconda.yml)
# RIAssigner
RIAssigner is a python tool for retention index (RI) computation for GC-MS data developed at [RECETOX](https://www.recetox.muni.cz/en).

## Class Diagram
<!-- generated by mermaid compile action - START -->
![~mermaid diagram 1~](/.resources/README-md-1.svg)
<details>
  <summary>Mermaid markup</summary>

```mermaid
classDiagram
    class MatchMSData{
        -List ~Spectra~ data
    }

    class PandasData {
        -DataFrame data
    }

    Data <|-- MatchMSData
    Data <|-- PandasData

    class Data{
        <<abstract>>
        +read(string filename)
        +write(string filename)
        +retention_times() List~float~
        +retention_indices() List~int~
    }


    class ComputationMethod{
        <<interface>>
        +compute(Data query, Data reference) List~int~

    }

    class Kovats {

    }
    class Harangi {

    }
    class CubicSpline {

    }

    ComputationMethod <|-- Kovats
    ComputationMethod <|-- Harangi
    ComputationMethod <|-- CubicSpline

```

</details>
<!-- generated by mermaid compile action - END -->
