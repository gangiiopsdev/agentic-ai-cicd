from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def escape_input(user_input):
    # More robust escaping using regex to allow only alphanumeric characters and basic punctuation.
    return re.sub(r'[^a-zA-Z0-9]+', '_', user_input)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_input(host)
    try:
        subprocess.run(shlex.split(f'ping {escaped_host}'), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}