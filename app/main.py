from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        output = subprocess.run(['ping', '-c', '1', safe_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)