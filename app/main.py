from fastapi import FastAPI
import subprocess

async def execute_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        if result.returncode != 0:
            raise Exception(f'Ping failed with error: {stderr.decode()}')
        return {'status': 'completed', 'output': stdout.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    sanitized_host = subprocess.list2cmdline([host])
    return execute_ping(sanitized_host)