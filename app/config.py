from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Get the exact folder where this configuration file is located
BASE_DIR = Path(__file__).resolve().parent.parent
class Settings(BaseSettings):
# Field definitions
    database_url: str
    test_database_url: str
    secret_key: str
    algorithim : str
    access_token_expire_minutes: int

    # New way to define configuration in Pydantic V2
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )
    

settings = Settings()