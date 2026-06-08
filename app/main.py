from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = ''.join(e for e in host if e.isalnum() or e in ('-', '.', '_'))
    subprocess.run(['ping', '-c', '1', safe_host], check=True)
    return {"status": "completed"}