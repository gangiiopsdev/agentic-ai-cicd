from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', host]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate or sanitize input to prevent injection
    if not all(c.isalnum() or c in '.-:' for c in host):  # Example validation
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(generate_ping_command(host), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}