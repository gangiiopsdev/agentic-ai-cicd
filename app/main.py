from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_safe_ping(host: str):
    # Use shlex to safely split the command line
    args = shlex.split(f'ping {host}')
    try:
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return run_safe_ping(host)