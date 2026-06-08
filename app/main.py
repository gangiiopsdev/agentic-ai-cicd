from fastapi import FastAPI
import subprocess
class CommandExecutor:
    @staticmethod
def execute(command: str):
        try:
            result = subprocess.run(command.split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    result = CommandExecutor.execute(command)
    return {"status": "completed", "output": result}