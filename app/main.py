from fastapi import FastAPI, HTTPException
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Validate input to ensure it does not contain malicious characters.
    if 'ping' in sanitized_host or '&' in sanitized_host or '|' in sanitized_host:
        raise HTTPException(status_code=400, detail="Invalid input detected")

    try:
        args = shlex.split('ping {}'.format(sanitized_host))
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}