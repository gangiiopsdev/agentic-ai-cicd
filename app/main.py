from fastapi import FastAPI
import subprocess
cimport re

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation
    safe_host = ''.join(c for c in host if re.match(r'[a-zA-Z0-9.-_]', c))
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}