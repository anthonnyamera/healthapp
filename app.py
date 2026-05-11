# HealthApp - Main Application
# Combines everything into one flow

import datetime

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_alert_id():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# ================================
# STEP 1: WELCOME SCREEN
# ================================
def welcome_screen():
    print("=" * 45)
    print("        WELCOME TO HEALTHAPP")
    print("   Emergency Response System - Kenya")
    print("=" * 45)
    print("Your GPS location has been detected.")
    print("You are in: Nairobi, Kenya")
    print("=" * 45)

# ================================
# STEP 2: WHO NEEDS HELP
# ================================
def who_needs_help():
    print("\nWHO NEEDS HELP?")
    print("-" * 45)
    print("1. Someone near me is injured (Bystander)")
    print("2. I am injured (Patient)")
    print("-" * 45)
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        return "bystander"
    elif choice == "2":
        return "patient"
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return who_needs_help()

# ================================
# STEP 3: EMERGENCY TYPE
# ================================
def select_emergency():
    print("\nWHAT IS THE EMERGENCY?")
    print("-" * 45)
    print("1. Road Accident")
    print("2. Medical Emergency")
    print("3. Fire")
    print("4. Other (describe your own)")
    print("-" * 45)
    
    choice = input("Enter 1, 2, 3 or 4: ")
    
    emergencies = {
        "1": "Road Accident",
        "2": "Medical Emergency",
        "3": "Fire"
    }
    
    if choice in emergencies:
        return emergencies[choice]
    elif choice == "4":
        other_emergency = input("Please describe the emergency: ")
        return other_emergency
    else:
        print("Invalid choice. Try again.")
        return select_emergency()

# ================================
# STEP 4: PATIENT MEDICAL PROFILE
# ================================
def get_patient_profile():
    print("\n" + "=" * 45)
    print("   YOUR MEDICAL PROFILE")
    print("Loading your saved profile...")
    print("=" * 45)
    
    name = input("Your full name: ")
    blood_type = input("Blood type (A+, B-, O+, etc): ")
    conditions = input("Any conditions (diabetes/asthma/none): ")
    medications = input("Current medications (or none): ")
    allergies = input("Allergies to medicine (or none): ")
    contact_name = input("Emergency contact name: ")
    contact_phone = input("Emergency contact phone: ")
    
    return {
        "name": name,
        "blood_type": blood_type,
        "conditions": conditions,
        "medications": medications,
        "allergies": allergies,
        "emergency_contact": f"{contact_name} - {contact_phone}"
    }

# ================================
# STEP 5: SEND ALERT
# ================================
def send_alert(caller_type, emergency_type, profile=None):
    print("\n" + "=" * 45)
    print("        EMERGENCY ALERT SENT!")
    print("=" * 45)
    print(f"Alert ID     : {get_alert_id()}")
    print(f"Caller       : {caller_type.upper()}")
    print(f"Emergency    : {emergency_type}")
    print(f"Location     : Nairobi, Kenya (GPS)")
    print(f"Time         : {get_timestamp()}")
    
    if profile:
        print("-" * 45)
        print("PATIENT MEDICAL PROFILE:")
        print(f"Name         : {profile['name']}")
        print(f"Blood Type   : {profile['blood_type']}")
        print(f"Conditions   : {profile['conditions']}")
        print(f"Medications  : {profile['medications']}")
        print(f"Allergies    : {profile['allergies']}")
        print(f"Contact      : {profile['emergency_contact']}")
    
    print("=" * 45)
    print("Status       : ACTIVE")
    print("Ambulance    : Dispatched")
    print("Doctor       : Connecting via video...")
    print("=" * 45)
    print("\nHelp is on the way! Stay calm.")
    print("A doctor will connect with you shortly.")

# ================================
# MAIN APP - RUNS EVERYTHING
# ================================
def run_app():
    welcome_screen()
    
    caller = who_needs_help()
    emergency = select_emergency()
    
    if caller == "patient":
        profile = get_patient_profile()
        send_alert(caller, emergency, profile)
    else:
        send_alert(caller, emergency)

# Start the app
run_app()