from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(command: str):    result = subprocess.run(command.split(), check=True, capture_output=True, text=True)    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the input using shlex.quote
        safe_host = shlex.quote(host)
        command = f'ping {safe_host}'
        return run_ping(command)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': f'Ping failed: {e.stderr}'}