from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or len(host) > 10:
        return {"error": "Invalid input"}, 400
    command = shlex.split('ping ' + host)
    subprocess.call(command)
    return {"status": "completed"}