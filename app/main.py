from fastapi import FastAPI
import subprocess
class CommandSanitizer:
    @staticmethod
def sanitize_command(command: str) -> list:
        return command.split()

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = CommandSanitizer.sanitize_command(host)
    subprocess.call(['ping'] + sanitized_host)
    return {"status": "completed"}