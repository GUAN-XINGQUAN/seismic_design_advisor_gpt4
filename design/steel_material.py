# This file is used to define the steel material.
# Re-factored by GUAN, XINGQUAN in Feb 2024


# #########################################################################
#            Define a class including steel material property             #
# #########################################################################


class SteelMaterial(object):
    """
    This class is used to define the steel material.
    It includes the following physical quantities:
    (1) Yield stress (Fy)
    (2) Ultimate stress (Fu)
    (3) Young's modulus (E)
    (4) Ry value
    """

    def __init__(self, yield_stress=50, ultimate_stress=65, elastic_modulus=29000, Ry_value=1.1, Rt_value=1.2):
        """
        :param yield_stress: yield stress of steel, unit: ksi
        :param ultimate_stress: tensile stress of steel, unit: ksi
        :param elastic_modulus: elastic modulus of steel, unit: ksi
        :param Ry_value: yield strength ratio
        :param Rt_value: tensile strength ratio
        """
        self.Fy = yield_stress
        self.Fu = ultimate_stress
        self.E = elastic_modulus
        self.Ry = Ry_value
        self.Rt = Rt_value