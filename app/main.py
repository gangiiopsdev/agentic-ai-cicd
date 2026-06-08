from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Sanitize input to prevent command injection
        host = subprocess.quote(host)
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return output.decode('utf-8'), 0
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8'), e.returncode
global safe_ping
app = FastAPI()

@app.get("/" )
def home():
    return {"message": "Agentic Self-Healing Pipeline" }

@app.get("/ping")
def ping(host: str):
    output, status_code = SafePing.safe_ping(host)
    return {"status": status_code, "output": output}