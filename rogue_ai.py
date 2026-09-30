# ============================================================
# CMP 131 - ROGUE AI EMERGENCY DIAGNOSTIC SYSTEM
# Team members: Mikhail Arias
# ============================================================

print("========================================")
print("     ROGUE AI DIAGNOSTIC SYSTEM")
print("========================================")

# LEVEL 1 - TEMPERATURE DIAGNOSTIC
# Ask for the system temperature and make the required decision.
Temperature = int(input("Enter The System Temperature:"))
if Temperature >= 100:
    print("WARNING: SYSTEM OVERHEATING")
else:
    print("Temperature Normal")
# LEVEL 2 - POWER DIAGNOSTIC
# Ask for the battery percentage and make the required decision.
Battery_Percentage = int(input("Enter the Battery percentage:"))
if Battery_Percentage <= 20:
    print("LOW POWER")
else:
    print("Power Normal")

# LEVEL 3 - SECURITY DIAGNOSTIC
# Ask for the security status and make the required decision.
print("-------Status = danger / Safe-----------")
Security_Status = int(input("Enter The Security Status:"))
if Security_Status == ("danger"):
    print("SHUTDOWN REQUIRED")
else:
    print("System Secure")

print("========================================")
print("Diagnostic complete.")
print("========================================")
