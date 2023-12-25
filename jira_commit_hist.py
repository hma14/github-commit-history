import requests
import json
from jira import JIRA

# Replace these placeholders with your Jira details
JIRA_URL = 'https://omnae.atlassian.net/jira/software'
JIRA_USERNAME = 'hma' #'hma@omnae.com'
JIRA_PASSWORD = 'Mfs585885'

# Jira REST API endpoint for searching issues
issue_url = f'{JIRA_URL}/rest/api/2/search'

# Replace 'your-project-key' with the actual project key you want to query
project_key = 'OE'

# JQL query to retrieve issues for a specific project
jql_query = f'project = "{project_key}"'

# Basic authentication
auth = (JIRA_USERNAME, JIRA_PASSWORD)

# Parameters for the request
params = {
    'jql': jql_query,
    'maxResults': 100,  # Adjust the number of results per page as needed
    'startAt': 0  # Adjust the starting index for pagination
}

# Make the request to Jira REST API
#response = requests.get(issue_url, auth=auth, params=params)

response = requests.get(issue_url, params=params)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    content_type = response.headers.get('Content-Type', '')
    if 'applciation/json' in content_type:
        # Parse the response JSON and process the data
        data = response.json()
        for issue in data['issues']:
                print(f"Issue Key: {issue['key']}")
                print(f"Summary: {issue['fields']['summary']}")
                print("\n---\n")
        
    elif 'text/html' in content_type:
        # Handle HTML content (potentially an error response)
        print("Error: HTML response received. Check for error messages.")
        #print(f"HTML Content: {response.text}")
        # Redirect output to a file
        with open('html_output.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
    else:
        print(f"Error: Unexpected content type: {content_type}")

else:
    print(f"Error: Unable to retrieve issues. Status code: {response.status_code}")
    print(f"Response Content: {response.text}")