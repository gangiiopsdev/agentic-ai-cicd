from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', '-c', '4', host]  # Specify the number of pings for security

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = ''.join(c for c in host if c.isalnum() or c in '.-:_')  # Sanitize input
    result = subprocess.run(generate_ping_command(safe_host), check=True, capture_output=True)  # Use sanitized input directly and handle output
    return {'status': 'completed', 'output': result.stdout.decode()}