def logtolist(filename):
    list_of_dict = []
    with open(filename, 'r') as f:
        for line in f:
            my_dict = {'ip_address': line.split(' ', 1)[0], 'timestamp': line.split('[')[1].split(']')[0],
                       'request': line.split('"')[1].split('"')[0]}
            list_of_dict.append(my_dict)
    return list_of_dict


if __name__ == '__main__':
    print(logtolist('mini-access-log.txt'))
