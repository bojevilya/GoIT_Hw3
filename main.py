from datetime import datetime, date, timedelta


def get_days_from_today(date):
    try:
        choosen_date = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        delta = today - choosen_date
        return delta.days
    except ValueError:
        return ('Wrong format. Use "YYYY-MM-DD"')


choosen_date = ("2024-03-26")
print(get_days_from_today(choosen_date))
