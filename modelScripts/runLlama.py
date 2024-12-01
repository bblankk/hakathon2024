import subprocess
import pandas as pd

def generate_response_with_dynamic_csv(csv_file_path, user_question):
    # Define a basic template for asking the model
    template = """
    Hi, here's some system data: 
    """

    # Read the CSV data into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Convert the DataFrame to a dictionary (key-value pairs)
    data_dict = pd.Series(df['value'].values, index=df['key']).to_dict()

    # Prepare a string with the data extracted from the CSV
    csv_data = "\n".join([f"{key}: {value}" for key, value in data_dict.items()])

    # Prepare the input for the model with the extracted CSV data
    input_with_template = template + "  " + csv_data + "  " + f"Question: {user_question}"

    # Debugging output
   #  print("Prepared input:")
    # print(input_with_template)

  
    try:
        result = subprocess.Popen(
            ["ollama", "run", "llama3.2:1b"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8'
        )

        # Send the input to the model via stdin and get the response
        stdout, stderr = result.communicate(input=input_with_template)

        if result.returncode != 0:
            return f"Error running Ollama model: {stderr}"

        return stdout
    except Exception as e:
        return f"Error: {e}"


csv_file_path = 'W:/hakathon2024/getInfoScripts/system_info.csv'  

user_question = "Based on this information, can you choose one file : SunityAsset2.py or unityAsset3.py? Just give me the file name when you choose, nothing else. The format is very important, make sure there's nothing in front or behind , just the filename and .py . that's it. "

response = generate_response_with_dynamic_csv(csv_file_path, user_question)

print("Model Response:", response)

runFile = str(response)
print("\n" + response)

#are you sure ? + timer