from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more valid hosts as needed
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ['ping', subprocess.check_output(['nslookup', host]).decode().strip().split()[4]]  # Use nslookup to resolve the hostname safely
    result = subprocess.run(command, check=True, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}