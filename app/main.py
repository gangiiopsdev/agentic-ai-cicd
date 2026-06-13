from fastapi import FastAPI
import subprocess
generics = subprocess.Popen(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = generics.wait()
    return {"status": "completed", "result": result}