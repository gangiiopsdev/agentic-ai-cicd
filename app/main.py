from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() and e.isdigit())
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', shlex.quote(sanitized_host)]  # Use shlex.quote to escape special characters
    subprocess.run(command, check=True)  # Use subprocess.run instead of subprocess.call for better error handling and more secure execution
    return {"status": "completed"}