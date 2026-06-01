from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host):
    # Secure implementation using subprocess.run with shell=False and quoted inputs
    try:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)