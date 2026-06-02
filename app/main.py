from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        # Sanitize input to prevent command injection
        safe_host = ''.join(c for c in host if c.isalnum() or c in '.-_')
        args = ['ping', '-c', '1', safe_host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingCommand.execute(host)
    return {"status": "completed"}