from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_input(value: str) -> str:
    return value.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_input(shlex.quote(host))
    try:
        result = subprocess.run(['ping', '-c 1', safe_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": e.stderr}