#!/usr/bin/env python3
"""
This module uses regular expressions to extract data.
"""

import re


# Open form.txt
def read_file():
    """Read content of form.txt and save
       inside data
    """
    with open("form.txt", "r") as file:
        data = file.read()
        return data


# Finding emails
def find_emails(content):
    """
    Print all emails found.
    """
    # Email regex form to extract all emails
    email_regex = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
    emails = re.findall(email_regex, content)
    if emails:
        for email in emails:
            print(email)
    else:
        print("No emails found")


# Finding URL
def find_urls(content):
    """
    Print all urls found.
    """
    url_regex = (r"https?:\/\/(?:www\.)?[a-zA-Z0-9?.\-_*+#*]+\."
                 r"[a-zA-Z]{2,}(?:\/\S*)?")
    urls = re.findall(url_regex, content)
    if urls:
        for url in urls:
            print(url)
    else:
        print("No URLs found")


# Finding phone number
def find_phone_numbers(content):
    """
    Print all phone numbers found.
    """
    phone_number_regex = r"\+?(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}"
    phone_numbers = re.findall(phone_number_regex, content)
    if phone_numbers:
        for phone_number in phone_numbers:
            print(phone_number)
    else:
        print("No phone numbers found!")


# Finding credit card
def find_credit_cards(content):
    """
    Print all credit cards found.
    """
    credit_card_regex = r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b"
    credit_cards = re.findall(credit_card_regex, content)
    if credit_cards:
        for card_numbers in credit_cards:
            print(card_numbers)
    else:
        print("No credit cards found!")


# Finding time
def find_times(content):
    """
    Print all the times found.
    """
    time_regex = r"(?:[0-9]|1[0-9]|2[0-3]):[0-5][0-9](?:\s?(?:PM|AM|pm|am))?"
    times = re.findall(time_regex, content)
    if times:
        for time_str in times:
            print(time_str)
    else:
        print("No times found!")


# Currency amount
def find_amounts(content):
    """
    Print all amounts found.
    """
    amount_regex = r"(?:\$|€|£|RWF|CDF)\s?[0-9]{1,3}" \
                   r"(?:[.,][0-9]{3})*(?:[.,][0-9]{2})?"
    amounts = re.findall(amount_regex, content)
    if amounts:
        for amount in amounts:
            print(amount)
    else:
        print("No amount paid")


# Finding hashtags
def find_hashtags(content):
    """
    print all hashtags found.
    """
    hashtags_regex = r"\#[a-zA-Z0-9_@&%$!()=+<>]+"
    hashtags = re.findall(hashtags_regex, content)
    if hashtags:
        for hashtag in hashtags:
            print(hashtag)
    else:
        print("No hashtags")


# Finding HTML tags
def find_html_tags(content):
    """
    print all HTML tags found.
    """
    html_regex = r"<\/?[a-zA-Z][a-zA-Z0-9]*\b[^>]*\/?>"
    html_tags = re.findall(html_regex, content)
    if html_tags:
        for tag in html_tags:
            print(tag)
    else:
        print("No HTML tags found")


if __name__ == "__main__":
    while True:
        content = read_file()  # open the file
        print("____________________________________________\n")
        print("Welcome to our Regex pattern matching platform\n")
        print("Here you can extract contents in your file\n")
        print("________________________________________")
        print("1. Find Emails inside your file")
        print("2. Find URLs inside your file")
        print("3. Find phone numbers inside your file")
        print("4. Find credit cards inside your file")
        print("5. Find all the times")
        print("6. Find amount/currency inside your file")
        print("7. Find hashtags inside your file")
        print("8. Find HTML tags inside your file")
        print("9. Exit!")
        print("___________________________________________")

        prompt = "Enter your choice between 1-9:\n"
        choice = input(prompt)

        if not choice.isdigit() or not (1 <= int(choice) <= 9):
            print("Error!❌ Please enter a valid number between 1-9,"
                  "no decimals or letters")
            continue

        choice = int(choice)

        if choice == 1:
            print("All Emails:\n")
            find_emails(content)

        elif choice == 2:
            print("All URLs inside your file:")
            find_urls(content)

        elif choice == 3:
            print("All phone numbers inside your file:")
            find_phone_numbers(content)

        elif choice == 4:
            print("All credit cards:\n")
            find_credit_cards(content)

        elif choice == 5:
            print("All the times:\n")
            find_times(content)

        elif choice == 6:
            print("All amounts:\n")
            find_amounts(content)

        elif choice == 7:
            print("Find all hashtags:\n")
            find_hashtags(content)

        elif choice == 8:
            print("All HTML tags:\n")
            find_html_tags(content)

        elif choice == 9:
            print("Exiting✅🎉 the application...\n")
            break
