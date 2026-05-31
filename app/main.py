from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input
    if not host.isalnum():
        return "Invalid input"

    try:
        result = subprocess.run(['ping', subprocess.check_output(f'echo {host}', shell=True).decode()], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)