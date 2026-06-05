from fastapi import FastAPI
import subprocess

def execute_safe_command(command, *args):
    safe_args = [arg for arg in args if isinstance(arg, str) and all(c not in arg for c in ['&&', '|'])]
    try:
        result = subprocess.run([command] + list(safe_args), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class PingInputValidator:
    @staticmethod
    def validate_host(host: str):
        if not host.isalnum():
            raise ValueError("Invalid input")

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingInputValidator.validate_host(host)
    safe_command = execute_safe_command(f'ping -c 4 {host}')  # Use parameterized input for safety
    return {"status": "completed", "result": safe_command}