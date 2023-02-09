import argparse
import urllib.request
import logging
import datetime


def downloadData(url):
    """
    Reads data from a URL and returns the data as a string

    :param url:
    :return: the content of the URL
    """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response


def processData(file_content):
    result = dict()
    lines = file_content.split("\n")
    header = True
    for line in lines:
        # deals with the header
        if header:
            header = False
            continue
        # deals with empty lines
        if len(line) == 0:
            continue

        elements = line.split(",")
        id = int(elements[0])
        name = elements[1]
        try:
            birthday = datetime.datetime.strptime(elements[2], "%d/%m/%Y")
            result[id] = (name, birthday)
            print(id, name, birthday)
        except ValueError:
            print(f"************ Could not parse {elements[2]} to a date in format dd/mm/YYYY **********")

    return result


def displayPerson(id, personData):
    pass


def main(url):
    print(f"Running main with URL = {url}...")
    url_data = downloadData(url)
    processed_data = processData(url_data)
    while True:
        id = int(input("Enter an ID to search: "))
        if id < 0:
            break
        displayPerson(id, processed_data)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
