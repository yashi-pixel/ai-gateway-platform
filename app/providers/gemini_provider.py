from google.genai import Client
from google.genai.errors import ServerError
from app.core.settings import settings
from app.core.time_config import timeout_config, retry_config
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from loguru import logger

class Geminiprovider:
    def __init__(self):
        self.client = Client(api_key=settings.GEMINI_API_KEY, http_options={
                "timeout": timeout_config.READ_TIMEOUT,  #custom timout instead of SDK default of 10s
                #"connect_timeout": timeout_config.CONNECT_TIMEOUT,
            })
        self.model = settings.GEMINI_MODEL
        
    def log_retry(retry_state):
        logger.warning(
            f"Attempt {retry_state.attempt_number} failed. "
            f"Retrying..."
    )
    @retry(
            stop=stop_after_attempt(retry_config.MAX_RETRIES),
            wait=wait_exponential(
                multiplier=retry_config.BACKOFF_MULTIPLIER,
                min=retry_config.MIN_WAIT_TIME, 
                max=retry_config.MAX_WAIT_TIME
                ),
            retry=retry_if_exception_type(ServerError),
            before_sleep=log_retry,
            reraise=True
    )
              
    def generate(self, prompt: str):
               response = self.client.models.generate_content(model=self.model, contents=prompt)
               return response.text
             
            