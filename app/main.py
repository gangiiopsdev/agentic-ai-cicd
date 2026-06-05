from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize and validate input
    if not host.strip() or len(host) > 256 or ' ' in host:
        return {'error': 'Invalid input'}, 400
    
    result = execute_ping(subprocess.list2cmdline([host]))
    return {'status': 'completed', 'result': result}