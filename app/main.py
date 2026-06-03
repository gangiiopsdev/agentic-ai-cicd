from fastapi import FastAPI
import subprocess
import shlex
class CommandSanitizer:
    @staticmethod
def sanitize(command):
        safe_command = [part for part in shlex.split(command) if part]
        return safe_command

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(CommandSanitizer.sanitize(f'ping {host}'), shell=False)
    return {"status": "completed"}