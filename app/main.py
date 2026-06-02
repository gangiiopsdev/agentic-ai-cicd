from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        return subprocess.run(command.split(), *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = SafeSubprocess.run(f'ping -c 1 {host}', shell=False)
    return {"status": "completed", "output": result.stdout.decode() if result.returncode == 0 else 'Ping failed'}