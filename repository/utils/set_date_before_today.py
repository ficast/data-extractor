from datetime import datetime, timedelta


def set_date_before_today(number_of_days):
    return datetime.strftime(datetime.now() - timedelta(number_of_days), '%Y-%m-%d')
