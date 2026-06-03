from fastapi import FastAPI
import subprocess
get_ip_cmd = ['ping', '-c', '4', '{host}']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = subprocess.run(get_ip_cmd.format(host=host), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}