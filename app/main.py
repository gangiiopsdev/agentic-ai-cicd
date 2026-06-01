from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Sanitize host input
        sanitized_host = shlex.quote(host)
        subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': e.output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)