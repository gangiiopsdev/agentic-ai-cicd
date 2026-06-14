from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run with shell=False and split command arguments safely
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Safely call the safe_ping function
    return {'status': safe_ping(host)}