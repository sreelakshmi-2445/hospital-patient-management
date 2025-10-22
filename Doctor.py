# -*- coding: utf-8 -*-
# doctor.py
# Stores doctor details

class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.schedule = []  # appointment times for doctor

    def add_appointment(self, time):
        self.schedule.append(time)

    def get_details(self):
        return f"ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}"

