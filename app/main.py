from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def call(command: list):
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f'Command failed with return code {e.returncode}')

global safe_subprocess
safe_subprocess = SafeSubprocess()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_subprocess.call(['ping', host])
    return {"status": "completed"}