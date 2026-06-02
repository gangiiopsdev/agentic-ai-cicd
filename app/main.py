from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '_', '-'))

@app.get("/ping")
def ping(host: str):

    # Sanitize input to prevent command injection
    safe_host = sanitize_input(host)

    # Use subprocess.run instead of subprocess.call with shell=True
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)

    return {'status': 'completed', 'output': result.stdout}