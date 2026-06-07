from fastapi import FastAPI
import subprocess
cimport = subprocess.call
csafe = subprocess.run

cdef ping(host: str):
    safe_ping = ["ping", host]
    try:
        cresult = csafe(safe_ping, capture_output=True, text=True)
        return {"status": "completed", "output": cresult.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)