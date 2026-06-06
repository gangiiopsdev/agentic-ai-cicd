from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str) -> None:
        args = ['ping', host]
        try:
            output = subprocess.run(args, capture_output=True, text=True, check=True)
            print(output.stdout)
        except subprocess.CalledProcessError as e:
            print(f'Ping failed: {e}')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    SafePing.safe_ping(host)
    return {"status": "completed"}