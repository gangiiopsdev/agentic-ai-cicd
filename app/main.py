from fastapi import FastAPI
import subprocess
global allowed_hosts = ['example.com', 'another-example.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        # Use the full path of the executable to mitigate shell injection risks
        subprocess.run(["/bin/ping", host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400

def validate_host(host):
    # Implement a simple host validation logic
    global allowed_hosts
    return host in allowed_hosts