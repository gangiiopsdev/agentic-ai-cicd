from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if not host or not host.strip():
        raise ValueError("Invalid host")
    if ' ' in host:
        raise ValueError("Host contains invalid characters")
    return host

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("")
def ping(host: str):
    try:
        validated_host = validate_host(host)
        output = subprocess.check_output(shlex.split(f'ping -c 4 {validated_host}'), stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": e.output.decode()}
    except Exception as e:
        return {"status": "error", "message": str(e)}