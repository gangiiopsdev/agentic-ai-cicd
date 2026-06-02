from fastapi import FastAPI
import subprocess
def escape_shell_argument(arg):
    return subprocess.list2cmdline([arg])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    result = subprocess.run(['ping', escaped_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}