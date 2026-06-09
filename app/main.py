from fastapi import FastAPI
import subprocess
git

class SafeSubprocess:
    def __init__(self):
        pass

    @staticmethod
def safe_ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
            return output
        except subprocess.CalledProcessError as e:
            return e.output

app = FastAPI()

git

git

git

git

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = SafeSubprocess.safe_ping(host)
    return {"status": "completed", "result": result}