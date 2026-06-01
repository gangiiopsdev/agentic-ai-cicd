from fastapi import FastAPI
import re

def sanitize_input(input_string):
    return ''.join(e for e in input_string if re.match(r'[a-zA-Z0-9 ]', e))

app = FastAPI()

async def safe_ping(host: str):
    host = sanitize_input(host)
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        output, _ = await result.communicate()
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}