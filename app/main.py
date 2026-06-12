from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def check_output(command: list) -> str:
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Failed to execute command: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = subprocess.quote(host)
    command = ['ping', safe_host]
    output = SafeSubprocess.check_output(command)
    return {"status": "completed", "output": output}