from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate input to prevent command injection
    valid_hosts = ['example.com', 'localhost']
    if host in valid_hosts:
        try:
            args = ['ping', host]
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'result': response}