from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_subprocess(command, *args):
        try:
            # Validate and sanitize input
            sanitized_args = [shlex.quote(arg) for arg in args]
            result = subprocess.run([command] + sanitized_args, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input using SafeSubprocess.safe_subprocess
    safe_command = SafeSubprocess.safe_subprocess('ping', host)
    return {"status": "completed", "output": safe_command}