from fastapi import FastAPI
cimport shlex

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_parts = [sanitize_host(part) for part in shlex.split(host)]
    command = ' '.join(sanitized_parts)
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}