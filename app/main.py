from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        safe_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))
        try:
            subprocess.run(['ping', safe_host], check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f'Ping command failed with error {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingCommand.execute(host)
    return {"status": "completed"}