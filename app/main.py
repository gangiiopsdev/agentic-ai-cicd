from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_input(user_input):
    return user_input.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    safe_host = escape_shell_input(host)
    subprocess.call(f"ping {safe_host}", shell=True)
    return {"status": "completed"}