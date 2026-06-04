from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.run safely with shell=False to avoid execution of untrusted input
    args = ['ping', host]
    process = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return process.stdout, process.stderr


@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the input to avoid injection attacks
        allowed_hosts = ['example.com']  # Example list of allowed hosts
        if host not in allowed_hosts:
            raise ValueError('Host is not allowed')
        result, error = safe_ping(host)
        if error:
            return {'status': 'failed', 'error': error}
        else:
            return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}