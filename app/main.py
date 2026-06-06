from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        if not host or 'localhost' in host.lower() or '127.0.0.1' in host.lower():
            return False
        command = ['ping', '-c', '4', host]
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(e.stderr)
            return False
        return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if SafePing.safe_ping(host):
        return {"status": "completed", "message": "Ping successful"}
    else:
        return {"status": "failed", "message": "Invalid host or error during ping"}