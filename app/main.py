from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class CommandSanitizer:
    @staticmethod
def sanitize_command(command: str) -> list:
        return [arg.strip() for arg in command.split(' ') if arg]

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    sanitized_host = CommandSanitizer.sanitize_command(request.host)
    subprocess.run(['ping'] + [subprocess.quote(arg) for arg in sanitized_host], check=True)
    return {"status": "completed"}