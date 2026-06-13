from fastapi import FastAPI
import shlex

class ShellCommand:
    @staticmethod
def build_safe_command(command: str, arg: str):
        return f'{command} {shlex.quote(arg)}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure the host input is sanitized to prevent shell injection
    safe_command = ShellCommand.build_safe_command('ping', host)
    return {"safe_command": safe_command}