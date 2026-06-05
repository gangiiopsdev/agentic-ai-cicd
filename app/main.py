from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_subprocess(command, *args):
        try:
            result = subprocess.run([command] + list(args), check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_command = SafeSubprocess.safe_subprocess('ping', host)
    return {"status": "completed", "output": safe_command}