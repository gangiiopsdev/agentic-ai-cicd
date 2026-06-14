from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, host: str):
        super().__init__(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

global app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    result = PingCommand(host)
    stdout, stderr = result.communicate()
    return {"status": "completed", "output": stdout.decode('utf-8'), "error": stderr.decode('utf-8')}