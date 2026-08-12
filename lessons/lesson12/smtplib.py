import smtplib

my_email = "senders@email.com"
password = "1234cdedpded"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="recipient@email.com",
        msg="Subject:Hell0\n\nThis is the body of my email.",
    )
