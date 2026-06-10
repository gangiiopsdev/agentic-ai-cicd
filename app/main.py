from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Use subprocess.Popen instead of subprocess.call for safer execution
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Use the safe_ping function to avoid command injection
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}