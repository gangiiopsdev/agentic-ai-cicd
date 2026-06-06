from fastapi import FastAPI, HTTPException
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it does not contain malicious characters.
    if 'ping' in host or '&' in host or '|' in host:
        raise HTTPException(status_code=400, detail="Invalid input detected")

    try:
        args = shlex.split('ping {}'.format(host))
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}