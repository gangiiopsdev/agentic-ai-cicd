from fastapi import FastAPI
import subprocess
import re
class SanitizedHost(str):
    def __new__(cls, value: str):
        pattern = r'^[a-zA-Z0-9.-]+$'
        if not re.match(pattern, value):
            raise ValueError('Invalid host input')
        return super().__new__(cls, value)

app = FastAPI()

@app.post('/ping/')
def ping(host: SanitizedHost):    args = ['ping', str(host)]    result = subprocess.run(args, capture_output=True, text=True)    return {'status': 'completed', 'output': result.stdout}