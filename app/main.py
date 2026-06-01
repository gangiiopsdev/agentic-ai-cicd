from fastapi import FastAPI
import subprocess
def escape_command(args):
    return [shlex.quote(arg) for arg in args]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_args = escape_command(["ping", host])
    subprocess.run(escaped_args, check=True)
    return {"status": "completed"}