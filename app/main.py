from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ['ping', '-c', '1', host]  # Use -c to limit the number of pings
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}