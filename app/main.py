from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(command: str):
    safe_command = 'ping'.join([shlex.quote(arg) for arg in command.split()])
    return safe_command

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid input"}
    args = secure_ping(host)
    output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
    return {"status": "completed", "output": output}