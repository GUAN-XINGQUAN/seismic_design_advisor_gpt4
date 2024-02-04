# This file is used to declare all global variables.
# Re-factored by GUAN, XINGQUAN in Feb. 2024

from pathlib import Path
from steel_material import SteelMaterial
from sections import Sections

BASE_DIRECTORY = Path.cwd()

# Steel material unit: ksi
STEEL = SteelMaterial(yield_stress=50, ultimate_stress=65, elastic_modulus=29000, Ry_value=1.1)

# Different section database that will be used across the board
SECTION_DATABASE = Sections(BASE_DIRECTORY / 'section_database' / 'all_sections.jsonl')
BEAM_DATABASE = Sections(BASE_DIRECTORY / 'section_database' / 'all_sections.jsonl')
COLUMN_DATABASE = Sections(BASE_DIRECTORY / 'section_database' / 'all_sections.jsonl')


class GlobalVariables:
    """
    All parameters that may dominate the seismic design are stored under this class.
    These parameters may be subjected to change based on user's own experience and judgement.
    """
    # Ix ratio between exterior column and interior column
    EXTERIOR_INTERIOR_COLUMN_RATIO = 1.0
    # Zx ratio between beam and interior column
    BEAM_TO_COLUMN_RATIO = 0.6
    # Define the number of stories that have identical member sizes when considering ease of construction
    IDENTICAL_SIZE_PER_STORY = 2
    # The ratio between upper column Zx and lower column Zx
    UPPER_LOWER_COLUMN_Zx = 0.5
    # Define a coefficient that describes the accidental torsion
    # Imagine two special moment frames are symmetrically placed at the building perimeter
    # and the floor plan of the building is a regular shape (rectangle)
    # If the accidental torsion is not considered -> each frame is taken 0.5 of total lateral force
    # Then the ACCIDENTAL_TORSION = 1.0
    # If the accidental torsion is considered -> one frame will take 0.55 of total lateral force
    # since the center is assumed to be deviated from its actual location by 5% of the building dimension
    # Then the ACCIDENTAL_TORSION = 0.55/0.50 = 1.1
    ACCIDENTAL_TORSION = 0.50/0.50
    # Define a scalar to denote the drift limit which is based on ASCE 7-16 Table 12.12-1
    DRIFT_LIMIT = 0.020
    # Define a boolean variable to determine whether the Section 12.8.6.2 is enforced or not
    # Section 12.8.6.2:
    # For determining the design story drifts, it is permitted to determine the elastic drifts using
    # seismic design force based on the computed fundamental period without the upper limit (CuTa).
    # True -> Bound by upper limit, i.e., don't impose Section 12.8.6.2
    # False -> Not bound by upper limit, i.e., impose Section 12.8.6.2 requirement
    # Please note this period is only for computing drift, not for computing required strength.
    PERIOD_FOR_DRIFT_LIMIT = False
    # Declare global variables of strong column weak beam ratio for checking
    STRONG_COLUMN_WEAK_BEAM_RATIO = 1.0
    # When reduced-beam section is used at beam/column interface, we need the factor to bump up the drift.
    RBS_STIFFNESS_FACTOR = 1.10


if __name__ == '__main__':
    print("The design drift limit is: ")
    print(GlobalVariables.DRIFT_LIMIT)
    print("The section database is: ")
    print(SECTION_DATABASE.dataframe.head(3))
