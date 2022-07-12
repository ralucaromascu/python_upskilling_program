class LogDicts:
    pass


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
    print("test pull request")
