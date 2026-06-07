from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        result = subprocess.run(command.split(), *args, **kwargs)
        return result

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safer implementation using SafeSubprocess
    if not host.strip():
        raise ValueError('Invalid host')
    SafeSubprocess.run(f"ping {host}")
    return {"status": "completed"}