from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic host validation (e.g., allow only alphanumeric characters and periods)
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

@app.get="/ping")
def ping(host: str):
    if validate_host(host):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": output.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Invalid host provided"}