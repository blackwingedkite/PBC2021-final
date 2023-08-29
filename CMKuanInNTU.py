import CMKuan_game
import pygame

def game_loop(gameName):
    game_exit = False
    gameName.display_music()
    
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
            if event.type == pygame.QUIT:
                game_exit = True
        if gameName.get_timer()//40 <= 0:
            game_exit = True
            
        # game flow
        gameName.display_background()
        gameName.display_status()
        gameName.display_event()
        gameName.display_player()
        gameName.check_event()
        gameName.update_timer()
        pygame.display.update()
    gameName.display_ending()

if __name__ == '__main__':
    CMKGame = CMKuan_game.Game()
    # display cover page
    CMKGame.init_screen()
    CMKGame.display_cover()
    pygame.display.update()
    # display game page
    CMKGame.init_screen()
    CMKGame.init_setting()
    game_loop(CMKGame)
