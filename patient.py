# -*- coding: utf-8 -*-
# patient.py
# Stores patient details

class Patient:
    def __init__(self, patient_id, name, age, phone):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.phone = phone

    def get_details(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Phone: {self.phone}"

