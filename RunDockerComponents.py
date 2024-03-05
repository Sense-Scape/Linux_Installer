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
    import os
    import subprocess

    current_directory = os.getcwd()
    
    for component_name, components_list in components.items():
        for component in components_list:
            
            if "C++" in component["Type"]:
                
                try:
                    # Go to where executable is
                    executable_path = os.path.join("Install/", component["name"]+"/")
                    os.chdir(current_directory + "/" + executable_path)

                    # Launch it in the background with outputs in the background
                    with open(os.devnull, 'w') as devnull:
                        subprocess.Popen(["./" + component["name"]], stdout=devnull, stderr=subprocess.PIPE)
                    
                    # And then go back
                    os.chdir(current_directory)

                except Exception as e:
                    print("Failed to launch " + component["name"] + " with error: " + str(e))
        
if __name__ == "__main__":
    main()