from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to ensure it does not contain malicious content
    if any(char in host for char in [';', '&', '|', '`', '$', '(', ')']):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)