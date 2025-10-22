# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 12:32:14 2025

@author: HP
"""

# exceptions.py
class HospitalError(Exception):
    """Base class for hospital system exceptions"""
    pass

class PatientExistsError(HospitalError):
    pass

class DoctorExistsError(HospitalError):
    pass

class AppointmentExistsError(HospitalError):
    pass

class InvalidPatientIDError(HospitalError):
    pass

class InvalidDoctorIDError(HospitalError):
    pass

class TimeSlotBookedError(HospitalError):
    pass
