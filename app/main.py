from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    # Define a set of safe hostnames or use regex to validate the hostname
    return hostname in ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {"status": "error", "message": "Unsafe hostname provided"}
    # Secure implementation using subprocess.run with shell=False and proper argument handling
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}