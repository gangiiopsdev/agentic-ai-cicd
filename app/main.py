from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    cmd = ['ping', host]
    try:
        result = subprocess.run(cmd, check=True, shell=False, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = safe_ping(shlex.quote(host))  # Validate and escape input
    return {'status': 'completed', 'output': output}