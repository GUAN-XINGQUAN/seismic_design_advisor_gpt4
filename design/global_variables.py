import os

base_directory = os.get_cwd()

class GlobalVariables:
    EXTERIOR_INTERIOR_COLUMN_RATIO = 1.0
    EXTERIOR_INTERIOR_COLUMN_RATIO = 1.0
    BEAM_TO_COLUMN_RATIO = 0.6
    IDENTICAL_SIZE_PER_STORY = 2
    UPPER_LOWER_COLUMN_Zx = 0.5
    ACCIDENTAL_TORSION = 0.50/0.50
    DRIFT_LIMIT = 0.020
    PERIOD_FOR_DRIFT_LIMIT = False
    STRONG_COLUMN_WEAK_BEAM_RATIO = 1.0
    RBS_STIFFNESS_FACTOR = 1.10

class GlobalConstants:
    # The following three section database are global constants and no need to change across the board.
    SECTION_DATABASE = pd.read_csv(os.path.join(base_directory, 'section_database', 'section_database.csv'), header=0)
    COLUMN_DATABASE = pd.read_csv(os.path.join(base_directory, 'section_database', 'column_database.csv'), header=0)
    BEAM_DATABASE = pd.read_csv(os.path.join(base_directory, 'section_database', 'beam_database.csv'), header=0)