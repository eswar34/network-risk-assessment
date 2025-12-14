from datetime import datetime

def generate_report(target, risk, ports):
    filename = f"report_{target.replace('.', '_')}.txt"

    with open(filename, "w") as file:
        file.write("SECURITY SCAN REPORT\n")
        file.write("=====================\n\n")
        file.write(f"Target       : {target}\n")
        file.write(f"Scan Time    : {datetime.now()}\n")
        file.write(f"Risk Level   : {risk}\n\n")

        file.write("Open Ports:\n")
        if ports:
            for port in ports:
                file.write(f"- {port}\n")
        else:
            file.write("No open ports found\n")

        file.write("\nRecommendation:\n")
        if risk == "High":
            file.write("Immediate security hardening required.\n")
        elif risk == "Medium":
            file.write("Review exposed services and restrict access.\n")
        else:
            file.write("System appears safe.\n")

    return filename
