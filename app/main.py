from fastapi import FastAPI
import socket
def run_ping(host):
    try:
        ip_address = socket.gethostbyname(host)
        return f'Ping to {ip_address} successful'
    except socket.gaierror as e:
        return f'Ping failed: {e}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)