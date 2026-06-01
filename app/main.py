from fastapi import FastAPI
import subprocess
import shlex
class SafeCommandRunner:
    @staticmethod
def safe_run(command_parts):
        safe_command = ' '.join(shlex.quote(part) for part in command_parts)
        try:
            result = subprocess.run(safe_command, shell=True, check=True, stdout=subprocess.PIPE)
            return {"status": "completed", "output": result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command_parts = ['ping', host]
    return SafeCommandRunner.safe_run(command_parts)