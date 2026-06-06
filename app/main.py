from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_call(command: str):
        try:
            result = subprocess.run(command, shell=False, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    result = SafeSubprocess.safe_call(command)
    return {"status": "completed", "output": result}