alert = input("Enter security alert: ")

if "malware" in alert.lower():
    print("Malware Alert Detected")
elif "virus" in alert.lower():
    print("Virus Alert Detected")
elif "ransomware" in alert.lower():
    print("Ransomware Alert Detected")
else:
    print("No Threat Detected")

print("Created by Darwin Brown")