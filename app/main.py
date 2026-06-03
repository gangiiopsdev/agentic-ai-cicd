from fastapi import FastAPI
import subprocess
import shlex

class HostValidator:
    @staticmethod
def validate_host(host: str) -> bool:
        # Simple validation, replace with more robust logic as needed
        return host.replace('.', '').isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if HostValidator.validate_host(host):
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    else:
        return "Invalid host input"