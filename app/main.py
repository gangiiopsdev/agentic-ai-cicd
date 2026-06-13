from fastapi import FastAPI
import subprocess
cimport subprocess as sp

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = sp.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive Controls
# 1. Validate and sanitize input to ensure it does not contain malicious commands.
# 2. Use parameterized queries if applicable.
# 3. Consider using a whitelist of allowed hosts or IPs.