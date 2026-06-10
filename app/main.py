from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    full_command = [os.path.join(os.environ['PATH'], 'ping'), host]
    # Use subprocess.run instead of subprocess.call for better control and security
    result = subprocess.run(full_command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}