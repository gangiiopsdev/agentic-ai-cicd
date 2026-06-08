from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def execute_ping(host: str) -> None:
        try:
            output = subprocess.run(['ping', subprocess.shlex_quote(host)], capture_output=True, text=True, check=True)
            print(output.stdout)
        except subprocess.CalledProcessError as e:
            print(f'Ping failed: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingService.execute_ping(subprocess.shlex_quote(host))
    return {"status": "completed"}