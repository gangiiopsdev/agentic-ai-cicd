from fastapi import FastAPI
import subprocess
def get_shell_access():
    return False  # Control function to prevent shell access by default

class SafeSubprocess:
    @staticmethod
def ping(host: str):
        if '-' in host or '/' in host:
            raise ValueError('Unsafe input detected')
        subprocess.call(['ping', host])  # Use list to avoid shell injection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.ping(host)
    return {"status": "completed"}