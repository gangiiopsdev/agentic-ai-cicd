from fastapi import FastAPI
import subprocess
class SafeCommand:
    @staticmethod
def ping(host):
        # Safe implementation
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return SafeCommand.ping(host)