from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    # Use the fully qualified path for ping if necessary
    # args = ['/sbin/ping', host] on Unix-like systems
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or '&&' in host or ';' in host:
        return {"error": "Invalid input"}, 400
    try:
        safe_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}, 500