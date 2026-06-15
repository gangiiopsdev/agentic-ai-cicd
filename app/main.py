from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host input to prevent injection attacks
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    try:
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}