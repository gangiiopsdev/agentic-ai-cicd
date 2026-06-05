from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_execute(command, args):
        return subprocess.run([command] + shlex.split(args), capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to avoid command injection
    safe_host = shlex.quote(host)
    result = SafePing.safe_execute('ping', safe_host)
    return {'status': 'completed', 'output': result.stdout}