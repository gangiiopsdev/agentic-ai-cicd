from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        command = ["ping", host]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "host_not_allowed"}