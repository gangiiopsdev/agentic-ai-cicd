from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_command(user_input):
    return [quote(part.strip()) for part in user_input.split(' ')] if ' ' in user_input else [quote(user_input)]

@app.get("/ping")
def ping(host: str):
    subprocess.run(escape_command(host), check=True)
    return {"status": "completed"}