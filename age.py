import datetime
current_date = datetime.date.today()

date = input("Enter a date in format of DD-MM-YYYY: ")
year = int(date[-4:])
year_difference = current_date.year - year
print(year_difference)
