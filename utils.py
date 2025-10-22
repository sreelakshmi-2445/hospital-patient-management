# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 12:28:27 2025

@author: HP
"""

# utils.py
"""
Utility functions for Hospital Management System:
- ID generation
- Basic validations (age, phone, time slot)
"""

import random
import re

def generate_id(prefix):
    """
    Generate unique ID like:
    PAT123, DOC456, APT789
    """
    return f"{prefix}{random.randint(100,999)}"

def validate_age(age):
    """
    Validate age: must be a positive integer
    """
    try:
        age = int(age)
        return  0 < age <=120
    except ValueError:
        return False

def validate_phone(phone):
    """
    Validate phone number: must be 10 digits
    """
    return phone.isdigit() and len(phone) == 10

def validate_time_slot(time):
    """
    Validate appointment time in HH:MM format
    """
    pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d$"
    return re.match(pattern, time) is not None

