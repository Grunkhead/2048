def launch_menu_scene():
    
    for event in pygame.event.get():
                
        # Check if application should be closed.
        if application_closed(event) == True:
            print('APPLICATION CLOSED AT MAIN MENU!')
            exit()

        # GOTO ORANGE screen.
        mainScene()
        
        screen.fill(DARKERBLUE)
        input()

        # Update 
        pygame.display.update()
        input()