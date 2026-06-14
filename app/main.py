from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            args = ['ping', '-c', '1', host]
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)