from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Use subprocess.run instead of subprocess.call and validate input
    if host and host.isalnum():
        command = ['ping', shlex.quote(host)]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout  # Return the output to be included in the response
    else:
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    except ValueError as e:
        return {"status": "error", "message": str(e)}