# app/core/config.py
class RetryConfig:
    MAX_RETRIES: int = 3
    MIN_WAIT_TIME: int = 1 # seconds
    MAX_WAIT_TIME: int = 10  # seconds
    BACKOFF_MULTIPLIER: int = 2

class TimeoutConfig:
    #CONNECT_TIMEOUT: float = 10.0  --> unsupported Validation error with SDK, will use it with HTTPX
    READ_TIMEOUT: float = 12000.0  # LLMs are slow! Min is 10s


retry_config = RetryConfig()
timeout_config = TimeoutConfig()    