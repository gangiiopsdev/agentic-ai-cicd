from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'output': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

# Further improvements:
# 1. Use a whitelist of allowed hosts or use DNS resolution to ensure the input is valid.
# 2. Consider using an alternative method for pinging, such as ping3 library which does not require subprocess.