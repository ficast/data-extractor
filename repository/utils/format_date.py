def format_date(reg_date):
    day = reg_date.strftime("%d")
    month = reg_date.strftime("%m")
    year = reg_date.strftime("%Y")
    return day, month, year
