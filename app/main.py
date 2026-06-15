from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_ping(host):
        try:
            output = subprocess.check_output(['ping', '-c', '4', host], universal_newlines=True)
            return output
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = SafeSubprocess.safe_ping(host)
    return {"status": "completed", "result": result}