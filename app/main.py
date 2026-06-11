from fastapi import FastAPI
import subprocess
get_ip = lambda ip: subprocess.run(['ping', '-c', '4', ip], capture_output=True, text=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = get_ip(host)
    return {"status": "completed", "output": result.stdout}