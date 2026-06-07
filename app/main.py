from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it does not contain malicious content
    if not host.isalnum():
        raise ValueError('Invalid input')
    return run_ping(host)