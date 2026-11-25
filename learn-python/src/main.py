from collections import defaultdict
from datetime import date, datetime

numberOne = 1
name = "  Python  "

my_dict = defaultdict(list)

my_dict["fruit"] = ["apples"]
my_dict["vegetable"] = ["carrots"]

print(my_dict)


def main():
    if numberOne <= 2:
        print("Hello from Python!")
        print("Today's date is:", date.yesterday())
        print("Current time is:", datetime.now().time().replace(microsecond=0))
    else:
        print("Goodbye from Python!")


def print_name():
    print(name.strip())


if __name__ == "__main__":
    main()
    print_name()
