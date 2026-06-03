from fastapi import FastAPI
import subprocess
class CommandExecutionException(Exception):
    pass

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(['ping', host], check=True, text=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        raise CommandExecutionException(f'Ping failed with error: {e}') from None