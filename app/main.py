from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run_command(command: str):
        try:
            result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
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
    result = SafeSubprocess.run_command(command)
    return {"status": "completed", "result": result}