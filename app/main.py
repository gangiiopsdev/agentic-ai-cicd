from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command_arg(arg):
    return arg.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_command_arg(host)
    try:
        result = subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}