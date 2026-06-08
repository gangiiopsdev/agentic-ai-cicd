from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        command = shlex.split(command)
        return subprocess.run(command, *args, capture_output=True, text=True, check=True, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = SafeSubprocess.run(f"ping {host}")
        return {"status": "completed", "response": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "response": str(e)}