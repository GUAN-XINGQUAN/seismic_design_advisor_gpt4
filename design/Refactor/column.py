# This file is used to define the class of column, which includes the axial, shear, and flexural strengths of column
# Refactored by GUAN, XINGQUAN in Feb 2024

from steel_material import SteelMaterial
from global_variables import COLUMN_DATABASE

class Column:
    """
    This class is used to define a column member, which has the following attributes:
    (1) Column section, a dictionary including the size and associated properties.
    (2) Column demand, a dictionary including axial, shear, and flexural demands.
    (3) Column strength, a dictionary including axial, shear, and flexural strengths.
    (4) Column flag, an integer with value of zero or nonzero. If it's zero, the column is feasible.
    """

    def __init__(self, section_size: str, axial_demand: float, shear_demand: float,
                 moment_demand_bot: float, moment_demand_top: float, Lx: float, Ly: float, steel: SteelMaterial):
        """
        This function initializes the attributes of class of column.

        Args:
            section_size: a string which specifies the size for column, e.g., "W14X730"
            axial_demand: a float number which describes axial demand, unit: kips
            shear_demand: a float number which describes shear demand, unit: kips
            moment_demand_bot: a float number which describes moment demand at bottom of column, unit: kip-inch
            moment_demand_top: a float number which describes moment demand at top of column, unit: kip-inch
            Lx: unbraced length in x direction, unit: inch
            Ly: unbraced length in y direction, unit: inch
        """
        # Assign the necessary information for column class
        self.section = COLUMN_DATABASE.get_section_property(section_size)
        self.demand = {'axial': axial_demand,
                       'shear': shear_demand,
                       'moment bottom': moment_demand_bot,
                       'moment top': moment_demand_top}
        self.unbraced_length = {'x': Lx, 'y': Ly}

        # Initialize the strength dictionary with an empty dictionary
        self.strength = {}
        # Initialize the dictionary to denote the possible failure mode (if any) of column
        self.is_feasible = {}
        # Initialize the dictionary to indicate the demand to capacity ratios
        self.demand_capacity_ratio = {}
        # Define a boolean flag to indicate the overall check results.
        self.flag = None

        # Define a hinge dictionary to store each parameters of OpenSees bilinear property
        self.plastic_hinge = {}

        # Using the following method to compute the strength and check whether strength is sufficient
        self.check_flange(steel)
        self.check_web(steel)
        self.check_axial_strength(steel)
        self.check_shear_strength(steel)
        self.check_flexural_strength(steel)
        self.check_combined_loads()
        self.compute_demand_capacity_ratio()
        self.calculate_hinge_parameters(steel)