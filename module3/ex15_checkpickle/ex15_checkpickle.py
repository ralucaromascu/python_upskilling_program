import os
import pickle
import time

fields = ""


def get_people_from_checkpoint(cp_stem, timestamp):
    checkpoint = None
    timestamps_from_files = []
    people = []
    cp_stem = str(cp_stem)
    obj = os.scandir(os.curdir)
    with obj as it:
        for entry in it:
            if entry.is_file() and entry.name.startswith(cp_stem):
                timestamps_from_files.append(float(entry.name.split(cp_stem)[1]))
    for timestamp_checkpoint in sorted(timestamps_from_files, reverse=True):
        if timestamp_checkpoint <= float(timestamp):
            checkpoint = cp_stem + str(timestamp_checkpoint)
            break

    if checkpoint:
        print(checkpoint)
        with open(checkpoint, "rb") as f:
            people = pickle.load(f)
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
            people_list = get_people_from_checkpoint(cp_stem, float(time.time()))
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
