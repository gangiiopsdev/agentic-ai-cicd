from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ' .-:' for c in host):
        raise ValueError("Invalid input")
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)