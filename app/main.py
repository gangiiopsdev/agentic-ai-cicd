from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):

    # Sanitize the host input to prevent command injection
    sanitized_host = sanitize_input(host)

    # Secure implementation using subprocess.run with shell=False and args parameter
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)

    return {'status': 'completed', 'output': result.stdout}