from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement your sanitization logic here
    return ''.join(e for e in input_string if e.isalnum())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}