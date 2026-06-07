from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

decorator_options = {
    'summary': "Ping a host",
    'description': "This endpoint pings the specified host and returns the output."
}

@app.get("/ping", **decorator_options)
def ping(host: str):
    try:
        # Validate input to ensure it's a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', *shlex.split(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Secure fix: Use a whitelist for allowed hosts or sanitize the input using other methods.