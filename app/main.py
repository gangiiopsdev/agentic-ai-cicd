from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "error", "result": "Invalid host"}
    result = execute_ping(host)
    return {"status": "completed", "result": result}

def is_valid_host(host):
    # Add validation logic to check if the host is valid
    return all(c.isalnum() or c in ['.', '-'] for c in host)