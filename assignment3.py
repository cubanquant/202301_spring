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
    hours_accessed = {hour: 0 for hour in range(24)}
    csv_data = csv.reader(io.StringIO(urldata))
    image_counter = 0
    for row in csv_data:
        path_to_file = row[0]
        datetime_access_str = row[1]
        browser = row[2]
        # GIF, JPG, JPEG, PNG
        # Try to do this with a regular expression
        if re.search(r"\.JPG|.JPEG|\.GIF|\.PNG", path_to_file, re.IGNORECASE):
            image_counter = image_counter + 1

        # check the "browser" for specific string: Safari, Firefox, Chrome or MSIE
        if "Safari" in browser:
            browser_count["Safari"] += 1
        elif "Firefox" in browser:
            browser_count["Firefox"] += 1
        # do the same for the other browser

        # Convert datetime_access_str to datetime
        access_time = datetime.datetime.strptime(datetime_access_str, "%Y-%m-%d %H:%M:%S")
        hours_accessed[access_time.hour] += 1

    print(f"Safari count = {browser_count['Safari']}")
    print(f"Image count = {image_counter}")

    # after you have all the browser counts, find the highest and print the result
    most_popular_browser = max(browser_count, key=browser_count.get)

    print(hours_accessed)


def main(url):
    data = downloadData(url)
    process_data(data)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
