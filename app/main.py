from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    # Implement validation logic here (e.g., check allowed hosts)
    return host in ['example.com', 'another.example.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    # Safe implementation using subprocess.run with shell=False and a list of arguments
    result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}