from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    cmd = ['ping', *shlex.split(host)]
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e), 'stdout': e.stdout, 'stderr': e.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)