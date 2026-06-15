from fastapi import FastAPI
import subprocess
from pydantic import validator

def sanitize_input(input_str: str) -> str:
    # Sanitize or validate user input here
    return input_str.strip()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c 1', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}