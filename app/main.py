from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if '/' in host or '\' in host or '@' in host or ';' in host or '&' in host or '`' in host:
        raise ValueError("Invalid input detected")
    return safe_ping(host)