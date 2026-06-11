from fastapi import FastAPI
import subprocess
class SanitizeInput:
    @staticmethod
def clean_input(value):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        return ''.join(filter(lambda x: x in allowed_chars, value)).replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = SanitizeInput.clean_input(host)
    try:
        output = subprocess.check_output(['ping', '-c 1', sanitized_host], universal_newlines=True, timeout=5)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e).replace('\n', '')}
    except Exception as e:
        return {'status': 'error', 'message': str(e).replace('\n', '')}