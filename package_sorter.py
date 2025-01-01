"""
Package sorter module - The main implementation of the sorting function.
"""

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sort packages into stacks based on volume and mass criteria.
    
    Args:
        width (float): Package width in centimeters
        height (float): Package height in centimeters
        length (float): Package length in centimeters
        mass (float): Package mass in kilograms
    
    Returns:
        str: The stack where the package should be dispatched
    """
    # Calculate volume by multiplying width, height, and length
    volume = width * height * length
    
    # Check bulky conditions: volume ≥ 1,000,000 cm³ or any dimension ≥ 150 c   m
    is_bulky = (volume >= 1_000_000) or \
               (width >= 150) or \
               (height >= 150) or \
               (length >= 150)
    
    # Check heavy condition: mass ≥ 20 kg
    is_heavy = mass >= 20
    
    # Sorting logic
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"