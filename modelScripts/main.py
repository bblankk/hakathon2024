import subprocess
import runLlama
import run_cmd
import os

def main():
    csv_file_path = 'W:/hakathon2024/getInfoScripts/system_info.csv'  
    user_question = "Based on this information, can you choose one file : SunityAsset2.py or unityAsset3.py? Just give me the file name when you choose, nothing else. The format is very important, make sure there's nothing in front or behind, just the filename and .py . that's it."
    
    # Get the response from the model
    response = runLlama.generate_response_with_dynamic_csv(csv_file_path, user_question)
    
    # Step 2: Extract the file name from the response (if response is valid)
    runFile = response  # Ensure no extra spaces or newlines, but there's no need for this, just in case
    
    print(f"Model chose file: {runFile}")
    
    if runFile:  # If the model responded with a valid filename
        # Step 3: Run the command in run_cmd.py with the chosen file
        vimeows_folder = "W:/hakathon2024/modelScripts/vimeows/SunityAsset2.py" # + runFile 
        # runFilePath = os.path.join(vimeows_folder, runFile)  # Full path to the chosen file
        
        if os.path.isfile(vimeows_folder):
            print(f"Running the file: {vimeows_folder}")
            run_cmd.run_command(f"python {vimeows_folder}")
        else:
            print(f"Error: The file {vimeows_folder} does not exist.")
    else:
        print("Error: No valid file name returned from the model.")

if __name__ == "__main__":
    main()
