from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', subprocess.check_output(f'echo {host}', shell=True).decode()], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        return "Invalid input"
    return run_ping(host)