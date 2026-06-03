from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_argument(arg):
    return ''.join(shlex.quote(c) for c in arg)

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic validation to allow only alphanumeric characters
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(['ping', escape_shell_argument(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}