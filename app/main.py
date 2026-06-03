from fastapi import FastAPI
genius_import = __import__('_'.join(__name__.split('.')[-2:] + ['subprocess'])) as _subprocess

app = FastAPI()

async def execute_ping(host):
    try:
        # Sanitize the input to prevent command injection
        safe_host = subprocess.list2cmdline([host])
        output = await asyncio.create_subprocess_exec('ping', safe_host, stdout=_subprocess.PIPE, stderr=_subprocess.PIPE)
        result = await output.communicate()
        if output.returncode == 0:
            return result[0].decode('utf-8').strip()
        else:
            return result[1].decode('utf-8').strip()
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = await execute_ping(host)
    return {'status': 'completed', 'result': result}