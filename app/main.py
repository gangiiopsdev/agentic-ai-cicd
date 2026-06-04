from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    return ''.join(filter(lambda x: x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-', user_input))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    subprocess.call(shlex.split(f"ping {host}"), shell=False)
    return {"status": "completed"}