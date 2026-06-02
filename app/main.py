from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call for better control and security
    if not host or not isinstance(host, str) or ' ' in host:
        raise ValueError('Invalid input')
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
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