from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Constructing the ping command safely
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

@app.get("/ping")
def ping(host: str):
    # Using the safe_ping function to avoid command injection
    return {'status': 'completed', 'output': safe_ping(host)}