# ESS563-2025
Advanced Seismology

This repository contains the Python environment setup and utilities for the ESS563 Advanced Seismology course.

## Environment Setup

### Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/UW-geophysics-edu/ESS563-2025.git
   cd ESS563-2025
   ```

2. Create the conda environment:
   ```bash
   conda env create -f environment.yml
   ```

3. Activate the environment:
   ```bash
   conda activate ess563
   ```

### Alternative Installation (pip only)

If you prefer to use pip instead of conda:

```bash
pip install -r requirements.txt
```

## Testing the Environment

To verify that all packages are installed correctly, run the test script:

```bash
python examples/test_environment.py
```

This will check that all required packages are installed and functioning properly.

## Included Packages

This environment includes the following key packages for seismological analysis:

- **obspy**: Seismic data processing and analysis
- **matplotlib**: Plotting and visualization
- **scipy**: Scientific computing
- **numpy**: Numerical computing
- **pandas**: Data manipulation and analysis
- **h5py**: HDF5 file format support

## Usage

After activating the environment, you can start using any of the included packages in your Python scripts or Jupyter notebooks.

Example:
```python
import obspy
from obspy import read
import matplotlib.pyplot as plt
import numpy as np

# Your seismological analysis code here...
```

## Directory Structure

```
ESS563-2025/
├── environment.yml     # Conda environment specification
├── requirements.txt    # Pip requirements file
├── ess563/            # Main package directory
│   └── __init__.py    # Package initialization
└── examples/          # Example scripts and tests
    └── test_environment.py  # Environment verification script
```

## Contributing

This repository is for educational purposes as part of the ESS563 Advanced Seismology course.
