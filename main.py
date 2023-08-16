import random
import smtplib
import datetime as dt
import pandas

PLACEHOLDER = "[NAME]"


def send_email(name, email):
    my_email = "****"
    password = "****"
    ran_num = random.randint(1, 3)
    with open(f"./letter_templates/letter_{ran_num}.txt") as name_file:
        letter_contents = name_file.read()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"./letter_templates/new_letter.txt", "w") as complete_letter:
            complete_letter.write(new_letter)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        with open(f"./letter_templates/new_letter.txt", "r") as letter_to_send:
            letter = letter_to_send.read()
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Helloo {name}\n\n{letter}")


data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
now_year = now.year
now_month = now.month
now_day = now.day

birthday_people = data[data["month"] == now_month]

# Get the names of the people with birthdays today
birthday_names = birthday_people[birthday_people["day"] == now_day]["name"]
birthday_email = birthday_people[birthday_people["day"] == now_day]["email"]
# print("People with birthdays today:")

name_str = birthday_names.to_string(index=False)
email_str = birthday_email.to_string(index=False)

# print(email_str)

send_email(name_str, email_str)
