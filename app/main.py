from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run_command(command: str):
        try:
            result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum() or '&&' in host or ';' in host:
        return {"status": "error", "result": "Invalid input"}
    command = f'ping -c 1 {host}'
    result = SafeSubprocess.run_command(command)
    return {"status": "completed", "result": result}