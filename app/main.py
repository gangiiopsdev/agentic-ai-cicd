from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_call(command, *args, **kwargs):
        return subprocess.run(command, check=True, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    result = SafeSubprocess.safe_call(command)
    return {"status": "completed", "output": result.stdout}