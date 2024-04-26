from datetime import datetime


def get_days_from_today(date):
    try:
        chosen_date = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        delta = today - chosen_date
        return delta.days
    except ValueError:
        return ('Wrong format. Use "YYYY-MM-DD"')


date = "2024-03-26"
print(get_days_from_today(date))
