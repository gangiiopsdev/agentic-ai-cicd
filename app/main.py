from fastapi import FastAPI
import subprocess
class SanitizeInput:
    @staticmethod
def clean_input(value):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        return ''.join(filter(lambda x: x in allowed_chars, value))

app = FastAPI()

@app.get('/ping')
def ping(host: str):    
    sanitized_host = SanitizeInput.clean_input(host)
    try:
        # Using subprocess.run with shell=False to mitigate command injection risk
        output = subprocess.run(['ping', sanitized_host], check=True, universal_newlines=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}