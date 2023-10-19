# Installing Text-to-Speech Model

This guide will walk you through the installation process for running a text-to-speech model on your local machine. We will be using a Python library called TTS, which provides better audio quality compared to other text-to-speech models.

## Prerequisites

- Python 3.x
- pip package manager

## Installation Steps

### Windows

1. Open a command prompt.

2. Clone the repository by running the following command:
   ```
   git clone https://github.com/username/repository.git
   ```

3. Change to the cloned repository directory:
   ```
   cd repository
   ```

4. Create a new virtual environment:
   ```
   python -m venv env
   ```

5. Activate the virtual environment:
   ```
   env\Scripts\activate
   ```

6. Upgrade pip:
   ```
   python -m pip install --upgrade pip
   ```

7. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

8. Run the text-to-speech generation script:
   ```
   python better.py
   ```

### Mac/Linux

1. Open a terminal.

2. Clone the repository by running the following command:
   ```
   git clone https://github.com/username/repository.git
   ```

3. Change to the cloned repository directory:
   ```
   cd repository
   ```

4. Create a new virtual environment:
   ```
   python3 -m venv env
   ```

5. Activate the virtual environment:
   ```
   source env/bin/activate
   ```

6. Upgrade pip:
   ```
   python3 -m pip install --upgrade pip
   ```

7. Install the required packages:
   ```
   pip3 install -r requirements.txt
   ```

8. Run the text-to-speech generation script:
   ```
   python3 better.py
   ```

## Bug fixing

if you get the following error:

```
raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 11 column 21 (char 549)
```

It is a bug in the TTS package. It is due to a misspelled json file. 
It should be here some where: "./env/lib/python3.11/site-packages/TTS/.models.json"

To find the json file:

Go to the "manage.py" file. It should be located in your "env/" folder.
Something similar to this part: "./env/lib/python3.11/site-packages/TTS/utils/manage.py"

Here change the following:
```
with open(file_path, "r", encoding="utf-8") as json_file:
   self.models_dict = json.load(json_file)
```
to:

```
print("file path: ", file_path)
exit()
with open(file_path, "r", encoding="utf-8") as json_file:
   self.models_dict = json.load(json_file)
```

Rerun the script.

Now it should print the file path. Open that file with vscode or another editor. The editor will show you the problem. The problem is on line 10. Remove ",".

That it. Hopefully it works now!


## Conclusion

By following these steps, you should now have the text-to-speech model installed and running on your local machine. You can experiment with different models by checking the available models in the code and selecting the one you prefer. Enjoy generating more human-like voices!

If you found this guide helpful, please give it a thumbs up and consider subscribing to our channel for more tutorials.
