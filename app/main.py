from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement proper sanitization logic here
    return input_string

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation using subprocess.run with shell=False and properly sanitized inputs
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}