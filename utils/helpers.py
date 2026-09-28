
## **File 5: utils/helpers.py** (Helper Functions)

```python
"""
Helper functions for the Textile Fiber Explorer application.
"""

import json
import pandas as pd
from typing import Dict, List, Any
import pathlib

def load_fibers_data() -> List[Dict[str, Any]]:
    """
    Load fiber data from JSON file.
    
    Returns:
        List of fiber dictionaries
    """
    try:
        # Get the path to the data directory
        data_path = pathlib.Path(__file__).parent.parent / "data" / "fibers.json"
        
        with open(data_path, 'r') as file:
            fibers = json.load(file)
        
        return fibers
    except FileNotFoundError:
        print(f"Warning: Could not find {data_path}")
        return get_sample_fibers()
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return get_sample_fibers()

def get_sample_fibers() -> List[Dict[str, Any]]:
    """
    Return sample fiber data if the JSON file is not found.
    
    Returns:
        List of sample fiber dictionaries
    """
    return [
        {
            "name": "Cotton",
            "type": "Natural",
            "sustainability": "Medium",
            "properties": {
                "tensile_strength": "Medium",
                "moisture_absorption": "High",
                "elasticity": "Low",
                "thermal_conductivity": "Medium",
                "resistance_to_chemicals": "Low",
                "biodegradability": "High"
            },
            "advantages": [
                "Comfortable and soft to wear",
                "Excellent breathability",
                "Hypoallergenic",
                "Good moisture absorption",
                "Easy to dye and print"
            ],
            "limitations": [
                "Wrinkles easily",
                "Shrinks when washed",
                "Weakens when wet",
                "Susceptible to mildew",
                "Can be damaged by acids"
            ],
            "applications": [
                "T-shirts",
                "Jeans",
                "Bed sheets",
                "Towels",
                "Underwear",
                "Dresses",
                "Shirts",
                "Curtains"
            ],
            "production_countries": ["China", "India", "USA"],
            "production_shares": [25.0, 22.0, 15.0],
            "production_trend": 1.2,
            "did_you_know": "Cotton has been cultivated for over 7,000 years and was independently domesticated in both the Old and New Worlds."
        },
        {
            "name": "Polyester",
            "type": "Synthetic",
            "sustainability": "Low",
            "properties": {
                "tensile_strength": "High",
                "moisture_absorption": "Very Low",
                "elasticity": "Medium",
                "thermal_conductivity": "Low",
                "resistance_to_chemicals": "High",
                "biodegradability": "Very Low"
            },
            "advantages": [
                "Strong and durable",
                "Wrinkle-resistant",
                "Quick-drying",
                "Resistant to chemicals and mildew",
                "Retains shape well"
            ],
            "limitations": [
                "Poor breathability",
                "Can feel clammy",
                "Static electricity buildup",
                "Non-biodegradable",
                "Made from petroleum"
            ],
            "applications": [
                "Sportswear",
                "Outerwear",
                "Bedding",
                "Carpets",
                "Ropes",
                "Conveyor belts",
                "Sailcloth",
                "Medical implants"
            ],
            "production_countries": ["China", "India", "USA"],
            "production_shares": [35.0, 18.0, 12.0],
            "production_trend": 1.5,
            "did_you_know": "Polyester was first patented in 1941 and became popular in the 1970s as a 'wonder fabric'."
        },
        {
            "name": "Wool",
            "type": "Natural",
            "sustainability": "High",
            "properties": {
                "tensile_strength": "Medium",
                "moisture_absorption": "High",
                "elasticity": "High",
                "thermal_conductivity": "Low",
                "resistance_to_chemicals": "Low",
                "biodegradability": "High"
            },
            "advantages": [
                "Excellent insulation",
                "Naturally flame-resistant",
                "Absorbs moisture without feeling wet",
                "Elastic and resilient",
                "Biodegradable"
            ],
            "limitations": [
                "Can shrink when washed",
                "Can be itchy",
                "Requires special care",
                "Can be damaged by moths",
                "Expensive"
            ],
            "applications": [
                "Sweaters",
                "Suits",
                "Blankets",
                "Carpets",
                "Winter coats",
                "Socks",
                "Upholstery",
                "Insulation"
            ],
            "production_countries": ["Australia", "China", "New Zealand"],
            "production_shares": [30.0, 18.0, 12.0],
            "production_trend": 0.8,
            "did_you_know": "Wool can absorb up to 30% of its weight in moisture without feeling wet, making it ideal for outdoor clothing."
        },
        {
            "name": "Silk",
            "type": "Natural",
            "sustainability": "Medium",
            "properties": {
                "tensile_strength": "High",
                "moisture_absorption": "Medium",
                "elasticity": "Medium",
                "thermal_conductivity": "Medium",
                "resistance_to_chemicals": "Low",
                "biodegradability": "High"
            },
            "advantages": [
                "Luxurious feel and appearance",
                "Strongest natural fiber",
                "Excellent drape",
                "Hypoallergenic",
                "Thermoregulating"
            ],
            "limitations": [
                "Very expensive",
                "Requires dry cleaning",
                "Can be damaged by sunlight",
                "Weakens when wet",
                "Labor-intensive production"
            ],
            "applications": [
                "Evening gowns",
                "Ties",
                "Scarves",
                "Bedding",
                "Medical sutures",
                "Parachutes",
                "Insulation",
                "Art supplies"
            ],
            "production_countries": ["China", "India", "Uzbekistan"],
            "production_shares": [80.0, 15.0, 2.0],
            "production_trend": 0.9,
            "did_you_know": "It takes about 2,500 silkworms to produce one pound of raw silk, and a single silk filament can be up to 1,600 meters long."
        },
        {
            "name": "Nylon",
            "type": "Synthetic",
            "sustainability": "Low",
            "properties": {
                "tensile_strength": "Very High",
                "moisture_absorption": "Low",
                "elasticity": "High",
                "thermal_conductivity": "Medium",
                "resistance_to_chemicals": "High",
                "biodegradability": "Very Low"
            },
            "advantages": [
                "Extremely strong and durable",
                "Excellent elasticity",
                "Resistant to abrasion",
                "Quick-drying",
                "Easy to care for"
            ],
            "limitations": [
                "Poor UV resistance",
                "Can melt at high temperatures",
                "Non-biodegradable",
                "Can develop static",
                "Made from petroleum"
            ],
            "applications": [
                "Stockings",
                "Swimwear",
                "Sportswear",
                "Ropes",
                "Parachutes",
                "Toothbrush bristles",
                "Fishing line",
                "Carpets"
            ],
            "production_countries": ["China", "USA", "India"],
            "production_shares": [45.0, 20.0, 10.0],
            "production_trend": 1.1,
            "did_you_know": "Nylon was first introduced at the 1939 World's Fair and was initially called 'fiber 66' because of its molecular structure."
        }
    ]

def filter_fibers_by_type(fibers: List[Dict[str, Any]], fiber_type: str) -> List[Dict[str, Any]]:
    """
    Filter fibers by type.
    
    Args:
        fibers: List of fiber dictionaries
        fiber_type: Type to filter by (e.g., "Natural", "Synthetic")
    
    Returns:
        Filtered list of fibers
    """
    return [fiber for fiber in fibers if fiber["type"] == fiber_type]

def get_fiber_names(fibers: List[Dict[str, Any]]) -> List[str]:
    """
    Get list of all fiber names.
    
    Args:
        fibers: List of fiber dictionaries
    
    Returns:
        List of fiber names
    """
    return [fiber["name"] for fiber in fibers]

def calculate_property_average(fibers: List[Dict[str, Any]], property_name: str) -> float:
    """
    Calculate average value for a specific property across fibers.
    
    Args:
        fibers: List of fiber dictionaries
        property_name: Name of property to average
    
    Returns:
        Average value (converted to numeric scale)
    """
    # Convert property values to numeric scale
    property_scale = {
        "Very Low": 1,
        "Low": 2,
        "Medium": 3,
        "High": 4,
        "Very High": 5
    }
    
    values = []
    for fiber in fibers:
        prop_value = fiber["properties"].get(property_name, "Medium")
        values.append(property_scale.get(prop_value, 3))
    
    return sum(values) / len(values) if values else 0

def create_comparison_table(fibers: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Create a comparison table for selected fibers.
    
    Args:
        fibers: List of fiber dictionaries to compare
    
    Returns:
        DataFrame with comparison data
    """
    comparison_data = []
    
    for fiber in fibers:
        comparison_data.append({
            "Fiber": fiber["name"],
            "Type": fiber["type"],
            "Sustainability": fiber["sustainability"],
            "Tensile Strength": fiber["properties"].get("tensile_strength", "N/A"),
            "Moisture Absorption": fiber["properties"].get("moisture_absorption", "N/A"),
            "Top Producer": fiber["production_countries"][0] if fiber["production_countries"] else "N/A"
        })
    
    return pd.DataFrame(comparison_data)

def get_fiber_statistics(fibers: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Get overall statistics about the fiber database.
    
    Args:
        fibers: List of fiber dictionaries
    
    Returns:
        Dictionary with statistics
    """
    stats = {
        "total_fibers": len(fibers),
        "natural_fibers": len(filter_fibers_by_type(fibers, "Natural")),
        "synthetic_fibers": len(filter_fibers_by_type(fibers, "Synthetic")),
        "avg_sustainability_score": 0,
        "total_applications": 0,
        "unique_countries": set()
    }
    
    # Calculate sustainability scores
    sustainability_scores = {"Low": 1, "Medium": 2, "High": 3}
    scores = []
    
    for fiber in fibers:
        scores.append(sustainability_scores.get(fiber["sustainability"], 0))
        stats["total_applications"] += len(fiber["applications"])
        stats["unique_countries"].update(fiber["production_countries"])
    
    stats["avg_sustainability_score"] = sum(scores) / len(scores) if scores else 0
    stats["unique_countries"] = len(stats["unique_countries"])
    
    return stats
