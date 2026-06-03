from fastapi import FastAPI
import ping3

def run_ping(host):
    return str(ping3.ping(host)) if ping3.ping(host) else 'Ping failed'

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return run_ping(host)