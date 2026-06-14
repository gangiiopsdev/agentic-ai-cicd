from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return shlex.quote(input_string)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Use a more secure method to execute the command, e.g., use subprocess.run directly with a list of arguments.
    result = subprocess.run(['ping', sanitized_host], check=True, shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}