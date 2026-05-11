# HealthApp - Emergency Alert System
# This is the brain behind the SOS button

import datetime

def create_emergency_alert(caller_type, emergency_type, location):
    
    time_now = datetime.datetime.now()
    
    alert = {
        "alert_id": time_now.strftime("%Y%m%d%H%M%S"),
        "caller_type": caller_type,
        "emergency_type": emergency_type,
        "location": location,
        "time": time_now.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "ACTIVE"
    }
    
    return alert

def display_alert(alert):
    print("=" * 40)
    print("   EMERGENCY ALERT TRIGGERED")
    print("=" * 40)
    print(f"Alert ID     : {alert['alert_id']}")
    print(f"Caller       : {alert['caller_type']}")
    print(f"Emergency    : {alert['emergency_type']}")
    print(f"Location     : {alert['location']}")
    print(f"Time         : {alert['time']}")
    print(f"Status       : {alert['status']}")
    print("=" * 40)
    print("Connecting to nearest doctor...")

# Test it
alert = create_emergency_alert("Bystander", "Road Accident", "Westlands, Nairobi")
display_alert(alert)