from fastapi import FastAPI
import subprocess
import shlex
def is_safe_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"error": "Invalid host"}, 400
    args = shlex.split(f'ping {host}')
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return {"error": str(error)}, 500
    return {"status": "completed", "output": str(output)}