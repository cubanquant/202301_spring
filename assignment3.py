import argparse
import urllib.request
import re
import datetime
import csv
import io


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


def process_data(urldata):
    """
    Process the data

    :param urldata:
    :return:
    """
    browser_count = {
        "MSIE": 0,
        "Safari": 0,
        "Chrome": 0,
        "Firefox": 0
    }
    csv_data = csv.reader(io.StringIO(urldata))
    image_counter = 0
    for row in csv_data:
        path_to_file = row[0]
        datetime_access_str = row[1]
        browser = row[2]
        # GIF, JPG, JPEG, PNG
        # Try to do this with a regular expression
        extension = path_to_file.upper().split(".")[-1]
        if extension in ["JPEG", "JPG", "GIF", "PNG"]:
            image_counter = image_counter + 1

        # check the "browser" for specific string: Safari, Firefox, Chrome or MSIE
        if "Safari" in browser:
            browser_count["Safari"] += 1

        # Convert datetime_access_str to datetime
        access_time = datetime.datetime.strptime(datetime_access_str, "%Y-%m-%d %H:%M:%S")
        print(access_time.hour)

    print(f"Image count = {image_counter}")
    # after you have all the browser counts, find the highest
    print(f"Safari count = {browser_count['Safari']}")


def main(url):
    data = downloadData(url)
    process_data(data)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
