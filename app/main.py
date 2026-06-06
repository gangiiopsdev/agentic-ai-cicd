from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        command = shlex.split(f'ping {host}')
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr.strip()}'

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)