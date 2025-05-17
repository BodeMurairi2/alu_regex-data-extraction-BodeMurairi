#!/usr/bin/env python3
"""
This module uses regular expression to extract data
"""
import re

email_regex = r"\b[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z0-9._]{2,}\b"

with open("forms.txt", "r") as file:
    data = file.read()

email_match = re.findall(email_regex, data)

if email_match:
    for emails in email_match:
        print(emails)
else:
    print("No email founds")
