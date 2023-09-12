import peewee
from db_init.models_tables import Projects, Contracts
from db_init.db_connection import db
from utils import status_message


#autoload Database
def autocomplete_load() -> str:
    try:
        Contracts.create(contract_name='One contract')
        Contracts.create(contract_name='Two contract')
        Contracts.create(contract_name='Three contract')
        Contracts.create(contract_name='Four contract')
        Contracts.create(contract_name='Five contract')
        
        Projects.create(project_name='One project')
        Projects.create(project_name='Two project')
        Projects.create(project_name='Three project')
        Projects.create(project_name='Four project')
        Projects.create(project_name='Five project')
        status_message('Database autocomplete completed successfully')
        db.close()
    except peewee.IntegrityError:        
        status_message('Error! Database disabled or autocomplete has already been completed')


if __name__ == '__main__':
    autocomplete_load()