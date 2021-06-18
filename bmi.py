"""
Calculating BMI of Patients

You are assisting a researcher with Python code that computes the Body Mass Index (BMI) of patients.
The researcher is concerned because all patients seemingly have unusual and identical BMIs, despite having
different physiques. BMI is calculated as weight in kilograms divided by the square of height in metres.

This program outputs the BMI of three patients. Each patient is represented by a tuple with the structure:
(weight in kilograms, height in meters)

This program is supposed to output:
Patient's BMI is: 21.604938271604937
Patient's BMI is: 22.1606648199446
Patient's BMI is: 51.90311418685122

Modified from https://swcarpentry.github.io/python-novice-inflammation/11-debugging/index.html
"""

patients = [(70, 1.8), (80, 1.9), (150, 1.7)]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(weight, height)
    print(f"Patient's BMI is: {bmi}")