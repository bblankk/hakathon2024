import subprocess
import runLlama
import os
def run_command(command):
    try:
        a = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        print("Command Output:")
        print("a equals: ", command)
        print(a.stdout)
        
        if a.stderr:
            print("Command Errors:")
            print(a.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    vimeows_folder =  "W:/hakathon2024/modelScripts/vimeows/SunityAsset2.py"  # Assumes the folder is in the same directory as the script
    runFile = runLlama.runFile  # This should be dynamically set by the output of the runLlama script

    # Construct the full path to the file to run
    runFilePath = os.path.join(vimeows_folder, runFile)
    

    if os.path.isfile(vimeows_folder):
        print(f"Running the file: {vimeows_folder}")
        run_command(f"python {vimeows_folder}")
    else:
        print(f"Error: The file {vimeows_folder} does not exist.")

    print(f"Running the file: {runFile}")
    run_command(f"python {runFile}")
   