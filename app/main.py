from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, host):
        super().__init__(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = PingCommand(host)
    output, error = result.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}