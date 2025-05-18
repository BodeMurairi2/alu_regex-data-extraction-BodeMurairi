#!/usr/bin/env python3
"""
This module uses regular expression to extract data
"""
import re
import time


# open form.txt
def opened_file():
    with open("form.txt", "r") as file:
        data = file.read()
        return data

#............................
# Finding emails
def find_email(file_data):
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
def find_htmls(file_data):
    html_regex = r"<\/?[a-zA-Z][a-zA-Z0-9]*\b[^>]*\/?>"
    htmls = re.findall(html_regex, file_data)
    if htmls:
        for html in htmls:
            print(html)
    else:
        print("No htmls tags found")

if __name__ == "__main__":
    """Running the application"""
    while True:
        # open the file
        file_data = opened_file()
        print("Welcome to our Regex pattern matching plateform\n")
        print("Here you can extract contents in your file\n")
        print("________________________________________")
        print("1.Find Emails inside your file")
        print("2.Find urls inside your file")
        print("3.Find phone numbers inside your file")
        print("4.Find credit cards inside your file")
        print("5.Find a/ll the times")
        print("6.Find amount/currency inside your file")
        print("7.Find hashtags inside your file")
        print("8.Find htmls tags inside your file")
        print("9.Exit!")
        print("___________________________________________")
        
        choice = int(input("Enter your choice between 1-9:\n"))
        
        if choice == 1:
            print("All Emails inside your file:\n")
            time.sleep(1)
            find_email(file_data)
        elif choice == 2:
            print("All urls inside your file")
            time.sleep(1)
            find_url(file_data)
        elif choice == 3:
            print("All phone numbers inside your file")
            time.sleep(1)
            find_phone_number(file_data)
        elif choice == 4:

        elif choice == 5:

        elif choice == 6:

        elif choice == 7:

        elif choice == 8:

        elif choice > 9:
            print("Exiting the application...\n")
            time.sleep(1)
            break

        else:
            print("Error! Please enter a valid number between 1-9 not decimal nor letters")
            continue
        