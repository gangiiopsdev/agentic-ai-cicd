from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.')
    return ''.join(char for char in input_str if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        args = ['ping', sanitized_host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': str(e)}

# Preventive Controls:
# 1. Use a whitelist of allowed hosts.
# 2. Limit the use of subprocess to only trusted commands and arguments.