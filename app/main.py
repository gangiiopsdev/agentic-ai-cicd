from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input to prevent shell injection
    args = ['ping', host.replace('.', '-').replace('-', '')]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)
@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}