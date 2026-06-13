# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import os
import datetime as dt
import pandas
import random
from pathlib import Path
import smtplib

MY_EMAIL = os.environ.get("susy101117@gmail.com")
MY_PASSWORD = os.environ.get("mmiy hhim ecba oino")


data = pandas.read_csv("./birthdays.csv")

now = dt.datetime.now()

for index, row in data.iterrows():
    if row["month"] == now.month and row["day"] == now.day:
        name = row["name"]
        email = row["email"]

        path = Path('./letter_templates')
        files = [f for f in path.iterdir() if f.is_file()]
        random_file = random.choice(files)

        with open(random_file) as sample:
            old_name = sample.read()
            new_name = old_name.replace('[NAME]', f"{name}")


        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="susy101117@gmail.com",
                                msg= new_name
                                )







