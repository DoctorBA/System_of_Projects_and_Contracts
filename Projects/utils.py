import peewee
from db_init.models_tables import Projects
from utils import status_message, input_fild


#Serch all Projects
def serch_projects(contracts:peewee.Model=None) -> list:
    try:
        if contracts:
            return [v for v in contracts.dicts()]  
            
        projects = Projects.select()            
        return [v for v in projects.dicts()]
    except peewee.OperationalError:        
        status_message('Database connection error')
        
        
#Serch one Project
def serch_project(documents:peewee.Model=None) -> peewee.Model:
    try:
        project_id = int(input_fild(f'project id'))
        project = Projects.select().where(Projects.project_id==project_id)

        if project:
            return project.get()        
               
    except peewee.OperationalError:        
        status_message('Database connection error')
        

#validat Contracts in project
def validat_documents(contract:peewee.Model=None, project:peewee.Model=None, active_contracts:peewee.Model=None) -> bool:
    try:
        
        if project and active_contracts:                    
            return not project in active_contracts
        
        if contract:
            contract = Projects.select().where(Projects.contract==contract)
    
        if contract:
            status_message('The contract is already in development')
            return True
        
        if project:
            project = project.contract
    
        if project:
            status_message('The project is already in development')
            return True
        
    except peewee.OperationalError:        
        status_message('Database connection error')     
                
  