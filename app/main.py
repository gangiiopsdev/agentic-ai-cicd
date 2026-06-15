from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Validate input to ensure it only contains allowed characters
        if not host.isalnum():
            raise ValueError('Invalid host parameter')
        # Use shlex.quote to safely escape the host parameter
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)
    except ValueError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    response = safe_ping(host)
    return {"status": "completed", "response": response}