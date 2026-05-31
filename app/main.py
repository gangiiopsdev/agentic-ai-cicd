from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

# Preventive controls
1. Validate and sanitize the `host` input to ensure it does not contain malicious characters.
2. Use a whitelist of allowed hosts if possible.
3. Consider using higher-level abstractions for network operations instead of direct OS commands.