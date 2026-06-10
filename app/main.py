from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg: str) -> str:
    return subprocess.list2cmdline([arg])

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', escape_shell_arg(host)])
    return {"status": "completed"}