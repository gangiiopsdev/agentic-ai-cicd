from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        pass

    @staticmethod
def run(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use parameterized ping command to prevent command injection
        output = PingCommand.run(f'ping -c 4 {host}')
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "error", "message": str(e)}