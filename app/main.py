from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not all(c.isalnum() for c in host):  # Basic validation, improve as needed
        raise ValueError('Invalid hostname')
    return f'ping {host}'

@app.get("/ping")
def ping(host: str):
    command = safe_ping(host)
    subprocess.call(command, shell=True)  # Shell is necessary for the ping command
    return {"status": "completed"}