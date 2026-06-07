from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run and avoiding shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Using the safe implementation of the ping function
    output = safe_ping(host)
    return {"status": "completed", "output": output}