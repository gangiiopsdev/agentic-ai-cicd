from fastapi import FastAPI
import subprocess
get_shell_access = False  # Control variable to prevent shell access by default
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        if '-' in host or '/' in host or ' ' in host:
            raise ValueError('Unsafe input detected')
        subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.ping(host)
    return {"status": "completed"}