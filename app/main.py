from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if not host or not isinstance(host, str) or ' ' in host:
            return False
        # Use a whitelist of allowed hosts or validate input more strictly
        command = ['ping', host]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if SafePing.safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid input"}