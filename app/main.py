from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str) -> None:
        args = shlex.split(f"ping {host}")
        try:
            subprocess.run(args, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Ping failed: {e.stderr.strip()})

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    SafePing.safe_ping(host)
    return {"status": "completed"}