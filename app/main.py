from fastapi import FastAPI
import subprocess
generics = 'ping -c 4 {}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.call(generics.format(host), shell=True)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500