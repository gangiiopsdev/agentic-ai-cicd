from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command: str):
        args = shlex.split(command)
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    result = SafeSubprocess.call(command)
    return {"status": "completed", "output": result}