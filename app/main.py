from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Using subprocess.run and shlex.quote to avoid shell=True and command injection
    try:
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)