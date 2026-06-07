from fastapi import FastAPI
import subprocess

allowed_hosts = ['example.com', 'test.com']

def safe_ping(host: str):
    if host not in allowed_hosts:
        return "Invalid input"
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, timeout=5, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class FastAPIApplication(FastAPI):
    @app.get("/ping")
    def ping(host: str):
        if host not in allowed_hosts:
            return "Invalid input"
        return safe_ping(host)

app = FastAPIApplication()