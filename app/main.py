from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum() or '-' not in host:
        raise ValueError('Invalid host format')
    args = ['ping', '--force-v4-only', '--count=1', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}