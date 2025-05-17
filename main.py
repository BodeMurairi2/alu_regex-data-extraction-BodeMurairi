#!/usr/bin/env python3
"""
This module uses regular expression to extract data
"""
import re

# open form.txt
with open("form.txt", "r") as file:
    file_data = file.read()

# email regex form to extract all emails
email_regex = r"\b[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z0-9._]{2,}\b"

def email_find(email_regex, file_data):
    """This function display all the emails found"""
    email_match = re.findall(email_regex, file_data)
    if email_match:
        for emails in email_match:
            print(emails)
    else:
        print("No email founds")

#.........................................
#  Finding URL
url_regex = r"https?:\/\/(?:www\.)?[a-zA-Z0-9?.\-_*+#*]+\.[a-zA-Z]{2,}(?:\/\S*)?"

url_match = re.findall(url_regex, file_data)

if url_match:
    for url in url_match:
        print(url)
else:
    print("No Urls found")
