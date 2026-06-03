from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_call(command: str, *args, **kwargs):
        # Use shlex.split to safely split the command string into a list of arguments
        args_list = shlex.split(command)
        return subprocess.run(args_list, check=True, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid input")
    command = f'ping -c 1 {host}'  # Limit the number of pings to avoid denial of service
    result = SafeSubprocess.safe_call(command)
    return {"status": "completed", "result": result}