from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = date - today
        return delta.days
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'.")
        return None