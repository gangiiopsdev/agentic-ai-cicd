from fastapi import FastAPI
import subprocess
cimport = lambda x: x.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    clean_host = cimport(host)
    subprocess.call(f"ping {clean_host}", shell=True)
    return {"status": "completed"}