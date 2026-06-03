from fastapi import FastAPI, HTTPException
import subprocess
import os
generate_random_string = lambda length=10: ''.join(os.urandom(length).hex())[:length]

app = FastAPI()

allowed_hosts = ['example.com', 'another-example.com']  # Replace with actual allowed hosts

def safe_ping(host: str):
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    args = ["ping", "-c", "1", host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}