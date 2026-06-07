from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: str):
        try:
            output = subprocess.run(command, shell=False, capture_output=True, text=True)
            return output.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/"}
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    result = SafeSubprocess.run(command)
    return {"status": "completed", "result": result}