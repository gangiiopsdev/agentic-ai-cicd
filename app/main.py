from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        ping_command = shlex.split(f'ping {host}')
        result = subprocess.run(ping_command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}