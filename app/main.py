from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['.', '-', '_', ''])

@app.get('/ping')
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_input(host))
    subprocess.run(['ping', sanitized_host], check=True, text=True)