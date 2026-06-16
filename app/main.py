from fastapi import FastAPI
import subprocess
import shlex
class SecureSubprocess:
    @staticmethod
def secure_subprocess(command: str, args: list):
        full_command = [command] + args
        subprocess.run(full_command, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    secure_subprocess(shlex.quote('ping'), [shlex.quote(host)])
    return {"status": "completed"}