from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

def sanitize_input(input_string):
    # Basic sanitization example, real-world use may require more robust validation
    return ''.join(filter(str.isalnum, input_string))

async def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = await asyncio.create_subprocess_exec('ping', sanitized_host, check=True)
        return {'status': 'success'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)