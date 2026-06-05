from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
            return {'status': 'completed' if output.returncode == 0 else 'failed', 'output': output.stdout.strip(), 'error': output.stderr.strip()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return PingCommand.execute(host)