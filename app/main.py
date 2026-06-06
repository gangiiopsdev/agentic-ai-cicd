from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate and sanitize the host input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError("Invalid host")
        args = shlex.split(f"ping {host}")
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
    except ValueError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)