# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:00:45 2025

@author: HP
"""

# appointment.py
# Stores appointment details

class Appointment:
    def __init__(self, appointment_id, patient, doctor, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.time = time

    def get_details(self):
        return (f"Appointment ID: {self.appointment_id}, "
                f"Doctor: {self.doctor.name}, "
                f"Patient: {self.patient.name}, "
                f"Time: {self.time}")
