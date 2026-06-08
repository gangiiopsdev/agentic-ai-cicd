from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_input(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '').replace('`', '')

@app.get="/ping")
def ping(host: str):
    safe_host = escape_shell_input(host)
    subprocess.call(f"ping {safe_host}", shell=True)
    return {"status": "completed"}