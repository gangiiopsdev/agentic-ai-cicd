from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with check=True and text=True
d_args = {
        'args': ['ping', host],
        'check': True,
        'text': True
    }
    result = subprocess.run(**d_args)
    return {"status": "completed", "output": result.stdout}