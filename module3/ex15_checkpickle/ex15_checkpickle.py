import os
import pickle
import time
fields = ""


def get_people_from_checkpoint(cp_stem, timestamp):
    checkpoint = None
    people = []
    cp_stem = str(cp_stem)
    obj = os.scandir(os.getcwd())
    for entry in obj:
        if entry.is_file() and entry.name.startswith(cp_stem):
            timestamp_from_file = float(entry.name.split(cp_stem)[1])
            if timestamp_from_file <= float(timestamp):
                checkpoint = entry.name
                break
    if checkpoint:
        with open(checkpoint, "rb") as f:
            people.append(pickle.load(f))
    return people


def add_person(cp_stem):
    cp_stem = str(cp_stem)
    first_name = input("First name:")
    last_name = input("Last name:")
    email = input("Email:")
    if '@' not in email:
        print("Sorry, invalid email.")
    else:
        people = get_people_from_checkpoint(cp_stem, time.time())
        people.append({'first_name': first_name, 'last_name': last_name, 'email': email})
        timestamp = str(time.time())
        with open(cp_stem + timestamp, "wb") as f:
            pickle.dump(people, f)


def checkpickle(cp_stem='people-checkpoint-'):
    while 1:
        command = input("Enter a command - your options are:\n"
                        "'q'-Quit\n"
                        "'l'-List all people\n"
                        "'a'-Add a new person\n"
                        "'r'-Restore the adress book to a timestamp stage: ")

        if command == "q":
            return 0

        elif command == "l":
            people_list = get_people_from_checkpoint(cp_stem, time.time())
            print(people_list)

        elif command == "a":
            add_person(cp_stem)

        elif command == "r":
            timestamp_want = input("Give me a timestamp: ")
            people_list = get_people_from_checkpoint(cp_stem, timestamp_want)
        else:
            print("Sorry, wrong input.")


if __name__ == '__main__':
    checkpickle()
