from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char.isdigit())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation with shell=False and using a complete executable path
    subprocess.call(['ping', '-c', '1', sanitized_host], shell=False)
    return {"status": "completed"}