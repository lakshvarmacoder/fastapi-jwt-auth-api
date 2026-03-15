import os
from dotenv import load_dotenv

load_dotenv()

# JWT Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "eFuABlUoMQfrp1qkWi5oVyh13LPYOjVvx0vIUpPXb-k")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:root@localhost/db")
