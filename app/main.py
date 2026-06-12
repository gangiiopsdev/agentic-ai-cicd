from fastapi import FastAPI
import subprocess

async def run_ping(host: str):
    safe_host = subprocess.shlex_quote(host)
    try:
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', safe_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, result.args, output, error)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return run_ping(subprocess.shlex_quote(host))