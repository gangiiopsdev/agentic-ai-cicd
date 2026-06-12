from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Add input validation and sanitization logic here
    return input_string

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = subprocess.quote(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}