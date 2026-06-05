from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    # Secure implementation using a safe command and escaping
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)