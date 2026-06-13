from fastapi import FastAPI
import subprocess
global_ping_cache = {}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in global_ping_cache:
        try:
            result = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
            global_ping_cache[host] = result
        except subprocess.CalledProcessError as e:
            global_ping_cache[host] = str(e.output)
    return {"status": "completed", "result": global_ping_cache[host]}