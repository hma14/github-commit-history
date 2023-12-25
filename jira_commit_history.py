import requests
from requests.auth import HTTPBasicAuth
from jira import JIRA 

  
# Specify a server key. It should be your 
# domain name link. yourdomainname.atlassian.net 
jiraOptions = {'server': "https://omnae.atlassian.net"} 

jira = JIRA(options=jiraOptions, basic_auth=("hma@omnae.com", "ATATT3xFfGF0Ll1vBvp7W0unXz0hZAg6BQNfVYMN34vCU5Z3vyaAf3loCFttswhi79P5M6YJyoP0SMq4qkielg49WESJkcMC-d3MIDcklZOY1mrNi1N3meaD4BHbc6l7jxc4iQvtKItZh5xfPjDdbmaz00zoH9tKeV2VVKqcOFPuYPnlKidvCQA=D06E0734")) 

# Search all issues mentioned against a project name. 
for singleIssue in jira.search_issues(jql_str='project = OE'): 
    print('{}: {}:{}'.format(singleIssue.key, singleIssue.fields.summary, singleIssue.fields.reporter.displayName))


