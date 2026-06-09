from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        command = ['ping', shlex.quote(host)]  # Use shlex.quote to escape special characters in the host parameter
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}