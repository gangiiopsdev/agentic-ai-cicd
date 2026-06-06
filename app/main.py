from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check if the host is in a allowed list
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts