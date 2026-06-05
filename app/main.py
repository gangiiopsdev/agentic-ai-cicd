from fastapi import FastAPI
import subprocess
import shlex
class HostValidator:
    allowed_hosts = ['example.com', 'localhost']

    @staticmethod
def validate_host(host):
        if host not in HostValidator.allowed_hosts:
            raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input before executing the subprocess
    HostValidator.validate_host(host)
    result = subprocess.run(['ping', *shlex.split(host)], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}