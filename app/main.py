from fastapi import FastAPI
import subprocess
global ping
ping = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    output, error = ping.communicate()
    if error:
        return {"status": "error", "error": error.decode()}
    else:
        return {"status": "completed", "output": output.decode()}