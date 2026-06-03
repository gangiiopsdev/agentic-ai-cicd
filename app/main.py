from fastapi import FastAPI
import subprocess
cimport = subprocess.run

class Command:
    def __init__(self, *args):
        self.args = args

    def execute(self, **kwargs):
        return cimport(self.args, check=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = Command('ping', host)
    result = command.execute()
    return {"status": "completed", "output": result.stdout}