from fastapi import FastAPI
import subprocess
class SafeCommand:
    @staticmethod
def run_ping(host):
        try:
            # Sanitize input using shell=False and avoiding direct command construction
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e}'

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = SafeCommand.run_ping(host)
    return {"status": "completed", "result": result}