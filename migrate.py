import peewee
from db_init.models_tables import Contracts, Projects
from db_init.db_connection import db
from utils import *
 
 
# database init
def db_init() -> None:
    try:             
        Contracts.create_table(safe=True)
        status_message('Database "Contracts" creat successfully.')
        Projects.create_table(safe=True)
        status_message('Database "Projects" creat successfully.')
        db.close()
    except peewee.OperationalError:
        status_message("Database not found. Please, create database.")
   
   
if __name__ == '__main__':
    db_init()
                
    
      