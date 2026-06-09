from fastapi import FastAPI
import subprocess
get_ip = lambda ip: subprocess.getoutput(f'ping {ip}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = get_ip(host)
    return {"status": "completed", "result": result}