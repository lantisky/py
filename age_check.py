age = input("Please input your current age: ")

age_int = int(age)

years_remaining = 90 - age_int
month_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f"Your remaining month is {month_remaining} months, " +
      f"Your remaining weeks is {weeks_remaining} weeks, " +
      f"Your remaining days is {days_remaining} days. ")
