from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_command(input_string):
    return input_string.replace(';', '').replace('&', '').replace('&&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    safe_host = escape_shell_command(host)
    subprocess.call(f"ping {safe_host}", shell=False)
    return {"status": "completed"}