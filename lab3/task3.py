from datetime import datetime, timedelta


def payroll_calendar(year):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    # List to store the payroll dates
    payroll_dates = []

    for month in range(1, 13):
        # Determining the last day of the month
        if month == 12:
            last_day = datetime(year, month, 31)
        else:
            last_day = datetime(year, month + 1, 1) - timedelta(days=1)

        # Check if the last day of the month is saturday(5) or sunday(6)
        while last_day.weekday() >= 5:  # Monday=0, Sunday=6
            last_day -= timedelta(days=1)

        # Adding the date to the list in the appropriate format
        payroll_dates.append(f"{months[month - 1]}: {last_day.strftime('%d-%m-%Y')}")
    print(payroll_dates)
    return payroll_dates


# Example usage of the function for the year 2023
payroll_calendar(year_input := int(input('Podaj rok: ')))
