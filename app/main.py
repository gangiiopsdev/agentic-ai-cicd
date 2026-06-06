from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in '.-')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        if sanitized_host and '@' not in sanitized_host and '<>' not in sanitized_host and '&' not in sanitized_host and '|' not in sanitized_host:
            subprocess.call(['ping', sanitized_host], shell=False)
        else:
            return {'status': 'failed', 'error': 'Invalid input'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}