from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Splitting host into separate arguments to prevent shell injection
    args = shlex.split(host)
    try:
        result = subprocess.run(['ping'] + args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)