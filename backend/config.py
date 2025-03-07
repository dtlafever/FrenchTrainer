from decouple import config

class Settings:
    LLM_MODEL:str = config('LLM_MODEL', default='phi4-mini')
    SYSTEM_PROMPT_FILE:str = config('SYSTEM_PROMPT_FILE')
    DATABASE_URL:str = config('DATABASE_URL')

settings = Settings()