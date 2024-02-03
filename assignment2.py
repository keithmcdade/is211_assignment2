import urllib.request
import shutil
import tempfile
import argparse
import logging
import datetime
import csv
from pprint import pprint


def download_data(url):
    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)
            return tmp_file.name


def process_data(file_contents):
    # initialize dictionary to store contents of csv file
    person_data = {}
    with open(file_contents, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                person_data[int(row["id"])] = (row.get("name"),
                    datetime.datetime.strptime(row.get("birthday"), '%d/%m/%Y').date())
            except ValueError as val_err:
                logging.error('“Error processing line #<linenum> for ID #<id>”')
                continue
        return person_data


def display_person(input_id, person_data):
    pprint(person_data)
    print('Person {} is {} with a birthday of {}'.format(person_data.get('id'), person_data.get('name'),
                                                           person_data.get('birthday')))


def assignment_2():
    logging.basicConfig(filename='error.log', filemode='w')



def main(url):
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='url to download', type=str, required=True,)
    args = parser.parse_args()
    main(args.url)
    assignment_2()
    # try:
    csv_output = download_data(args.url)
    # except:
    #     print('no')
    #try:
    process_output = process_data(csv_output)
    #except Exception as e:
        #print(e)
    display_output = display_person(1, process_output)

