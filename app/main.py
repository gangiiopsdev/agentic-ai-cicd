from fastapi import FastAPI
import subprocess
import shlex

class SafePopen:
    @staticmethod
def popen(command, *args, **kwargs):
        return subprocess.Popen(shlex.split(command), *args, **kwargs)

app = FastAPI()

def sanitize_input(user_input):
    # Implement proper input sanitization here
    return user_input.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    SafePopen.popen(f"ping {sanitized_host}")
    return {"status": "completed"}