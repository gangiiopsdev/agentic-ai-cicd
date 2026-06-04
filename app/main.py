from fastapi import FastAPI
import subprocess
good_subprocess = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = good_subprocess.communicate()
    return {"status": "completed", "output": result[0].decode('utf-8')}