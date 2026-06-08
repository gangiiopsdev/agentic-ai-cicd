from fastapi import FastAPI
import subprocess
class Sanitize:
    @staticmethod
def clean_input(input_string):
        return ''.join(e for e in input_string if e.isalnum() or e.isdigit())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = Sanitize.clean_input(host)
    # Use subprocess.run safely by avoiding shell=True and ensuring args is a list of strings
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout