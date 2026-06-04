from fastapi import FastAPI
import subprocess
global host_var
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    global host_var
    host_var = host

@app.on_event("startup")
def startup_event():
    subprocess.call(f"ping {host_var}", shell=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}