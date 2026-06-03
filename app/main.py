from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return input_string.strip().replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):

    # Sanitize input to prevent command injection
    sanitized_host = sanitize_input(host)

    # Safe implementation using subprocess.run
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}