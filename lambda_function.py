from application import Exec
def lambda_handler(event, context):
    
    main_instance = Exec()
    #main_instance.load()
    
    return main_instance.execute()
    
