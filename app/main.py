from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or ' ' in host or '<' in host or '>' in host or '"' in host or '&' in host or ';' in host:
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}