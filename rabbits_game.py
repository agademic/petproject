'''
file doc
'''
import pygame

from settings import Settings
from police import Police
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    '''
    start the game and build an screen object
    '''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Rabbits in Tierpark")

    # create a player
    police = Police(ai_settings, screen)
    # create a group to store the bullets
    bullets = Group()
    rabbits = Group()
    # create a familiy of rabbits
    gf.create_fleet(ai_settings, screen, police, rabbits)

    # create stats data
    stats = GameStats(ai_settings)

    # start the inicial loop of the game
    while True:
        gf.check_events(ai_settings, screen, police, bullets)
        if stats.game_active:
            police.update()
            gf.update_bullets(rabbits, bullets)
            gf.update_rabbits(ai_settings, stats, screen, police,
                              rabbits, bullets)
        gf.update_screen(ai_settings, screen, police, rabbits,
                         bullets)


run_game()
