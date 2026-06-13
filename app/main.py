from fastapi import FastAPI
import subprocess
class SafeCommand:
    @staticmethod
def run(command: str, *args):
        return subprocess.run([command] + list(args), capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = SafeCommand.run("ping", host)
    return {"status": "completed", "output": result.stdout}