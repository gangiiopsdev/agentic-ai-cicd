from fastapi import FastAPI
import re
import asyncio

app = FastAPI()

async def safe_ping(host: str):
    sanitized_host = ''.join(e for e in host if re.match(r'[a-zA-Z0-9 ]', e))
    try:
        result = await asyncio.create_subprocess_exec('ping', *sanitized_host.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = await result.communicate()
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}