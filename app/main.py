from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        ping_cmd = ['ping', host]
        try:
            output = subprocess.run(ping_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            return {"status": "completed", "output": output.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)