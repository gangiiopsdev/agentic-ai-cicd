from fastapi import FastAPI
import subprocess
import shlex

def execute_ping(host: str):
    try:
        # Sanitize input using shlex.quote
        safe_host = shlex.quote(host)
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)