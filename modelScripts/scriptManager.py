#this officially works with model: distilgpt2

import subprocess
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load the model and tokenizer
model_name = "distilgpt2"  # Replace with "EleutherAI/gpt-neo-125M" if needed
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Use a pipeline for text generation
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=50)

# Map user input to commands
def map_input_to_command(user_input):
    commands = {
        "run backup": "python backup.py",
        "check disk": "dir",  # Replace with 'df -h' on Linux
        "list files": "dir",  # Replace with 'ls -la' on Linux
        "clear": "cls",       # Clear the terminal screen (for Windows)
        "exit": "exit",       # Close the program
    }
    # Return the mapped command or a default if the input doesn't match
    return commands.get(user_input.lower(), None)

# Execute a shell command
def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)  # Print the result of the command
    except Exception as e:
        print(f"Error: {e}")

# Main program loop
def main():
    print("Welcome to the AI-powered script manager!")
    while True:
        user_input = input("What do you want to do? (type 'exit' to quit): ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Use AI to generate a response based on the input
        ai_response = pipe(user_input)[0]["generated_text"]
        print(f"AI response: {ai_response.strip()}")

        # Extract the relevant command from AI response
        command = map_input_to_command(ai_response.strip().lower())
        
        if command:
            execute_command(command)
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
