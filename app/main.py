from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Use shlex.quote to safely handle user input
        safe_host = shlex.quote(host)
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)