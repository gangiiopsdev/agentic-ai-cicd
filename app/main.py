from fastapi import FastAPI
import subprocess
class CommandExecutor:
    @staticmethod
def execute(command: str):
        try:
            result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    output = CommandExecutor.execute(command)
    return {"status": "completed", "output": output}