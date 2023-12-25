from github import Github
from datetime import datetime
from config import access_token, organization_name
import csv

repositories = [ 'omnae', 'omnae-webapi', 'omnae-app', 'orders-service', 'companies-service', 'products-service', 'emails-service', 'app-gateway']

#repositories = ["emails-service"]


def list_organization_repositories(org_name, access_token):
    try:
        # Replace 'YOUR_ACCESS_TOKEN' with your GitHub personal access token
        g = Github(access_token)

        # Get the organization
        org = g.get_organization(org_name)

        # Get all repositories for the organization
        repos = org.get_repos()

        return repos

    except Exception as e:
        print(f"Error: {e}")


def get_commit_history(repo_name, org_name, access_token, start_date, end_date, output):
    try:
        print(f"Repositories for {repo_name}:")

        g = Github(access_token)

        # Get the organization
        org = g.get_organization(org_name)

        # Get the repository
        repo = org.get_repo(repo_name)

        # Get commits within the specified date range
        commits = repo.get_commits(since=start_date, until=end_date)

        with open(output, "w", encoding="utf-8") as csv_file:
            fieldnames = ["Commit SHA", "Author", "Date", "Commit Message"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            # Get commits within the specified date range
            commits = repo.get_commits(since=start_date, until=end_date)
            for commit in commits:
                # Get the commit details
                commit_details = repo.get_commit(commit.sha)
                writer.writerow(
                    {
                        "Commit SHA": commit.sha,
                        "Author": 
                            commit.author.name
                            if commit.author is not None
                            else "Unknown"
                        ,
                        "Date": commit.commit.author.date.strftime('%Y-%m-%d'),
                        "Commit Message": commit_details.commit.message,
                    }
                )

    except Exception as e:
        print(f"Error: {e}")


start_date = datetime.strptime("2021-02-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
end_date = datetime.strptime("2022-01-31T23:59:59Z", "%Y-%m-%dT%H:%M:%SZ")
output = "_commit_history.txt"

repos = list_organization_repositories(organization_name, access_token)
for repo in repos:
    if repo.name not in repositories:
        continue
    output = repo.name + "_commit_history.csv"
    get_commit_history(
        repo.name, organization_name, access_token, start_date, end_date, output
    )
