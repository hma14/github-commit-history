# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import csv


def JiraBoard():
    url = "https://omnae.atlassian.net/rest/api/3/search"

    auth = HTTPBasicAuth(
        "hma@omnae.com",
        "ATATT3xFfGF0Ll1vBvp7W0unXz0hZAg6BQNfVYMN34vCU5Z3vyaAf3loCFttswhi79P5M6YJyoP0SMq4qkielg49WESJkcMC-d3MIDcklZOY1mrNi1N3meaD4BHbc6l7jxc4iQvtKItZh5xfPjDdbmaz00zoH9tKeV2VVKqcOFPuYPnlKidvCQA=D06E0734",
    )

    headers = {"Accept": "application/json"}

    query = {"jql": "project = OE"}
    
    # Variables for pagination
    start_at = 0
    max_results = 100  # Adjust as needed

       # Initialize an array to store all issues
    all_issues = []

    #while True:
    while start_at < 100:
        # Set startAt and maxResults parameters for pagination
        query["startAt"] = start_at
        query["maxResults"] = max_results

        # Make a GET request to the Jira API
        response = requests.request("GET", url, headers=headers, params=query, auth=auth)

        # Parse the JSON response
        data = json.loads(response.text)

        # Get relevant data from each issue and append it to the array
        for issue in data["issues"]:
            all_issues.append(issue)

        # Increment startAt for the next page
        start_at += max_results

        # Check if there are more issues to retrieve
        if start_at >= data["total"]:
            break

    # Save data from Jira into a CSV file
    with open("issues.csv", "w", newline="", encoding="utf-8") as csvfile:
        # Define field names for the CSV file
        fieldnames = ["expand", "key", "id", "fields", "self"]
        
        # Create a CSV writer with the specified field names
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row to the CSV file
        writer.writeheader()

        # Write each issue to the CSV file
        for issue in all_issues:
            writer.writerow(issue)

    print(f"{len(all_issues)} issues written to issues.csv")


JiraBoard()
