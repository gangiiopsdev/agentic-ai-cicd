from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    # Basic sanitization: allow only alphanumeric characters and a few safe symbols
    return ''.join(char for char in input if char.isalnum() or char in '-._')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safer implementation without shell=True
    subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}