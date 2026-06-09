from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Add your sanitization logic here
    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}