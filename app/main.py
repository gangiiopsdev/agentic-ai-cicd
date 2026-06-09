from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_host(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent injection attacks
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    result = ping_host(host)
    return {"status": "completed", "result": result}

def validate_host(host:
    # Implement your validation logic here, e.g., allow only certain domains or IP addresses
    allowed_hosts = ["example.com", "192.168.1.1"]
    return host in allowed_hosts