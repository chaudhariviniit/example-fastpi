from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname : str
    database_port : str
    database_username : str
    database_password : str
    database_name : str
    secret_key : str
    algorithm : str
    access_token_expire_minutes : int

    class Config:
        env_file = ".env"

settings = Settings()        

# import os 
# from dotenv import load_dotenv

# load_dotenv()

# class Settiings:

#     database_hostname : str = os.getenv("DATABASE_HOSTNAME")
#     database_port : str = os.getenv("DATABASE_PORT") 
#     database_username : str = os.getenv("DATABASE_USERNAME")
#     database_password : str = os.getenv("DATABASE_PASSWORD")
#     database_name : str = os.getenv("DATABASE_NAME")
#     secret_key : str  = os.getenv(" SECRET_KEY")
#     algorithm : str = os.getenv("ALGORITHM")
#     access_token_expire_minutes : str = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

# settings = Settiings()