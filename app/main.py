from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run
    command = ['ping', host]
    for arg in command:
        if not isinstance(arg, str) or not arg.isalnum():
            raise ValueError('Invalid argument provided')
    result = subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode()}

# Additional recommendation: Use a whitelist for allowed hostnames to further mitigate risks.