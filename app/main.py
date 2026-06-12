from fastapi import FastAPI
import subprocess
class CommandExecutor:
    @staticmethod
def execute(command: str):
        result = subprocess.run(command.split(), capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = f'ping {host}'
    result = CommandExecutor.execute(command)
    return {"status": "completed", "result": result}