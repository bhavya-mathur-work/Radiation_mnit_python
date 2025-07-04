# -*- coding: utf-8 -*-
"""Dose_cal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bo2H2cqB_QuaafF92hIaoTILEKy01pMW
"""

energy_per_particle_MeV = 100
flux = 1e4
exposure_time = 3600
mass = 70


energy_J = energy_per_particle_MeV * 1.60218e-13

total_energy = energy_J * flux * exposure_time

dose = total_energy / mass

print("Radiation_dose : ", dose, "Gy (Gray)")