from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the input to avoid shell injection
    args = ['ping'] + shlex.split(host)
    return args

@app.get("/ping")
def ping(host: str):
    safe_host = safe_ping(host)
    try:
        subprocess.run(safe_host, check=True, capture_output=True, text=True)
        return "Command executed successfully"
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e.stderr}"