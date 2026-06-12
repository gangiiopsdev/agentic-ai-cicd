from fastapi import FastAPI
import re
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return shlex.quote(input_str)

@app.get('/ping')
def ping(host: str):
    # Validate input to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host'}, 400
    args = ['ping', sanitize_input(host)]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}