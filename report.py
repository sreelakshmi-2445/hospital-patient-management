# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:04:07 2025

@author: HP
"""

# report.py
# Generates simple reports from hospital system

class ReportGenerator:
    def __init__(self, hospital_system):
        self.system = hospital_system

    # Report: All doctor schedules
    def doctor_schedule_report(self):
        print("\n--- Doctor Schedules Report ---")
        if not self.system.doctors:
            print("No doctors available.")
            return
        for doc in self.system.doctors.values():
            if not doc.schedule:
                print(f"{doc.name} has no appointments.")
            else:
                print(f"{doc.name}'s schedule: {', '.join(doc.schedule)}")

    # Report: All patient appointments
    def patient_appointments_report(self):
        print("\n--- Patient Appointments Report ---")
        if not self.system.appointments:
            print("No appointments found.")
            return
        for appt in self.system.appointments.values():
            print(f"Patient {appt.patient.name} → Doctor {appt.doctor.name} at {appt.time}")
