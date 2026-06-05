from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return ' '.join(subprocess.list2cmdline([arg]).split())

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_arg(host)
    result = subprocess.run(f"ping {safe_host}", shell=False, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}