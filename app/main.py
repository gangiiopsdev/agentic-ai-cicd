from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host: str):
    try:
        args = ['ping', '-c', '1'] + [arg for arg in host.split(' ') if arg.strip()]  # Validate and sanitize input
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    if not host:
        return {'status': 'error', 'message': 'Host parameter is required'}
    return run_ping(host)