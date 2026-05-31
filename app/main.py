from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call for better control and security
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }

@app.get("/ping")
def ping(host: str):
    try:
        return secure_ping(host)
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "output": e.stdout,
            "error": e.stderr
        }