import datetime


def tomorrow():
    today = datetime.date.today()
    return today + datetime.timedelta(days=1)

print(tomorrow())