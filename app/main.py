from fastapi import FastAPI
import subprocess
def escape_host(host):
    # Simple escape mechanism for demonstration purposes
    return host.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    if not escaped_host.isalnum():
        raise ValueError("Invalid input for host")
    subprocess.run(["ping", escaped_host], check=True, text=True)
    return {"status": "completed"}