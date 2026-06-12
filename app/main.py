from fastapi import FastAPI
import subprocess
def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    safe_host = escape_host(host)
    try:
        args = ['ping', '--'] + [safe_host]  # Use -- to prevent injection
        subprocess.run(args, check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}