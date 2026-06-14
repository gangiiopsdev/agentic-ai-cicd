from fastapi import FastAPI
import subprocess
import shlex
def run_command(command, *args):
    return subprocess.run(command, *args, capture_output=True, text=True, check=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use a full path for the executable to avoid partial path issues and validate input
        if host.startswith('192.168.') or host.startswith('10.'):  # Example of input validation
            output = run_command(['/usr/bin/ping', shlex.quote(host)], timeout=5)
            return {"status": "completed", "output": output.stdout}
        else:
            return {"status": "failed", "error": "Invalid host address"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}
    except Exception as e:
        return {"status": "failed", "error": str(e)}