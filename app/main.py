from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = run_ping(host)
    return {'status': 'completed', 'output': output}

# Recommendations:
# 1. Use a fully qualified executable path for better security.
# 2. Consider using a whitelist of allowed hosts instead of arbitrary input.