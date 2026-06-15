from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['.', '-', '_'])

def safe_ping(host: str):
    # Define a list of allowed hosts
    allowed_hosts = ['example.com', '192.168.1.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.run(['ping', *host.split()], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    sanitized_host = sanitize_input(host)
    safe_ping(sanitized_host)
    return {"status": "completed"}