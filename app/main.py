from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str) -> bool:
        args = ['ping', '-c', '1', host]
        try:
            result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return True
        except Exception as e:
            print(f'Ping failed: {e}')
            return False
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = SafePing.safe_ping(host)
    if result:
        return {"status": "completed", "result": "success"}
    else:
        return {"status": "completed", "result": "failure"}