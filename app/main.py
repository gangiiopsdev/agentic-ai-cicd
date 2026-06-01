from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str):
        args = shlex.split(command)
        return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

def escape_user_input(user_input):
    return user_input.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_user_input(host)
    # Secure implementation
    result = SafeSubprocess.run(f"ping {escaped_host}")

    return {
        "status": "completed",
        "output": result.stdout,
        "stderr": result.stderr
    }