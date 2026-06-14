from fastapi import FastAPI
import subprocess
import re

class Sanitizer:
    @staticmethod
def sanitize_input(input_str):
        return re.sub(r'[^a-zA-Z0-9.-]', '', input_str)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', Sanitizer.sanitize_input(host)], check=True, shell=False)
    return {'status': 'completed'}