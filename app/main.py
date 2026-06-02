from fastapi import FastAPI
import subprocess
class CommandSanitizer:
    @staticmethod
def sanitize(command):
        safe_command = [part.strip() for part in command.split(' ') if part.strip()]
        return safe_command

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(CommandSanitizer.sanitize(['ping', host]), shell=False)
    return {"status": "completed"}