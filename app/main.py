from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    host = escape_shell_argument(host)
    # Safer implementation
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)  # Using subprocess.run instead of subprocess.call
    return {"status": "completed"}