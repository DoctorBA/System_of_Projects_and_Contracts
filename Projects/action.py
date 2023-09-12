import peewee
from db_init.models_tables import Projects, Contracts
from Contracts.action import search_menu_contract
from Projects.utils import serch_projects, validat_documents, serch_project
from utils import show_menu, show_documents, status_message, select_user, validat_select, input_fild


#menu Projects
def menu_projects() -> str:
    title = 'Working with projects'
    menu = {
        '0.': 'Back',
        '1.': 'Create a projects',
        '2.': 'Add contract in project',
        '3.': 'Complete a contract in a project',
        '4.': 'Show projects',
    }
    show_menu(title, **menu)
    select = select_user()
           
    while validat_select(select, len(menu)):
        select = select_user()
        
    if select:
        commands = {
            1: create_project,
            2: add_contract,
            3: complete_projects,
            4: show_projects
        }
        commands.get(select)()
        
        return menu_projects()
        
    return 'Main_menu'  


#create Projects
def create_project() -> None:    
    try:
        show_menu('Create a project')
        project_name = input_fild('name project')               
        Projects.create(project_name=project_name)
        status_message('Project created')   
    except peewee.OperationalError:
        status_message('Database connection Error')


#Add contract
def add_contract() -> None:
    try:
        status = 'Active'
        projects = Projects.select().where(Projects.contract==None)
        active_contracts = Contracts.select().where(Contracts.status_contract==status, Contracts.project_id==None)
        if not active_contracts or not projects:
            status_message(f"{status} contracts or projects not found")
        else:
            show_menu('Menu for adding a contract')          
            contract = search_menu_contract(status)
            
            while validat_documents(contract=contract):
                contract = search_menu_contract(status)
                
            if contract:
                project = search_menu_project(status=status, documents=projects)
                
                while validat_documents(project=project):
                    project = search_menu_project(status=status, documents=projects)
                    
                if project:
                    project.contract = contract
                    project.save()
                    contract.project_id = project.project_id
                    contract.save()     
                    status_message(f'Contract id {contract.contract_id} name: "{contract.contract_name}" added in work project id {project.project_id} name: "{project.project_name}".') 
    except peewee.OperationalError:        
        status_message('Database connection error')
 
 
#Complete a contract in a project
def complete_projects() -> None:
    try:
        status = 'Active'
        show_menu('Menu Complete a contract in a project')
        active_contracts = (
                                Projects.select()
                                .join(Contracts)  
                                .where(Contracts.status_contract==status, Contracts.project_id!=None)
                            )   
        if not active_contracts:
            status_message(f"There are no {status} contracts in the project")
        else:
            project = search_menu_project(status=status, documents=active_contracts)
            
            while validat_documents(project=project, active_contracts=active_contracts):
                status_message(f"The project has no {status} contract")
                project = search_menu_project(status=status, documents=active_contracts)
            
            if project:
                project.contract.status_contract = 'Completed'
                project.contract.save()   
                status_message(f'Contract id {project.contract.contract_id} name: "{project.contract.contract_name}" "Complete" in work project id {project.project_id} name: "{project.project_name}".') 
    except peewee.OperationalError:        
        status_message('Database connection error')
               
        
#show Projects   
def show_projects(documents:peewee.Model=None) -> None:    
    title = 'List projects'
    projects = serch_projects(documents)
    if projects:
        show_documents(title, *projects)
    else:
        status_message('Projects not created')
        
        
#Menu failed search project    
def search_menu_project(status:str=None, documents:peewee.Model=None) -> peewee.Model:  
        
        project = serch_project(documents)
        while not project:
            title = f'Project {status if status else "all"} not found'
            menu = {
                '0.': f'Return back',
                '1.': f'Project entering {status if status else "-"} contract id',
                '2.': f'View list of {status if status else "all"} project',
            }              
            show_menu(title, **menu)
            select = select_user()
    
            while validat_select(select, len(menu)):
                select = select_user()
            
            if not select:
                return None
            
            commands = {
                1: serch_project,
                2: show_projects, 
            }    
            project = commands.get(select)(documents)

        return project  