from fastapi import FastAPI
import subprocess
import shlex

class CommandExecutor:
    @staticmethod
def safe_run(command: str, *args):
        try:
            command_parts = shlex.split(command)
            result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return str(e.stderr.strip())

app = FastAPI()

@app.get("/" )
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.strip() or not all(c.isalnum() for c in host):
        return {"status": "error", "output": "Invalid input"}
    command = f'ping {host}'
    output = CommandExecutor.safe_run(command)
    return {"status": "completed", "output": output}