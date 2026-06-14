from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Replace special characters and ensure the input is safe
    sanitized_host = ''.join(char for char in host if char.isalnum() or char in '.-')
    return f'ping {sanitized_host}'

@app.get("/ping")
def ping(host: str):
    command = safe_ping(host)
    subprocess.call(command, shell=False)
    return {"status": "completed"}