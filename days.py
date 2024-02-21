def days_to_years_months_days(days):

    years = days // 365

    remaining_days = days % 365


    months = remaining_days // 30

    remaining_days %= 30


    print(f"{days} days is approximately {years} years, {months} months, and {remaining_days} days.")


input_days = int(input("Enter the number of days: "))
days_to_years_months_days(input_days)