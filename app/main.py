from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value):
    if not value.strip().isalnum():
        raise ValueError("Invalid input")

@app.get="/ping"
def ping(host: str): 
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}