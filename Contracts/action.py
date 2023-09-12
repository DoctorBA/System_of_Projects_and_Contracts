import peewee
from datetime import date
from db_init.models_tables import Contracts 
from Contracts.utils import serch_contracts, serch_contract
from utils import show_menu, show_documents, status_message, select_user, validat_select, input_fild


#menu Contracts
def menu_contracts() -> str:
    title = 'Working with contracts'
    menu = {
        '0.': 'Back',
        '1.': 'Create a contract',
        '2.': 'Confirm the contract',
        '3.': 'Complete the contract',
        '4.': 'Show contracts',
    }
    show_menu(title, **menu)
    select = select_user()
           
    while validat_select(select, len(menu)):
        select = select_user()
        
    if select:
        commands = {
            1: create_contract,
            2: confirm_contract,
            3: complete_contract,
            4: show_contracts
        }
        commands.get(select)()
        
        return menu_contracts()
        
    return 'Main_menu'     


#Create Contracts
def create_contract() -> None:    
    try:
        show_menu('Create a contract')
        contract_name = input_fild('name contract')
        Contracts.create(contract_name=contract_name)
        status_message('Contract created')
    except peewee.OperationalError:
        status_message('Error. Contract not created')


#Confirm contract
def confirm_contract() -> None:
    status = 'Draft'
    contracts = serch_contracts(status)
    if not contracts:
        status_message(f'{status} contracts not found')
    else:                
        try:
            show_menu('Confirm a contract')
            contract = search_menu_contract(status)
            
            if contract:
                contract.status_contract = 'Active'
                contract.signature_date = date.today()
                contract.save()
                status_message(f'Contract id {contract.contract_id} name {contract.contract_name} status successfully changed to "Active".')
                
        except peewee.OperationalError:        
            status_message('Database connection error')  
       
        
#Complete contract
def complete_contract() -> None:
    status = 'Active'
    contracts = serch_contracts(status)
    if not contracts:
        status_message(f'{status} contracts not found')
    else:        
        try:
            show_menu('Complete a contract')
            contract = search_menu_contract(status)  
            
            if contract:
                contract.status_contract = 'Completed'
                contract.save()
                status_message(f'Contract id {contract.contract_id} name {contract.contract_name} status successfully changed to "Completed".')
        except peewee.OperationalError:        
            status_message('Database connection error')      


#show Contracts   
def show_contracts(status=None) -> None:    
    title = f'List {status if status else "all"} contracts'
    contracts = serch_contracts(status)
    if contracts:
        show_documents(title, *contracts)
    else:
        status_message('Contracts not created')
        
        
#Menu failed search contract
def search_menu_contract(status:str=None) -> peewee.Model:  
        
        contract = serch_contract(status)
        while not contract:
            title = f'Contract {status if status else "all"} not found'
            menu = {
                '0.': f'Return back',
                '1.': f'Continue entering {status if status else "-"}  contract id',
                '2.': f'View list of {status if status else "all"} contracts',
            }              
            show_menu(title, **menu)
            select = select_user()
    
            while validat_select(select, len(menu)):
                select = select_user()
            
            if not select:
                return None
            
            commands = {
                1: serch_contract,
                2: show_contracts, 
            }    
            contract = commands.get(select)(status)

        return contract
    

  
    
     
    

    
