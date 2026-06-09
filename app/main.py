from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host):
    # Secure implementation using subprocess.run instead of subprocess.call for better control and security
    command = shlex.split(f'ping {host}')
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = secure_ping(host)
    return {"status": "completed", "output": output}