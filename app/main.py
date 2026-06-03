from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_str):
    return ' '.join(quote(x) for x in input_str.split())

app = FastAPI()

@app.get("/ping")
def ping(host: str):  
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}