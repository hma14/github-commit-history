from github import Github

def list_organization_repositories(org_name, access_token):
    try:
        # Replace 'YOUR_ACCESS_TOKEN' with your GitHub personal access token
        g = Github(access_token)
        
        # Get the organization
        org = g.get_organization(org_name)
        
        print(f"Repositories for {org_name}:")
        
        # Get all repositories for the organization
        repos = org.get_repos()
        
        for repo in repos:
            print(repo.name)
    
    except Exception as e:
        print(f"Error: {e}")

# Replace 'YOUR_ORGANIZATION_NAME' with the name of your organization
# Replace 'YOUR_ACCESS_TOKEN' with your GitHub personal access token
list_organization_repositories('omnae', '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')
