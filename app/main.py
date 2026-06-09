from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(command):
    return ' '.join(subprocess.list2cmdline(arg) for arg in command)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call(escape_command(['ping', host]))

    return {"status": "completed"}