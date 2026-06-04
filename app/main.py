from fastapi import FastAPI
import subprocess
class CommandRunner:
    @staticmethod
def run_command(command):
        try:
            output = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Command failed: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    # Sanitize user input to prevent command injection
    if not all(c.isalnum() or c in ' .-' for c in host):
        return {"status": "error", "message": "Invalid hostname"}
    result = CommandRunner.run_command(command)
    return {"status": "completed", "result": result}