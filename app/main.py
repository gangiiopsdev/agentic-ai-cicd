from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate host format
    if re.match(r'^[0-9]+$', host.strip().replace('.', '')) is None:
        raise ValueError('Invalid host')
    return subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    try:
        status = safe_ping(host)
        return {"status": status}
    except ValueError as e:
        return {"error": str(e)}, 400