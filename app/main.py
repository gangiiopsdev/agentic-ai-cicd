from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not all(char.isalnum() or char in '-.' for char in host):
        raise ValueError('Invalid host')
    command = ['ping', host]
    result = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    return output.decode(), error.decode()

@app.get("/ping")
def ping(host: str):
    try:
        output, error = safe_ping(host)
        if error:
            return {'error': error}
        else:
            return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'error': str(e)}