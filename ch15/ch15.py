from datetime import date


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    # We're looking for a year with the following conditions:
    # 1. Is a leap year
    # 2. Starts with 1 and ends with 6
    # 3. Jan 1 is a Thursday
    year = 1006
    while year < 2000:
        if is_leap_year(year) and date(year, 1, 1).weekday() == 3:
            print(f"Found: {year}")
        year += 10

    # We get a bunch of results. Second youngest is 1756.
    # Tip in the source is: "todo: buy flowers for tomorrow"
    # The day after the one marked is 27 Jan 1756, the birth of Mozart, which is the solution!


if __name__ == "__main__":
    main()
