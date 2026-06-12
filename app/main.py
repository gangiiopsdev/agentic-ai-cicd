from fastapi import FastAPI
import subprocess
class CommandExecutor:
    @staticmethod
def safe_execute(command: list):
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT)
            return True, output.decode()
        except subprocess.CalledProcessError as e:
            return False, e.output.decode()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in ["example.com", "google.com"]:
        command = ["ping", host]
        success, output = CommandExecutor.safe_execute(command)
        if success:
            return {"status": "completed", "output": output}
        else:
            return {"status": "error", "output": output}
    else:
        return {"status": "error", "output": "Invalid host"}