from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        args = ['ping', f'-c 1 {host}']  # Limiting the number of pings to mitigate injection risk
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
app = FastAPI()
@app.get("/ping")
def ping_wrapper(host: str):
    return SafePing.ping(host)