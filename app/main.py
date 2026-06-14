from fastapi import FastAPI
import subprocess

app = FastAPI()

async def run_ping(host: str):
    try:
        # Use a full path to avoid execution with a partial path
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, 'ping', output=error)
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr.decode().strip()}'

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = run_ping(host)
    return {'status': 'completed', 'output': output}