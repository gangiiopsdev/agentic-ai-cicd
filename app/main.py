from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        args = ['ping', host]
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive controls:
# 1. Validate and sanitize user input to ensure it does not contain malicious commands.
# 2. Use the `shlex` module to safely parse shell strings if necessary.
# 3. Consider using a safer alternative to subprocess for tasks that do not require direct system command execution.