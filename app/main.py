from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    if validate_host(host):\n        # Use a whitelist for the command and arguments\n        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)\n        return {"status": "completed", "output": result.stdout}\nexcept subprocess.CalledProcessError as e:\n    return {"status": "error", "output": str(e)}