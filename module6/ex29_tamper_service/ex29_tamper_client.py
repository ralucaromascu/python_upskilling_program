import requests

command = input("Do you want to scan or rescan a folder? Enter your command: scan/rescan\n")
print(command)
if command != 'scan' and command != 'rescan':
    print("Sorry, no valid command.")
    exit(0)

dir_path = input("Give me the folder you want:")
if command == 'scan':
    r = requests.get('http://127.0.0.1:5000/scan', params={'dirpath': dir_path})
    print(r.json())
else:
    r = requests.get('http://127.0.0.1:5000/rescan', params={'dirpath': dir_path})
    response = r.json()
    if len(response) == 1:
        print(response)
    else:
        message = f"Updates:\nFiles added: {response['added']}\n" \
                  f"Files changed: {response['changed']}\n" \
                  f"Files removed: {response['removed']}"
        print(message)
