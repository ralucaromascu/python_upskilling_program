import re


def logtolist(filename):
    list_of_dict = []
    reg_ip_address = re.compile(r'^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.'
                                r'){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    reg_timestamp = re.compile(r'(\d{2}/[A-Z][a-z][a-z]/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})')
    reg_request = re.compile(r'(GET [^"]*)')
    with open(filename, 'r') as f:
        for line in f:
            my_dict = {'ip_address': line.split(' ', 1)[0],
                       'timestamp': line.split('[')[1].split(']')[0],
                       'request': line.split('"')[1].split('"')[0]
                       }
            if reg_ip_address.match(my_dict['ip_address']) \
                    and reg_request.match(my_dict['request']) \
                    and reg_timestamp.match(my_dict['timestamp']):
                list_of_dict.append(my_dict)
    return list_of_dict


if __name__ == '__main__':
    print(logtolist('mini-access-log.txt'))
