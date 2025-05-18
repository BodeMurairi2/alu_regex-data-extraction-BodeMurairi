#!/usr/bin/env python3
"""
This module uses regular expression to extract data
"""
import re

# open form.txt
def opened_file():
    with open("form.txt", "r") as file:
        data = file.read()
        return data

file_data = opened_file()

#............................
# Finding emails
def email_find(file_data):
    # email regex form to extract all emails
    email_regex = r"\b[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z0-9._]{2,}\b"

    """This function display all the emails found"""
    email_match = re.findall(email_regex, file_data)
    if email_match:
        for emails in email_match:
            print(emails)
    else:
        print("No email founds")

#.........................................
#  Finding URL
def find_url(file_data):
    """
    This function find all the urls inside form.txt
    """
    url_regex = r"https?:\/\/(?:www\.)?[a-zA-Z0-9?.\-_*+#*]+\.[a-zA-Z]{2,}(?:\/\S*)?"
    url_match = re.findall(url_regex, file_data)
    if url_match:
        for url in url_match:
            print(url)
    else:
        print("No Urls found")

#.............................
# Finding phone number
def find_phone_number(file_data):
    """This function returns all the phone numbers"""
    phone_number_regex = r"\+?(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}"
    phone_numbers = re.findall(phone_number_regex, file_data)
    if phone_numbers:
        for numbers in phone_numbers:
            print(numbers)
    else:
        print("No phone numbers found!")

#...................................
# Finding credit card

def find_credit_card(file_data):
    """This function extracts all the credit card numbers"""
    credit_card_regex = r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b"
    credit_card = re.findall(credit_card_regex, file_data)
    if credit_card:
        for card_numbers in credit_card:
            print(card_numbers)
    else:
        print("No credit cards found!")

#.....................................
# Finding time
def find_time(file_data):
    time_regex = r"(?:[0-9]|1[0-9]|2[0-3]):[0-5][0-9](?:\s?(?:PM|AM|pm|am))?"
    times = re.findall(time_regex, file_data)
    if times:
        for time in times:
            print(time)
    else:
        print("No times found!")

#............................................
# Currency amount
def find_amount(file_data):
    """
    This function finds all amount paid
    """
    amount_regex = "(?:\$|€|£|RWF|CDF)\s?[0-9]{1,3}(?:[.,][0-9]{3})*(?:[.,][0-9]{2})?"
    amounts = re.findall(amount_regex, file_data)
    if amounts:
        for amount in amounts:
            print(amount)
    else:
        print("No amount paid")

#..................................................
# Finding hashtags
def find_hashtags(file_data):
    """Find hashtags"""
    hashtags_regex = r"\#[a-zA-Z0-9_@&%$!()=+<>]+"
    hashtags = re.findall(hashtags_regex, file_data)
    if hashtags:
        for hashtag in hashtags:
            print(hashtag)
    else:
        print("No hashtags")

#......................................................
# Finding html tags
html_regex = r"<\/?[a-zA-Z][a-zA-Z0-9]*\b[^>]*\/?>"
htmls = re.findall(html_regex, file_data)
print(htmls)