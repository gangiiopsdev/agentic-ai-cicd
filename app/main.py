from fastapi import FastAPI
import re
import shlex

class SanitizeFilter:
    @staticmethod
def sanitize_input(input_string):
        if input_string is None:
            return ''
        # Regex pattern to allow only alphanumeric and specific characters
        allowed_chars = re.compile(r'^[a-zA-Z0-9.-_!@#$%^&*()+=[]{}|;:,.<>?/`]*$')
        return ''.join(allowed_chars.findall(input_string))

app = FastAPI()

class PingController:
    @staticmethod
def ping(host: str):
        sanitized_host = SanitizeFilter.sanitize_input(host)
        if not sanitized_host:
            raise ValueError('Invalid input')
        subprocess.run(shlex.split(f'ping {shlex.quote(sanitized_host)}'), check=True, capture_output=True, text=True)
        return {'status': 'completed'}