from fastapi import FastAPI
import subprocess

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    return True  # Return a boolean value indicating if the host is valid

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = ['ping', '-c', '1', subprocess.check_output(f'echo {host}', shell=True).decode().strip()]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid host"}