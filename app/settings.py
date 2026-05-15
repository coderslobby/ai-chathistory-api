from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    GROQ_API_KEY: str
    language_model: str
    database_url:str
    max_llm_tokens: int
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )
settings = Setting()
