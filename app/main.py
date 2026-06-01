from fastapi import FastAPI
import subprocess
def escape_shell_argument(value):
    return subprocess.list2cmdline([value])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    subprocess.run(['ping', escape_shell_argument(host)], capture_output=True, text=True)
    return {"status": "completed"}