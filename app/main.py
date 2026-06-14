from fastapi import FastAPI
import subprocess
import shlex
from typing import Union

app = FastAPI()

def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(lambda x: x in allowed_chars, host))

async def ping(host: str) -> Union[dict, str]:
    sanitized_host = sanitize_host(host)
    if not validate_input(sanitized_host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', sanitized_host, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

def validate_input(input_value: str) -> bool:
    if not input_value:
        return False
    if any(char in input_value for char in [';', '&', '|', '`']):
        return False
    return True