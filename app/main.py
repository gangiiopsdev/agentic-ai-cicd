from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Add input validation and sanitization logic here
    return input_string

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = subprocess.quote(host)
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}