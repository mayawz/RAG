# Add your utilities or helper functions to this file.

import openai
import os
import sys
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.                                                                                                                     # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key



def load_api_key(file_name: str):
    cwd = os.getcwd()
    file_path = os.path.join(f"{cwd[:-27]}/APIs/",file_name)
    
    if not os.path.exists(f"{file_path}"):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        api_key = file.read().strip()
    
    if not api_key:
        raise ValueError("The API key file is empty.")
    
    return api_key