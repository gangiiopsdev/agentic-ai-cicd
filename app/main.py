from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host):
    # Secure implementation using subprocess.run with proper argument quoting
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    status = execute_ping(host)
    return {'status': 'completed', 'output': status}