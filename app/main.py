from fastapi import FastAPI
import subprocess
cimport = ['ping'] + [subprocess.quote(host)]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.run(cimport, check=True)
    return {"status": "completed"}