from fastapi import FastAPI
import shlex
def safe_ping(host: str):
    if host.isalnum() and len(host) < 256:
        # Use shlex.quote to safely escape the input
        safe_host = shlex.quote(host)
        subprocess.run(['ping', '-c', '1', safe_host], check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}