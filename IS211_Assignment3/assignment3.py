# --url http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv

import requests
import argparse
import datetime
import csv
import re
import requests

def download_content(url): 
    """Download the content of the file from the given URL and return it as a string"""
    # download the web log file from the given URL
    response = requests.get(url)
    # raise an exception if the request failed
    response.raise_for_status()
    # get the content of the response as bytes
    print(f"Downloaded {len(response.content)} bytes")
    # decode the bytes into a string
    content = response.content.decode('utf-8') 
    return content

def process_file(content):
    """Process the file content and store the results in a list of dictionaries"""
    # create a CSV reader from the content of the file
    reader = csv.reader(content.splitlines())
    # skip the header row, not needed for this csv, but might be needed for others
    # next(reader)
    # create a list to store the results
    processed_list_of_dicts = []
    # iterate over the rows of the file
    for row in reader:
        # get the values of each column in the row
        path, datetime, browser, status, size = row
        # create a dictionary with the values of the current row
        row_dict = {
            'path': path,
            'datetime': datetime,
            'browser': browser,
            'status': status,
            'size': size
        }
        # append the dictionary to the list of results
        processed_list_of_dicts.append(row_dict)
    # return the list of results
    return processed_list_of_dicts

def image_search(processed_list_of_dicts):
    """Search for image requests in the processed file content"""
    # initialize the count of image requests and the total number of requests
    image_requests_list = 0
    total = len(processed_list_of_dicts)
    # create a list to store the results
    image_requests_list = []
    # iterate over the rows of the file
    for row in processed_list_of_dicts:
        # get the values of each column in the row
        path, datetime, browser, status, size = row.values()
        # check if the path corresponds to an image file
        if re.search(r'\.(jpg|gif|png)$', path):
            # append the dictionary to the list of results
            image_requests_list.append(row)
    print(f"Image requests account for {len(image_requests_list)/total*100:.1f}% of all requests")
    # return the list of results
    return image_requests_list


def search_browser_data(processed_list_of_dicts):
    """Search for browser requests in the processed file content and determine the percentage of browser requests and most popular browser"""
    # create a dictionary to count the occurrences of each browser
    browser_dict = {'Firefox': 0,
                    'Chrome': 0,
                    'MSIE': 0,
                    'Safari': 0}
    # iterate over the rows of the file
    for data_obj in processed_list_of_dicts:
        # use a regular expression to extract the browser name and version number
        match = re.search(r'(?i)(firefox|msie|chrome|safari)[\/\s]([\d.]+)', data_obj["browser"])
        if match:

            # get the browser name and version number
            browser_name = match.group(1)
            browser_version = match.group(2)

            # update the dictionary
            if browser_name in browser_dict:
                browser_dict[browser_name] += 1
            else:
                browser_dict[browser_name] = 1
    
    # calculate the total number of requests
    total_requests = sum(browser_dict.values())
    # calculate the percentage of requests for each browser
    for browser, count in browser_dict.items():
        percentage = count / total_requests * 100
        print(f'{browser} has {count} requests ({percentage:.2f}% of total)')

    # get the most popular browser
    most_popular = max(browser_dict, key=browser_dict.get)
    print(f"The most popular browser is {most_popular}")
    return most_popular


def search_hourly_data(processed_list_of_dicts):
    """Outputs a list of hours during which the site had the most hits sorted by the total number of hits in the day"""
    # create a dictionary to count the occurrences of each hour
    hour_dict = {}
    # iterate over the rows of the file
    for data_obj in processed_list_of_dicts:
        # get the hour from the datetime string
        hour = datetime.datetime.strptime(data_obj["datetime"], "%Y-%m-%d %H:%M:%S").hour
        # update the dictionary
        if hour in hour_dict:
            hour_dict[hour] += 1
        else:
            hour_dict[hour] = 1
    # sort the dictionary by the number of hits
    sorted_hours = sorted(hour_dict.items(), key=lambda x: x[1], reverse=True)
    # print the results
    print("The following hours had the most hits:")
    for hour, count in sorted_hours:
        print(f"{hour}:00 - {count} hits")
    return sorted_hours



def main(url):
    print(f"Running main with URL = {url}...")
    # download the file from the given URL
    content = download_content(url)
    # process the file content
    processed_list_of_dicts = process_file(content)
    # search for image requests
    image_requests_list = image_search(processed_list_of_dicts)
    # search for browser requests
    most_popular = search_browser_data(processed_list_of_dicts)
    # search for hourly requests
    sorted_hours = search_hourly_data(processed_list_of_dicts)



if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    # specifies that the function download_content should be called when the script is run
    parser.set_defaults(func=download_content)
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)

