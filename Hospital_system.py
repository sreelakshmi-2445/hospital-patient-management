# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:03:00 2025

@author: HP
"""

# hospital_system.py
# Main system to manage patients, doctors, and appointments

# hospital_system.py
from patient import Patient
from Doctor import Doctor
from appointment import Appointment
from utils import generate_id, validate_phone, validate_age
from exceptions import (
    PatientExistsError,
    DoctorExistsError,
    AppointmentExistsError,
    InvalidPatientIDError,
    InvalidDoctorIDError,
    TimeSlotBookedError
)

class HospitalSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}

    # ----------------- Add New Patient -----------------
    def add_patient(self, name, age, phone):
        # Validate age and phone
        if not validate_age(age):
            print("❌ Error: Invalid age. Must be 1-120.")
            return
        if not validate_phone(phone):
            print("❌ Error: Invalid phone number. Must be 10 digits.")
            return

        # Generate patient ID
        patient_id = generate_id("PAT")
        if patient_id in self.patients:
            raise PatientExistsError(f"Patient ID {patient_id} already exists.")

        self.patients[patient_id] = Patient(patient_id, name, age, phone)
        print(f"✅ Patient added successfully. ID: {patient_id}")

    # ----------------- Add New Doctor -----------------
    def add_doctor(self, name, specialization):
        doctor_id = generate_id("DOC")
        if doctor_id in self.doctors:
            raise DoctorExistsError(f"Doctor ID {doctor_id} already exists.")

        self.doctors[doctor_id] = Doctor(doctor_id, name, specialization)
        print(f"✅ Doctor added successfully. ID: {doctor_id}")

    # ----------------- Book Appointment -----------------
    def book_appointment(self, patient_id, doctor_id, time):
        if patient_id not in self.patients:
            raise InvalidPatientIDError(f"Patient ID {patient_id} not found.")
        if doctor_id not in self.doctors:
            raise InvalidDoctorIDError(f"Doctor ID {doctor_id} not found.")

        doctor = self.doctors[doctor_id]
        if time in doctor.schedule:
            raise TimeSlotBookedError(f"Time slot {time} already booked for Doctor {doctor.name}.")

        # Generate appointment ID
        appointment_id = generate_id("APT")
        if appointment_id in self.appointments:
            raise AppointmentExistsError(f"Appointment ID {appointment_id} already exists.")

        patient = self.patients[patient_id]
        appointment = Appointment(appointment_id, patient, doctor, time)
        self.appointments[appointment_id] = appointment
        doctor.add_appointment(time)

        print(f"✅ Appointment booked successfully. ID: {appointment_id}")

    # ----------------- View Patients -----------------
    def view_patients(self):
        if not self.patients:
            print("No patients found.")
            return
        print("\n--- Patient List ---")
        for patient in self.patients.values():
            print(patient.get_details())

    # ----------------- View Doctors -----------------
    def view_doctors(self):
        if not self.doctors:
            print("No doctors found.")
            return
        print("\n--- Doctor List ---")
        for doctor in self.doctors.values():
            print(doctor.get_details())

    # ----------------- View Appointments -----------------
    def view_appointments(self):
        if not self.appointments:
            print("No appointments booked.")
            return
        print("\n--- Appointment List ---")
        for appointment in self.appointments.values():
            print(appointment.get_details())

    # ----------------- Cancel Appointment -----------------
    def cancel_appointment(self, appointment_id):
        if appointment_id not in self.appointments:
            print(f"❌ Error: Appointment ID {appointment_id} not found.")
            return
        appointment = self.appointments.pop(appointment_id)
        appointment.doctor.schedule.remove(appointment.time)
        print(f"✅ Appointment {appointment_id} cancelled successfully.")
