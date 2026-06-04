from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], timeout=5, text=True)
        return output
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = execute_ping(host)
    return {"status": "completed", "result": result}