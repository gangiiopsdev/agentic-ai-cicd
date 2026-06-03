from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Secure implementation using subprocess.run without shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic input validation
        return {"status": "error", "message": "Invalid input"}
    status = execute_ping(host)
    return {"status": "completed", "output": status}