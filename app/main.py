from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_input(user_input):
    return ' '.join(subprocess.list2cmdline([x]) for x in user_input.split())

@app.get="/ping")
def ping(host: str):
    escaped_host = escape_input(host)
    # Safe implementation
    subprocess.call(f"ping {escaped_host}")
    return {status": "completed"}