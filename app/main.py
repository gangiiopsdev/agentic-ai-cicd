from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(shlex.split(f'ping {sanitized_host}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
# Additional security measures:
# - Validate host input more strictly (e.g., whitelist of allowed domains).
# - Use a safer command or library if possible.
# - Limit the duration and resources available to the subprocess.