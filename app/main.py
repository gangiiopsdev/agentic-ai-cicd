from fastapi import FastAPI
import subprocess
class SafeCommandRunner:
    @staticmethod
def safe_ping(host):
        if host in ['localhost', '127.0.0.1']:
            return True
        return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if SafeCommandRunner.safe_ping(host):
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"status": "invalid host"}