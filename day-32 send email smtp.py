import smtplib

my_email = "harshadbagal518@gmail.com"
password = "nooreyhmhxzwzght"

with smtplib.SMTP("smtp.gmail.com")as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="harshadbagal77@gmail.com",
                        msg="subject:Hello\n\n this is the body of my email.")
