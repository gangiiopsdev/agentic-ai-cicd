from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    try:
        # Use a full path for the ping command and ensure that host is sanitized
        output = subprocess.check_output(['/bin/ping', shlex.quote(host)], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    sanitized_host = shlex.quote(host)
    result = safe_ping(sanitized_host)
    return {"status": "completed", "result": result}