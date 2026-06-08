from fastapi import FastAPI
import subprocess
def escape_host(host: str):
    return host.replace(';', '').replace('&', '')

app = FastAPI()

def execute_ping(host: str):
    try:
        escaped_host = escape_host(host)
        subprocess.run(['ping', escaped_host], check=True)
        return True
    except subprocess.CalledProcessError as e:
        return False

@app.get("/ping")
def ping(host: str):