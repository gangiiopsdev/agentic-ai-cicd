from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_cmd_arg(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('|', ' ') if isinstance(arg, str) else arg

@app.get("/ping")
def ping(host: str):
    safe_host = escape_cmd_arg(host)
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}