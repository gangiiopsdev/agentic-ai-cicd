from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host input does not contain malicious commands
    if any(char in host for char in [';', '&', '|', '$', '*', '?', '<', '>', '^']):
        raise ValueError("Invalid characters in host")

@app.get="/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', safe_ping(host)], check=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}