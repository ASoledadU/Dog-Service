import json
import datetime

SERVICES_FILENAME = "./services.json"
TRANSACTIONS_FILENAME = "./transactions.txt"
now = datetime.datetime.now()


def print_welcome_message():
    print(
        """
                         .--~~,__
            :-....,-------`~~'._.'
            `-,,,  ,_      ;'~U'
            _,-' ,'`-__; '--.
            (_/'~~      ''''(;
 WELCOME TO LUXURY DOG SERVICES!
    """
    )
    print("These are the services we offer:")
    line_width = 8
    print("".ljust(line_width) + "Bath.......$25.00")
    print("".ljust(line_width) + "Massage....$15.00")
    print("".ljust(line_width) + "Walk.......$10.00")
    print("".ljust(line_width) + "Play.......$20.00")


def dog_spa():
    with open(SERVICES_FILENAME) as file:
        service_list = json.load(file)
    print_welcome_message()
    while True:
        ask = input("Which service would you like to order today? ")

        if ask == "bath":
            print(ask, "what a good choice!")
            print(f'Your total is: ${service_list["services"][ask]["price"]}0')
            b = service_list["services"][ask]["price"]
            print("Thank you have a nice day!")
            with open(TRANSACTIONS_FILENAME, "a") as f:
                f.write("\n{}, {}, 25.0".format(now, ask))
            break
        elif ask == "massage":
            print(ask, "what a good choice!")
            print(f'Your total is: ${service_list["services"][ask]["price"]}0')
            print("Thank you have a nice day!")
            with open(TRANSACTIONS_FILENAME, "a") as f:
                f.write("\n{}, {ask}, 15.0".format(now))
            break
        elif ask == "walk":
            print(ask, "what a good choice!")
            print(f'Your total is: ${service_list["services"][ask]["price"]}0')
            print("Thank you have a nice day!")
            with open(TRANSACTIONS_FILENAME, "a") as f:
                f.write("\n{}, {ask}, 10.0".format(now))
            break
        elif ask == "play":
            print(ask, "what a good choice!")
            print(f'Your total is: ${service_list["services"][ask]["price"]}0')
            print("Thank you have a nice day!")
            with open(TRANSACTIONS_FILENAME, "a") as f:
                f.write("\n{}, {ask}, 20.0".format(now))
            break
        else:
            print(ask, "is an invalid option !")


if __name__ == "__main__":
    dog_spa()
