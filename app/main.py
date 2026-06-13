from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def escape_shell_input(input):
    return subprocess.list2cmdline([input])

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', escape_shell_input(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}