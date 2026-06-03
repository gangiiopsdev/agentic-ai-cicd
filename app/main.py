from fastapi import FastAPI
import subprocess
globally_allowed_hosts = {"example.com", "localhost"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in globally_allowed_hosts:
        # Use a whitelist of allowed IPs instead of hostnames
        allowed_ips = {'127.0.0.1', '8.8.8.8'}
        if host in allowed_ips:
            subprocess.run(["ping", host], check=True)
        else:
            raise ValueError("IP not allowed")
    else:
        raise ValueError("Host not allowed")
    return {"status": "completed"}