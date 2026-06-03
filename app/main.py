from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

# Preventive controls
- Validate and sanitize input to ensure it does not contain malicious code.
- Use whitelisting for command arguments.
- Consider using a safer library or method if possible.