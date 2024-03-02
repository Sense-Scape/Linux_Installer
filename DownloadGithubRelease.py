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

        # Remove zip file
        os.remove(repo_name+"/"+repo_name+".zip")

    else:
       print(f'Failed to download release assets. Status code: {response.status_code}')
       print(response.text)



def main():
    # Replace these values with your own
    repo_owner = 'Sense-Scape'
    repo_name = 'Sensor_Sim'
    release_id = 'v2.0.0'

    download_release_asset(repo_owner, repo_name, release_id)

if __name__ == "__main__":
    main()