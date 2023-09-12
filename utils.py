#visual menu
def show_menu(title: str, **menu: dict) -> None:
    print(('---').center(len(title)))
    print(f'| {title} |')
    print(('---').center(len(title)))
    
    if menu:
        print('Menu:')
        for k, v in menu.items():
            print(f'     {k} {v}')        
        print('_'*5)   
        
        
#visual Documents
def show_documents(title: str, *filds: list) -> None:
    print(('---').center(len(title)))
    print(f'| {title} |')
    print(('---').center(len(title)))
   
    print(*[str(value).center(len(value)) for value in filds[0].keys()], sep=' | ')
    for dict in filds:
        print(*[str(value).center(len(key)) for key, value in dict.items()], sep=' | ')
        
    input('\nClick to continue...')

  
#status message    
def status_message(title:str) -> None:      
    print(('---').center(len(title)))
    print(f'| {title} |')
    print(('---').center(len(title)))
    input('\nClick to continue...')
     
     
#validat select
def validat_select(select: str, max_num:int=None) -> bool:
    
    if select not in range(max_num):
        show_menu('Invalid command')
        return True
    
    return False
   
   
#Select user
def select_user() -> int:
    select = input('Select: ')
    
    while not select.isdigit():
        print('Incorrect input. Please, try again')
        select = input('Select: ')
        
    return int(select)


#Field Validation
def input_fild(fild: str) -> str:
    select = input(f'Enter {fild}: ')
    
    while not select:
        print('Field cannot be empty. Please, try again')
        select = input(f'Enter {fild}: ')
        
    return select