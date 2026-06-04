from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to prevent injection attacks
        if not host.strip().replace('.', '').isnumeric():
            raise ValueError("Invalid hostname")
        command = shlex.split(f'ping {host}')
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}
    except ValueError as e:
        return {"status": "invalid", "error": str(e)}