from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host):
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)