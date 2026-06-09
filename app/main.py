from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isdigit())

@app.get="/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.call with shell=False and arguments as a list
    subprocess.call(['ping', sanitized_host], shell=False)
    return {"status": "completed"}