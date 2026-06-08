from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}