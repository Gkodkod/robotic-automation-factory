import pytest
from package_sorter import sort

"""_summary_
The test_standard_package function tests the sort function with a standard package.

The test cases cover various scenarios such as:
a small, light package, 
a package that is heavy but not bulky, 
a bulky package but not heavy, 
a package that is both heavy and bulky, 
and a package with a bulky volume.

Lastly, the test_edge_cases function tests the sort function with edge cases such as:
a package with one dimension exactly 150 cm, 
a package with a mass exactly 20 kg, 
and a package with a volume exactly 1,000,000 cm^3
"""

def test_standard_package():
    # Small, light package
    assert sort(50, 40, 30, 10) == "STANDARD"

def test_heavy_package():
    # Package is heavy but not bulky
    assert sort(50, 40, 30, 25) == "SPECIAL"

def test_bulky_package():
    # Package is bulky but not heavy
    assert sort(160, 50, 50, 10) == "SPECIAL"

def test_rejected_package():
    # Package is both heavy and bulky
    assert sort(160, 50, 50, 25) == "REJECTED"

def test_volume_bulky():
    # Package is bulky due to volume
    assert sort(100, 100, 100, 10) == "SPECIAL"

def test_edge_cases():
    # Boundary conditions
    assert sort(150, 50, 50, 10) == "SPECIAL"  # One dimension exactly 150
    assert sort(50, 50, 50, 20) == "SPECIAL"  # Mass exactly 20
    assert sort(1000, 1000, 1000, 10) == "SPECIAL"  # Volume exactly 1,000,000