from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Using check_output to safely execute the command
        result = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "result": result}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e.output)}