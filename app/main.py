from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Implement proper input sanitization here
    return ''.join(filter(str.isalnum, input_string))

app = FastAPI()

async def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = await asyncio.create_subprocess_exec('ping', sanitized_host, stdout=subprocess.PIPE)
        output, _ = await result.communicate()
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)