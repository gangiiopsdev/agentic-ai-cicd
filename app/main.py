from fastapi import FastAPI
import re
class SanitizedHost(str):
    def __new__(cls, value: str):
        pattern = r'^[a-zA-Z0-9.-]+$'
        if not re.match(pattern, value):
            raise ValueError('Invalid host input')
        return super().__new__(cls, value)

app = FastAPI()

@app.post('/ping/')
def ping(host: SanitizedHost):    args = ['ping', str(host)]    result = subprocess.run(args, capture_output=True, text=True, check=True)  # Use check=True to raise an exception on error    return {'status': 'completed', 'output': result.stdout}