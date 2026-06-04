from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/""
return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}