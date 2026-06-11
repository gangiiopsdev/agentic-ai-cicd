from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run with args parameter
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

class SecureFastAPI(FastAPI):
    @app.get("/ping")
    def ping(host: str):
        if not validate_host(host):
            raise ValueError("Invalid host")
        output = safe_ping(host)
        return {"status": "completed", "output": output}

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define allowed hosts
    if host in allowed_hosts:
        return True
    return False

global app
app = SecureFastAPI()

@app.get("/")
async def home():
    return {"message": "Agentic Self-Healing Pipeline"}