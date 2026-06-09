from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        self.ping = subprocess.Popen(['ping', '-c', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = Ping()
    output, error = ping_command.ping.communicate()
    if error:
        return {"status": "error", "message": str(error)}
    else:
        return {"status": "completed", "output": output.decode()}