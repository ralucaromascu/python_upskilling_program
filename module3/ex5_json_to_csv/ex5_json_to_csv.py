import csv
import json
from urllib.request import urlopen

gist_url = 'https://gist.githubusercontent.com/Coraline13/d9cc3db0a77f548b3fe3a5f4267a9a9b/raw' \
           '/ba7ca3dff3acc140ca368b91bff195e2694383eb/cities.json'


def cities_to_csv(my_url, filename):
    response = urlopen(my_url)
    data_json = json.loads(response.read())
    csv_data = open(filename, 'w')
    for info in data_json:
        data = [info['city'], info['state'], info['rank'], info['population']]
        wrt = csv.writer(csv_data, delimiter='\t')
        wrt.writerow(data)


if __name__ == '__main__':
    cities_to_csv(gist_url, 'cities.csv')
