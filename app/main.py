from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    cmd = ['ping', '-c', str(4), host]
    try:
        output = subprocess.check_output(cmd, input=b'', stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e.output)}