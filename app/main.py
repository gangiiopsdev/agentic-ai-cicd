from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.isalnum() or len(host) > 255:
            raise ValueError("Invalid host")
        cmd = ['ping', shlex.quote(host)]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)