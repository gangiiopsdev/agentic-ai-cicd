from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        cmd = ['ping', host]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(shlex.quote(host))