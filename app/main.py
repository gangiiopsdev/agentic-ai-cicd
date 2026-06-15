from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return process.communicate()

global safe_subprocess
safe_subprocess = SafeSubprocess()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    result = safe_subprocess.run(command)
    return {"status": "completed", "output": result[0]}