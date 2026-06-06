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
        # Validate the input to prevent command injection
        safe_host = subprocess.list2cmdline([host])
        subprocess.call(['ping', safe_host])
        return {"status": "completed"}
    else:
        return {"status": "invalid host"}