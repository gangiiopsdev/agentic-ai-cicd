from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run_secure_command(command: str):
        args = shlex.split(command)
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Command failed with error: {e.stderr}'

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid hostname")
    output = run_secure_command(f'ping {shlex.quote(host)}')
    return {"status": "completed", "output": output}