from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host):
        cmd = ['ping'] + shlex.split(host)
        result = subprocess.run(cmd, check=True, capture_output=True)
        return result.stdout.decode()
app = FastAPI()
@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get="/ping"
def ping(host: str):
    try:
        output = SafePing.safe_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}