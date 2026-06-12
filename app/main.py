from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation using subprocess.Popen with validation
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):  # Basic validation of the hostname
        return {'status': 'error', 'message': 'Invalid host name'}
    args = ['ping', host]
    process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await process.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}

# Use ping with async/await for non-blocking execution