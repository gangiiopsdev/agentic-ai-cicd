from fastapi import FastAPI
import subprocess
def escape_host(host):
    return host.replace(';', ' ').replace('&', ' ').replace('\', '').replace('*', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    escaped_host = escape_host(host)
    args = ['ping', escaped_host]
    subprocess.call(args)
    return {"status": "completed"}