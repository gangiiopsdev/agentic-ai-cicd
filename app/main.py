from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Define a whitelist of allowed hosts or use other validation logic
    return host in ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    # Safe implementation using subprocess.run with shell=False and list of arguments
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}