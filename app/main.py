from fastapi import FastAPI
import subprocess
glom = subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = glom.stdout if glom.returncode == 0 else 'Ping failed'
    return {"status": result}