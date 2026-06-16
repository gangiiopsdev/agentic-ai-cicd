from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Secure implementation
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return safe_ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}