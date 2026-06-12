from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command: str, *args, **kwargs):
    args = shlex.split(command)
    return subprocess.run(args, *args, **kwargs)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = safe_subprocess(f'ping {host}', stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}