from fastapi import FastAPI
import shlex
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))
app = FastAPI()
@app.get("/ping")
def ping(host: str):    sanitized_host = sanitize_input(host)    try:
        result = subprocess.run(shlex.split(f"ping {sanitized_host}"), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}