##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address

from smtplib import SMTP
from datetime import datetime
import pandas
import random


My_email="vamshivardhan2020@gmail.com"
password="kvv15122002"

today=datetime.now()
today_tuple=(today.month,today.day)
data=pandas.read_csv("birthdays.csv")
dictionary={(data_row["month"],data_row["day"]):data_row for (index, data_row) in data.iterrows()}
if today_tuple in dictionary:
    birthday_person=dictionary[today_tuple]
    # print(birthday_person["name"])
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as  file:
        letter=file.read()
        contents=letter.replace("[NAME]", birthday_person["name"])
        print(contents)

    with SMTP("smtp.gmail.com") as collection:
        collection.starttls()
        collection.login(My_email,password)
        collection.sendmail(from_addr=My_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{contents}")
