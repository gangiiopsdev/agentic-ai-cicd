from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Use a safer method to avoid shell injection risks
    generate_ping_command = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = generate_ping_command.communicate()
    if error:
        return {'status': 'error', 'error': error.decode()}
    return {'status': 'completed', 'output': output.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use a safer method to avoid shell injection risks
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}