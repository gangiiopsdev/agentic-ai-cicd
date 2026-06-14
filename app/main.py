from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host name")
    # Sanitize the input to prevent command injection
    sanitized_host = ''.join(filter(str.isalnum, host))
    return safe_ping(sanitized_host)