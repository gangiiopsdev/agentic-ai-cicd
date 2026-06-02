from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    safe_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    return host in safe_hosts

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        args = ["ping", host]
        result = subprocess.run(args, check=True)
        return {"status": "completed", "result": result}
    else:
        raise ValueError("Invalid host")