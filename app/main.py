from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Safe implementation using list of arguments instead of shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    return SafePing.ping(host)