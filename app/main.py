from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"error": "Invalid host"}, 400
    args = ['ping', shlex.quote(host)]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        return {"error": "Ping failed: {}".format(error.decode())}, 500
    return {"status": "completed", "output": output.decode()}