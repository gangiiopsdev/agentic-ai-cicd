from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(command: str):
    safe_command = 'ping' + shlex.quote(command)
    return safe_command

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid input"}
    args = secure_ping(host)
    output = subprocess.run(args, stderr=subprocess.STDOUT, capture_output=True, text=True)
    return {"status": "completed", "output": output.stdout}