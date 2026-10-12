import re
import sys

def scan_code(diff_text: str):
    issues = []
    if re.search(r"\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13})\b", diff_text):
        issues.append("CRITICAL [PCI-DSS 3.4]: Potential unmasked Primary Account Number (PAN) detected.")
    if re.search(r"(log|logger|print|console\.log).*?(password|ssn|cvv|pin|secret|token)", diff_text, re.IGNORECASE):
        issues.append("HIGH [SOC2 CC6.1]: Potential plain-text logging of authentication or credential data.")
    return issues

if __name__ == "__main__":
    print("FinTech Compliance Scanner active.")
