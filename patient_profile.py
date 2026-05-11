#HealthApp -patient medical profile system 
#stores health info that doctors see instantly during emergencies


import datetime

def create_patient_profile():
    print("=" * 40)
    print("   CREATE YOUR MEDICAL PROFILE")
    print("=" * 40)
    print("This information will be shared with")
    print("doctors instantly during emergencies.")
    print("=" * 40)
    
    # Basic info
    name = input("Full name: ")
    age = input("Age: ")
    blood_type = input("Blood type (A+, B-, O+, etc): ")
    
    # Medical conditions
    print("\nDo you have any of these? (yes/no)")
    diabetes = input("Diabetes: ")
    hypertension = input("Hypertension/High blood pressure: ")
    asthma = input("Asthma: ")
    epilepsy = input("Epilepsy: ")
    hiv = input("HIV positive: ")
    other = input("Any other condition: ")
    
    # Medications and allergies
    medications = input("\nCurrent medications (or 'none'): ")
    allergies = input("Allergies especially to medicine (or 'none'): ")
    
    # Emergency contacts
    print("\nEmergency contact:")
    contact_name = input("Contact name: ")
    contact_phone = input("Contact phone: ")
    
    # Build the profile
    profile = {
        "name": name,
        "age": age,
        "blood_type": blood_type,
        "conditions": {
            "diabetes": diabetes,
            "hypertension": hypertension,
            "asthma": asthma,
            "epilepsy": epilepsy,
            "hiv": hiv,
            "other": other
        },
        "medications": medications,
        "allergies": allergies,
        "emergency_contact": {
            "name": contact_name,
            "phone": contact_phone
        },
        "profile_created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return profile

def display_profile(profile):
    print("\n" + "=" * 40)
    print("   PATIENT MEDICAL PROFILE")
    print("=" * 40)
    print(f"Name         : {profile['name']}")
    print(f"Age          : {profile['age']}")
    print(f"Blood Type   : {profile['blood_type']}")
    print(f"Diabetes     : {profile['conditions']['diabetes']}")
    print(f"Hypertension : {profile['conditions']['hypertension']}")
    print(f"Asthma       : {profile['conditions']['asthma']}")
    print(f"Epilepsy     : {profile['conditions']['epilepsy']}")
    print(f"HIV          : {profile['conditions']['hiv']}")
    print(f"Other        : {profile['conditions']['other']}")
    print(f"Medications  : {profile['medications']}")
    print(f"Allergies    : {profile['allergies']}")
    print(f"Contact      : {profile['emergency_contact']['name']} - {profile['emergency_contact']['phone']}")
    print("=" * 40)
    print("Profile ready — will be shared with doctor instantly!")

# Test it
profile = create_patient_profile()
display_profile(profile)