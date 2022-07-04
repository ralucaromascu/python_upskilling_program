# json to csv

For this week's exercise, you are to download information in JSON format about the 1,000 largest cities. You can find it on GitHub [here](https://gist.github.com/Coraline13/d9cc3db0a77f548b3fe3a5f4267a9a9b), but you should download the "raw" version, which is [here](https://gist.githubusercontent.com/Coraline13/d9cc3db0a77f548b3fe3a5f4267a9a9b/raw/ba7ca3dff3acc140ca368b91bff195e2694383eb/cities.json).

After you retrieve the data and decode the JSON into Python data structures, I want you to create a CSV file. That file, which should have tabs as delimiters (rather than commas), should include the following data from the JSON file:
- city name
- state name
- city population
- city size rank

More specifically: you should write a function `cities_to_csv` that takes a URL and a filename. It'll download the JSON information from the URL, and then write it to the file specified.

The code needs to pass the tests in [ex5_json_to_csv_test.py](ex5_json_to_csv_test.py) file.
