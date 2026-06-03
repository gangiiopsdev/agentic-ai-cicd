from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.Popen safely
    args = ['ping', host]
    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return process.stdout, process.stderr

def validate_host(host):
    allowed_hosts = ['example.com']  # Example list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result, error = safe_ping(host)
        if error:
            return {'status': 'failed', 'error': error}
        else:
            return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}