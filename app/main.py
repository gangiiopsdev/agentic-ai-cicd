from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def ping(host: str):
        try:
            result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        result = SafeSubprocess.ping(host)
        return result
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}