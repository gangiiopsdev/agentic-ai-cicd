from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Implement host validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):\n    if not validate_host(host):\n        return {"status": "invalid host"}\n    args = ['ping', host]\n    subprocess.call(args)\n    return {"status": "completed"}