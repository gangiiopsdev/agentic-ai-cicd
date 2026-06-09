from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        # Safe implementation using subprocess.run instead of subprocess.call
        args = ['ping', host]
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            return {'stdout': '', 'stderr': str(e)}
        return {'stdout': result.stdout, 'stderr': ''}
global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return PingCommand.safe_ping(host)