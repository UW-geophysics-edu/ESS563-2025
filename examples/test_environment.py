#!/usr/bin/env python
"""
Test script to verify that all required packages are installed and working.

This script imports all the main packages used in ESS563 and performs
basic operations to ensure they're functioning correctly.
"""

import sys
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing

def test_imports():
    """Test that all required packages can be imported."""
    print("Testing package imports...")
    
    try:
        import numpy as np
        print(f"✓ numpy {np.__version__}")
    except ImportError as e:
        print(f"✗ numpy: {e}")
        return False
    
    try:
        import scipy
        print(f"✓ scipy {scipy.__version__}")
    except ImportError as e:
        print(f"✗ scipy: {e}")
        return False
    
    try:
        import pandas as pd
        print(f"✓ pandas {pd.__version__}")
    except ImportError as e:
        print(f"✗ pandas: {e}")
        return False
    
    try:
        import matplotlib.pyplot as plt
        print(f"✓ matplotlib {matplotlib.__version__}")
    except ImportError as e:
        print(f"✗ matplotlib: {e}")
        return False
    
    try:
        import h5py
        print(f"✓ h5py {h5py.__version__}")
    except ImportError as e:
        print(f"✗ h5py: {e}")
        return False
    
    try:
        import obspy
        print(f"✓ obspy {obspy.__version__}")
    except ImportError as e:
        print(f"✗ obspy: {e}")
        return False
    
    return True

def test_basic_functionality():
    """Test basic functionality of key packages."""
    print("\nTesting basic functionality...")
    
    try:
        import numpy as np
        import matplotlib.pyplot as plt
        import pandas as pd
        import h5py
        from obspy import UTCDateTime
        
        # Test numpy
        arr = np.array([1, 2, 3, 4, 5])
        print(f"✓ numpy array created: {arr}")
        
        # Test pandas
        df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
        print(f"✓ pandas DataFrame created with shape: {df.shape}")
        
        # Test matplotlib
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 2])
        plt.close(fig)
        print("✓ matplotlib plot created and closed")
        
        # Test obspy UTCDateTime
        t = UTCDateTime()
        print(f"✓ obspy UTCDateTime created: {t}")
        
        return True
        
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        return False

def main():
    """Main test function."""
    print("ESS563 Environment Test")
    print("=" * 30)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed!")
        sys.exit(1)
    
    # Test basic functionality
    if not test_basic_functionality():
        print("\n❌ Functionality tests failed!")
        sys.exit(1)
    
    print("\n✅ All tests passed! Environment is ready for ESS563.")

if __name__ == "__main__":
    main()