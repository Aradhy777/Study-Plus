from datetime import datetime, timedelta
import os


def format_date(date):
    if date:
        return date.strftime("%d-%m-%Y")
    return ""


def get_current_date():
    return datetime.now().date()


def minutes_to_hours(minutes):
    return round(minutes / 60, 2)


def ensure_charts_dir():
    charts_dir = "static/charts"
    if not os.path.exists(charts_dir):
        os.makedirs(charts_dir)
    return charts_dir


def get_week_dates():
    today = datetime.now().date()
    week_start = today - timedelta(days=today.weekday())
    return [week_start + timedelta(days=i) for i in range(7)]
