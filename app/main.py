from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    # Simple sanitization using regular expression to allow only alphanumeric characters and periods
    import re
    sanitized = re.sub(r'[^a-zA-Z0-9.]+', '', input_str)
    return sanitized

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        host = sanitize_input(host)
        args = shlex.split('ping') + [host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}