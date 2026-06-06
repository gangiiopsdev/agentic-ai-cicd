from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

@app.get("/ping")
def ping(host: str):  
    # Validate the input to ensure it does not contain malicious content
    if '&&' in host or '|' in host or ';' in host:
        return "Invalid input"
    return execute_ping(host)