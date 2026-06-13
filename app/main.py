from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive controls:
# 1. Validate the input to ensure it does not contain malicious content.
# 2. Use a whitelist of allowed host values.
# 3. Consider using a more secure method for executing external commands, such as using a dedicated library or service designed for this purpose.