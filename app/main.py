from fastapi import FastAPI
import subprocess
import shlex
class SanitizedSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        # Use a whitelist of allowed commands and arguments
        if not any(cmd in command for cmd in ['ping', 'traceroute']):
            raise ValueError('Only ping and traceroute commands are allowed')
        sanitized_command = shlex.split(command)
        return subprocess.run(sanitized_command, check=True, capture_output=True, text=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = SanitizedSubprocess.run(f'ping -c 1 {host}')
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}