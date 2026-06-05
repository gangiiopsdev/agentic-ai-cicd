from fastapi import FastAPI

def safe_ping(host: str) -> bool:
    allowed_hosts = {'127.0.0.1', '::1'}
    if host not in allowed_hosts:
        raise ValueError("Invalid host input")

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    return safe_ping(host)