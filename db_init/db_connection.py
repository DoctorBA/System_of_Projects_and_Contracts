import peewee
from dotenv import load_dotenv
import os


load_dotenv('db_init/.env')

db = peewee.PostgresqlDatabase(
                                database=os.getenv('DATABASE_NAME'),
                                user=os.getenv('DATABASE_USER'),
                                password=os.getenv('DATABASE_PASSWORD'),
                                host=os.getenv('DATABASE_HOST'),
                            )