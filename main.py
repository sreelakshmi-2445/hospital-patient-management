# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:04:20 2025

@author: HP
"""

# main.py
# Entry point to run in Spyder
        
from Hospital_system import HospitalSystem
from report import ReportGenerator
from exceptions import (
    PatientExistsError, DoctorExistsError, AppointmentExistsError,
    InvalidPatientIDError, InvalidDoctorIDError, TimeSlotBookedError
)

def main():
    system = HospitalSystem()
    report = ReportGenerator(system)

    while True:
        print("\n===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Book Appointment")
        print("4. View Patients")
        print("5. View Doctors")
        print("6. View Appointments")
        print("7. Doctor Schedule Report")
        print("8. Patient Appointment Report")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            phone = input("Enter Phone: ")
            try:
                system.add_patient(name, age, phone)
            except PatientExistsError as e:
                print("Error:", e)

        elif choice == '2':
            name = input("Enter Name: ")
            spec = input("Enter Specialization: ")
            try:
                system.add_doctor(name, spec)
            except DoctorExistsError as e:
                print("Error:", e)

        elif choice == '3':
            patient_id = input("Enter Patient ID: ")
            doctor_id = input("Enter Doctor ID: ")
            time = input("Enter Appointment Time (HH:MM, 24-hour format): ")
            try:
                system.book_appointment(patient_id, doctor_id, time)
            except (AppointmentExistsError, InvalidPatientIDError,
                    InvalidDoctorIDError, TimeSlotBookedError) as e:
                print("Error:", e)

        elif choice == '4':
            system.view_patients()

        elif choice == '5':
            system.view_doctors()

        elif choice == '6':
            system.view_appointments()

        elif choice == '7':
            report.doctor_schedule_report()

        elif choice == '8':
            report.patient_appointments_report()

        elif choice == '9':
            print("Thank you for using the system! 👋")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
