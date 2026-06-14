from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_command(host):
    try:
        # Use subprocess.run instead of subprocess.call for better security and control over arguments.
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return run_safe_command(host)