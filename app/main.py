from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Secure implementation using safe libraries like ping3
    try:
        result = ping3.ping(host)
        if result is not None:
            return {'status': 'completed', 'output': f'Response time: {result} seconds'}
        else:
            return {'status': 'failed', 'output': 'No response'}
    except Exception as e:
        return {'status': 'failed', 'output': str(e)}

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)