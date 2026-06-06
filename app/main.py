from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        result = subprocess.run(command.split(), *args, **kwargs)
        return result

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    # Safer implementation using SafeSubprocess
    SafeSubprocess.run(f"ping {host}")\n    return {"status": "completed"}