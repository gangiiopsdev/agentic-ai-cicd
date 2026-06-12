from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_call(command, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, check=True, capture_output=True, text=True)

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        result = SafeSubprocess.safe_call(f'ping -c 1 {shlex.quote(host)}')
        return {"status": "completed", "output": result.stdout, "stderr": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}