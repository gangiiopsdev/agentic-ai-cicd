from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Secure implementation using subprocess.run without shell=True and validate host
    if not host.isalnum():
        raise ValueError("Invalid input")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        status = execute_ping(host)
    except ValueError as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed", "output": status}