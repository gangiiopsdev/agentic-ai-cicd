from fastapi import FastAPI
import subprocess
gethostbyname = socket.gethostbyname

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        ip_address = gethostbyname(host)
        subprocess.call(["ping", ip_address], shell=False)
        return {"status": "completed", "ip_address": ip_address}
    except socket.gaierror as e:
        return {"status": "failed", "error": str(e)}