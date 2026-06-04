from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.strip() or ' ' in host:
        return {"error": "Invalid input"}, 400
    # Use shlex.quote to escape special characters
    from shlex import quote as cmd_quote
    subprocess.call(["ping", cmd_quote(host)], shell=False)
    return {"status": "completed"}