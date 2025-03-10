from decouple import config

class Settings:
    LLM_MODEL:str = config('LLM_MODEL', default='phi4-mini')
    SYSTEM_PROMPT_FILE:str = config('SYSTEM_PROMPT_FILE')
    DATABASE_URL:str = config('DATABASE_URL')

    def __init__(self):
        self.validate_settings()

    def validate_settings(self):
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL must be set")

settings = Settings()