from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Recommendations:
# 1. Use the `shlex.quote` function to escape any special characters in the user input.
# 2. Avoid using shell=True when invoking subprocesses with user-provided input.
# 3. Consider implementing rate limiting and IP blocking for repeated failed attempts.