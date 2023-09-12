from db_init.db_connection import db
from Contracts.action import menu_contracts
from Projects.action import menu_projects
from utils import show_menu, select_user, validat_select


#Main menu
def main_menu() -> int:
    title = 'Application "System of Projects and Contracts"'
    menu = {
        '0.': 'Exit',
        '1.': 'Working with contracts',
        '2.': 'Working with projects',
    }
    show_menu(title, **menu)   
    select = select_user()
    
    while validat_select(select, len(menu)):        
        select = select_user()
        
    return select
        

if __name__ == '__main__':
    select = main_menu()
    
    while select:
        commands = {
            'Main_menu': main_menu,
            1: menu_contracts,
            2: menu_projects,
        }
            
        select = commands.get(select)()
    db.close()    
    print('Exiting the program...')
    
    