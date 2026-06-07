from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str) -> None:
    try:
        # Validate and sanitize the host input
        if not host.isalnum():
            raise ValueError("Invalid hostname")
        # Use shlex to safely handle command arguments
        args = ['ping', shlex.quote(host)]
        subprocess.run(args, check=True)
    except Exception as e:
        print(f"Error: {e})
        raise

@app.get="/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}