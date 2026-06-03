from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host):
    try:
        # Validate and sanitize host input
        if not host.isalnum():
            raise ValueError("Invalid host")
        args = shlex.split('ping ' + host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except (subprocess.CalledProcessError, ValueError) as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation
    return execute_ping(host)