def check_risk():
    risk="Low"
    with open("scan.txt", "r") as file:
        data=file.read()
    if "22/tcp open" in data:
        risk="Medium"
    if "23/tcp open" in data or "3389/tcp open" in data:
        risk="High"
    return risk