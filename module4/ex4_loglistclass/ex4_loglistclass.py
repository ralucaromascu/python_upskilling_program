import time


class LogDicts:
    def __init__(self, filename):
        self.list_of_dicts = []
        with open(filename, 'r') as f:
            for line in f:
                my_dict = {'ip_address': line.split(' ', 1)[0],
                           'timestamp': line.split('[')[1].split(']')[0],
                           'request': line.split('"')[1].split('"')[0]
                           }
                self.list_of_dicts.append(my_dict)

    def dicts(self, key=None):
        if key:
            new_list = sorted(self.list_of_dicts, key=key)
            return new_list
        else:
            return self.list_of_dicts

    def iterdicts(self, key=None):
        new_list = self.list_of_dicts
        if key:
            new_list = sorted(self.list_of_dicts, key=key)
        for one_dict in new_list:
            yield one_dict

    def earliest(self):
        return sorted(self.list_of_dicts, key=lambda d: time.strptime(d['timestamp'], '%d/%b/%Y:%H:%M:%S %z'))[0]

    def latest(self):
        return sorted(self.list_of_dicts, key=lambda d: time.strptime(d['timestamp'], '%d/%b/%Y:%H:%M:%S %z'))[-1]


    def for_ip(self, ip_address, key=None):
        new_list = self.list_of_dicts
        if key:
            new_list = sorted(self.list_of_dicts, key=key)
        my_ip_list = [item for item in new_list if item['ip_address'] == ip_address]
        return my_ip_list

    def for_request(self, text, key=None):
        new_list = self.list_of_dicts
        if key:
            new_list = sorted(self.list_of_dicts, key=key)
        my_text_list = [item for item in new_list if text in item['request']]
        return my_text_list


if __name__ == '__main__':
    ld = LogDicts('mini-access-log.txt')

    print(ld.dicts(key=None))

    print(ld.iterdicts(key=None))
    print(ld.earliest())
    print(ld.latest())
    print(ld.for_ip('66.249.65.12', key=None))
    print(ld.for_request('GET', key=None))


    def by_ip_address(one_log_dict):
        return one_log_dict['ip_address']


    print(ld.dicts(key=by_ip_address))
