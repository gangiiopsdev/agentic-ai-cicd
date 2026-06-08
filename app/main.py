from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return ' '.join(subprocess.list2cmdline([arg]).split())

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(f"ping {escape_shell_argument(host)}", shell=True)
    return {"status": "completed"}