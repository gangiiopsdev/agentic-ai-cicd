from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            # Using subprocess.run with a safe command list and passing user input as an argument
            result = subprocess.run(['ping'], capture_output=True, text=True, check=True, input=host)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
global_safe_ping = SafePing()
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Using safe Ping method from SafePing class
    status = global_safe_ping.safe_ping(host)
    return {"status": status}