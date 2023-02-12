import requests
import json

# Define the API endpoint and API key
endpoint = "https://api.openai.com/v1/completions"
api_key = "YOUR_API_KEY"

# Store the questions and answers in a string
qna_string = ""
divider = "----------------------------------"

# Read questions.txt file line by line
with open("questions.txt", "r") as f:
  lines = f.readlines()
  for question in lines:
    # Define the API request data
    data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 2000
    }

    # Set the API key as a header in the API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Send the API request and get the response
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

    # Check if the API request was successful
    if response.status_code == 200:
      # Get the response text and print it
      result = response.json()["choices"][0]["text"]
      qna_string = qna_string + "Q. " + question + \
          "A. " + (str(result)).strip() + "\n\n" + divider + "\n\n"

    else:
      # Print the error message if the API request was not successful
      qna_string = qna_string + "Q. " + question + "A. " + \
          response.text + "\n\n" + divider + "\n\n"
      print("Error:", response.text)

  # Write the questions and response text to a file
  with open("qna.txt", "w") as f:
    f.write(qna_string)

  print(qna_string)
