from fastapi import FastAPI
import subprocess
global ping_command
ping_command = "ping {}" if platform.system().lower() == 'windows' else "ping -c {}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.call(ping_command.format(host, 1), shell=True)
        return {"status": "completed", "result": result}
    except Exception as e:
        return {"error": str(e)}