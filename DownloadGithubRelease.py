def download_release_asset(repo_owner, repo_name, release_id):
    base_url = "https://github.com/"+repo_owner+"/"+repo_name+"/releases/download/"+release_id+"/"+repo_name+".zip"

    print("Downloading: " + base_url)

    # Download from Github
    import requests
    response = requests.get(base_url)

    if response.status_code == 200:

        # Download file from Github
        file = open(repo_name+".zip", "wb")
        file.write(response.content)
        file.close()

        #Unzip and installer
        import shutil
        import os
        os.makedirs(repo_name)
        shutil.move(repo_name+".zip", repo_name+"/"+repo_name+".zip")

        # Now unzip
        import zipfile
        with zipfile.ZipFile(repo_name+"/"+repo_name+".zip", 'r') as zip_ref:
            zip_ref.extractall(repo_name)

        # And provide read, write, run permissions
        import os
        os.chmod(repo_name+"/"+repo_name, 0o755)

        # Remove zip file
        os.remove(repo_name+"/"+repo_name+".zip")

    else:
       print(f'Failed to download release assets. Status code: {response.status_code}')
       print(response.text)

def main():
    # Replace these values with your own
    repo_owner = 'Sense-Scape'

    data = ""
    with open("Install.json", 'r') as file:
            data = file.read()

    # Convert file to json structure
    import json
    components = json.loads(data)

    # Get and install all required components
    for component_name, components_list in components.items():
        for component in components_list:
            download_release_asset(repo_owner, component["name"], component["version"])
        
if __name__ == "__main__":
    main()