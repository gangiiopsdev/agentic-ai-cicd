from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only known hosts
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts