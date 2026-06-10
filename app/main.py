from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse
import shlex

class SafeCommandRunner:
    @staticmethod
def run_command(command, args):
        full_command = [command] + list(shlex.split(args))
        return subprocess.run(full_command, capture_output=True, text=True, check=True)

app = FastAPI()

def validate_host(host):
    result = urlparse(host)
    return bool(result.scheme and result.netloc)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = SafeCommandRunner.run_command('ping', '-c 4 ' + host)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}