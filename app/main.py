from fastapi import FastAPI
import subprocess
import shlex

class SafeCommand:
    @staticmethod
def safe_run(command: str, *args, **kwargs):
        try:
            args = shlex.split(args[0]) + list(args)[1:] if args else []
            result = subprocess.run(command, args=args, capture_output=True, text=True, check=True, **kwargs)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

def ping(host: str):
    # Safe implementation
    output = SafeCommand.safe_run('ping', host)
    return {"status": "completed", "output": output}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}