from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Unauthorized host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and sanitization
    validate_host(host)
    subprocess.run(['ping', '-c', '1', subprocess.check_output(f'echo {host}', shell=True).decode().strip()], check=True, shell=False)
    return {"status": "completed"}