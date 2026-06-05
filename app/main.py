from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and a list of arguments
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping_handler(host: str):
    if not host.isalnum():  # Basic validation to ensure host contains only alphanumeric characters
        return {"status": "failed", "error": "Invalid input"}
    return ping(host)