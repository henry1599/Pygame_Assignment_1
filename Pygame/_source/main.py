from symbol import pass_stmt
import pygame as pg
import random
from enum import Enum
from constants import *
from helper import *
import sys
import time
import particlepy
from components import *

class Ball(SpriteRenderer):
    def __init__(self, 
                 screen,
                 image_path : str, 
                 position : tuple = (0, 0), 
                 scale : tuple = (1, 1), 
                 scale_factor : float = 1, 
                 anchor : Anchor = Anchor.TOP_LEFT,
                 start_life_time = 1000,
                 angle_delta_min = 1,
                 angle_delta_max = 4):
        super().__init__(screen, image_path, position, scale, scale_factor, anchor)
        self.clicked = False
        self.start_life_time = start_life_time
        self.vfx_explosion = particlepy.particle.ParticleSystem()
        self.play_particle = False
        self.angle = 0
        self.angle_delta = random.uniform(angle_delta_min, angle_delta_max)
        self.rotate_factor = ROTATE_FACTOR[random.randint(0, 1)]
        self.image_copy = pg.transform.rotate(self.image, self.angle).convert_alpha()
        
    def GatherInput(self, _mouse_pos):
        if self.rect.collidepoint(_mouse_pos):
            self.clicked = True
            self.play_particle = True
    
    def ScaleImage(self, base_scale : tuple, scale_factor : float):
        self.image = pg.transform.scale(self.image, (base_scale[0] * scale_factor, base_scale[1] * scale_factor))
    
    def ApplyGravity(self):
        pass
    
    def PlayerAnimation(self):
        pass
    
    def update(self, _delta_time, _mouse_pos):
        self.GatherInput(_mouse_pos)
        self.start_life_time -= _delta_time
        self.angle += self.angle_delta * self.rotate_factor
        self.image_copy = pg.transform.rotate(self.image, self.angle)
        
    def draw(self):
        self.screen.blit(self.image_copy, (self.position[0] - int(self.image_copy.get_width() / 2), self.position[1] - int(self.image_copy.get_height() / 2)))

class Cursor(SpriteRenderer):
    def __init__(self, 
                 screen,
                 image_path : str, 
                 position : tuple = (0, 0), 
                 scale : tuple = (1, 1), 
                 scale_factor : float = 1, 
                 anchor : Anchor = Anchor.TOP_LEFT):
        super().__init__(screen, image_path, position, scale, scale_factor, anchor)
        pg.mouse.set_visible(0)
        
    def GatherInput(self, _mouse_pos):
        self.rect.topleft = _mouse_pos
    
    def ScaleImage(self, base_scale : tuple, scale_factor : float):
        self.image = pg.transform.scale(self.image, (base_scale[0] * scale_factor, base_scale[1] * scale_factor))
    
    def ApplyGravity(self):
        pass
    
    def PlayerAnimation(self):
        pass
    
    def update(self, _mouse_pos):
        self.GatherInput(_mouse_pos)
        self.draw()

class Grid(SpriteRenderer):
    def __init__(self, 
                 screen,
                 image_path : str, 
                 position : tuple = (0, 0), 
                 scale : tuple = (1, 1), 
                 scale_factor : float = 1, 
                 anchor : Anchor = Anchor.TOP_LEFT,
                 grids_pos = []):
        super().__init__(screen, image_path, position, scale, scale_factor, anchor)
        pg.mouse.set_visible(0)
        self.cells_dict = {
            grids_pos[0] : False,
            grids_pos[1] : False,
            grids_pos[2] : False,
            grids_pos[3] : False,
            grids_pos[4] : False,
            grids_pos[5] : False,
            grids_pos[6] : False,
            grids_pos[7] : False,
        }
        self.grids_pos = grids_pos
        
    def GatherInput(self, _mouse_pos):
        pass
    
    def ScaleImage(self, base_scale : tuple, scale_factor : float):
        self.image = pg.transform.scale(self.image, (base_scale[0] * scale_factor, base_scale[1] * scale_factor))
    
    def ApplyGravity(self):
        pass
    
    def PlayerAnimation(self):
        pass
    
    def update(self):
        self.draw()
    
    def GetEmptySlot(self):
        rand_idx = random.randint(0, 7)
        if not self.cells_dict[self.grids_pos[rand_idx]]:
            return self.grids_pos[rand_idx]
        return (-1, -1)

    def UpdateGrid(self, _pos, _status):
        self.cells_dict.update({_pos : _status})

class ButtonType(Enum):
    START = 0,
    CREDIT = 1,
    QUIT = 2

class ButtonTextRenderer(TextRenderer):
    def __init__(
        self,
        screen,
        font_path, 
        position, 
        string, 
        size, 
        fcolor, 
        anchor,
        is_outline = False,
        ocolor = (255, 255, 255),
        border_radius = 2,
        type = ButtonType.START
    ):
        super().__init__(screen, font_path, position, string, size, fcolor, anchor, is_outline, ocolor, border_radius)
        self.clicked = False
        self.type = type
    
    def GatherInput(self):
        if not self.clicked:
            mouse_presses = pg.mouse.get_pressed()
            if mouse_presses[0]:
                if self.rect.collidepoint(pg.mouse.get_pos()):
                    self.clicked = True
                    if self.type == ButtonType.START:
                        OnStartButtonClick()
                    elif self.type == ButtonType.CREDIT:
                        OnCreditButtonClick()
                    elif self.type == ButtonType.QUIT:
                        OnQuitButtonClick()
                        
        # pass
    
    def update(self):
        super().update()
            
    def draw_text(self):
        super().draw_text()
    
    def draw_text_support(self, font_path, position, string, size, fcolor, anchor, window):
        super().draw_text_support(font_path, position, string, size, fcolor, anchor, window)

    def draw_text_with_outline(self):
        super().draw_text_with_outline()

def OnStartButtonClick():
    Game.Start()

def OnCreditButtonClick():
    DisplayCredit()

def OnQuitButtonClick():
    Game.Exit()

pg.init()

screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption(GAME_NAME)

ground_surface = pg.image.load(BACKGROUND_PATH).convert()
ground_size = GetBackgroundScreenScale(BACKGROUND_WIDTH, BACKGROUND_HEIGHT, True)
ground_surface = pg.transform.scale(ground_surface, ground_size)
ground_position = (0, 0)


ball_spawn_timer = pg.USEREVENT + 1
pg.time.set_timer(ball_spawn_timer, BALL_SPAWN_INTERVAL)
ball_list = []

ball_start_life_time = pg.USEREVENT + 2
pg.time.set_timer(ball_start_life_time, BALL_LIFE_TIME)

current_score = 0
font = pg.font.Font(FONT_PATH, SCORE_TEXT_SIZE)
game_name_font = pg.font.Font(FONT_PATH, GAME_NAME_TEXT_SIZE)
title_font = pg.font.Font(FONT_PATH, TITLE_TEXT_SIZE)

click_the_ball_sound = pg.mixer.Sound(SOUND_CLICK_THE_BALL)
click_the_ball_sound.set_volume(0.5)

click_nothing_sound = pg.mixer.Sound(SOUND_CLICK_NOTHING)
click_nothing_sound.set_volume(0.5)

cursor = Cursor(
    screen,
    CURSOR_PATH,
    position = (0, 0),
    scale = CURSOR_SIZE,
    scale_factor = 0.2,
    anchor = Anchor.TOP_LEFT
)

grid = Grid(
    screen,
    GRID_PATH,
    position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
    scale = GRID_SIZE,
    scale_factor = 1,
    anchor = Anchor.MID_CENTER,
    grids_pos = GRIDS_POS
)

vfx_explosion = particlepy.particle.ParticleSystem()
vfx_particle_explosion = particlepy.particle.ParticleSystem()
vfx_particle_miss = particlepy.particle.ParticleSystem()

def BallSpawner(_ball_list, _delta_time, _mouse_pos):
    global current_score, vfx_explosion, vfx_particle_explosion
    if _ball_list:
        for ball in _ball_list:
            ball.update(_delta_time, _mouse_pos)
            if ball.clicked:
                # add score
                pg.mixer.Sound.play(click_the_ball_sound)
                grid.UpdateGrid(ball.position, False)
                current_score += 1
                _ball_list.remove(ball)
                for _ in range(1):
                    vfx_explosion.emit(
                    particlepy.particle.Particle(shape=particlepy.shape.Circle(radius=150,
                                                                            color=(255, 255, 255, 255),
                                                                            alpha=255),
                                                position = ball.position,
                                                velocity = (0, 0),
                                                delta_radius = 7))
                for _ in range(75):
                    vfx_particle_explosion.emit(
                    particlepy.particle.Particle(shape=particlepy.shape.Circle(radius=random.randint(5, 20),
                                                                            color=BALL_RAW_COLOR[random.randint(0, 1)],
                                                                            alpha=255),
                                                position = ball.position,
                                                velocity = (random.uniform(-250, 250), random.uniform(-250, 250)),
                                                delta_radius = 0.5))
            elif ball.start_life_time <= 0:
                # minus score
                for _ in range(1):
                    vfx_particle_miss.emit(
                    particlepy.particle.Particle(shape=particlepy.shape.Rect(radius=130,
                                                                            color=(255, 70, 70, 255),
                                                                            alpha=255),
                                                position = ball.position,
                                                velocity = (0, 0),
                                                delta_radius = 5))
                grid.UpdateGrid(ball.position, False)
                current_score -= 1
                if current_score <= 0:
                    current_score = 0
                _ball_list.remove(ball)
        for ball in _ball_list:
            ball.draw()
        return _ball_list
    else:
        return []
    
def DisplayScore(_score):
    global current_score
    current_score = _score
    score_surface = font.render(f'{SCORE_TEXT} : {current_score} balls', True, SCORE_TEXT_COLOR)
    score_rect = score_surface.get_rect(topleft = SCORE_POSITION)
    screen.blit(score_surface, score_rect)

ball_intro_list = []

def GetBallsForIntro(num, min_size = 0.1, max_size = 0.3):
    pos_list = []
    for i in range(num):
        pos_list.append((random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT)))        
    for pos in pos_list:
        ball = SpriteRenderer(
            screen = screen,
            image_path = BALL_PATH, 
            position = pos, 
            scale = BALL_SIZE, 
            scale_factor = random.uniform(min_size, max_size), 
            anchor = Anchor.MID_CENTER
        )
        ball_intro_list.append(ball)
        

def DisplayIntro():
    global ball_intro_list
    for ball_intro in ball_intro_list:
        ball_intro.update()
        ball_intro.draw_with_rotation()
    game_name_text = TextRenderer(
        screen,
        FONT_PATH, 
        (SCREEN_WIDTH / 2, 100), 
        GAME_NAME, 
        GAME_NAME_TEXT_SIZE, 
        GAME_NAME_COLOR, 
        Anchor.MID_CENTER,
        True,
        GAME_NAME_COLOR_OUTLINE, 
        4
    )
    start_title = ButtonTextRenderer(
        screen,
        FONT_PATH, 
        (SCREEN_WIDTH / 2, 350), 
        START_TITLE, 
        TITLE_TEXT_SIZE, 
        TITLE_COLOR, 
        Anchor.MID_CENTER,
        True,
        GAME_NAME_COLOR_OUTLINE, 
        2,
        ButtonType.START
    )
    credit_title = ButtonTextRenderer(
        screen,
        FONT_PATH, 
        (SCREEN_WIDTH / 2, 450), 
        CREDIT_TITLE, 
        TITLE_TEXT_SIZE, 
        TITLE_COLOR, 
        Anchor.MID_CENTER,
        True,
        GAME_NAME_COLOR_OUTLINE, 
        2,
        ButtonType.CREDIT
    )
    quit_title = ButtonTextRenderer(
        screen,
        FONT_PATH, 
        (SCREEN_WIDTH / 2, 550), 
        QUIT_TITLE, 
        TITLE_TEXT_SIZE, 
        TITLE_COLOR, 
        Anchor.MID_CENTER,
        True,
        GAME_NAME_COLOR_OUTLINE, 
        2,
        ButtonType.QUIT
    )
    
    game_name_text.update()
    start_title.update()
    credit_title.update()
    quit_title.update()

def DisplayCredit():
    pass

def DisplaySetting():
    pass

class Gameplay():
    def __init__(self):
        # delta time
        self.trail_particle_system = particlepy.particle.ParticleSystem()
        self.click_particle_system = particlepy.particle.ParticleSystem()
        self.is_clicked = False
        self.old_time = time.time()
        self.delta_time = 0
        self.clock = pg.time.Clock()
        self.run = True
        self.mouse_pos = (0, 0)
        self.game_active = False
    
    def Awake(self):
        pg.mixer.music.load(BEGIN_THEME)
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)
    
    def Start(self):
        pg.mixer.music.load(SOUND_THEME)
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)
        self.game_active = True
    
    def Exit(self):
        self.run = False
    
    def Run(self):
        global ball_list, particles, screen, current_score
        GetBallsForIntro(5)
        while self.run:
            self.mouse_pos = (0, 0)
            self.mouse_last_frame = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.Exit()
                if self.game_active:
                    if event.type == ball_spawn_timer:
                        for _ in range(BALL_EACH_TURN):
                            spawn_pos = grid.GetEmptySlot()
                            if spawn_pos == (-1, -1):
                                continue
                            grid.UpdateGrid(spawn_pos, True)
                            ball = Ball(
                                    screen = screen,
                                    image_path = BALL_PATH, 
                                    position = spawn_pos, 
                                    scale = BALL_SIZE, 
                                    scale_factor = 0.25, 
                                    anchor = Anchor.MID_CENTER,
                                    start_life_time = BALL_LIFE_TIME / 1000.0
                                )
                            ball_list.append(ball)
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_presses = pg.mouse.get_pressed()
                    if mouse_presses[0]:
                        pg.mixer.Sound.play(click_nothing_sound)
                        self.is_clicked = True
                        self.mouse_pos = pg.mouse.get_pos()
                        
            
            # update delta time
            now = time.time()
            self.delta_time = now - self.old_time
            self.old_time = now
            
            # must-have particles
            # setup trail particle
            self.trail_particle_system.update(delta_time=self.delta_time)
            self.click_particle_system.update(delta_time=self.delta_time)
            
            current_mouse = pg.mouse.get_pos()
            if current_mouse != self.mouse_last_frame:
                current_mouse = current_mouse[0] + 50, current_mouse[1] + 50
                for _ in range(8):
                    self.trail_particle_system.emit(
                        particlepy.particle.Particle(shape=particlepy.shape.Circle(radius=random.randint(1, 10),
                                                                                color=(255, 255, 255),
                                                                                alpha=255),
                                                    position = current_mouse,
                                                    velocity = (random.uniform(-50, 50), random.uniform(-50, 50)),
                                                    delta_radius = 0.4))
                
                # color manipulation
                for particle in self.trail_particle_system.particles:
                    particle.shape.color = particlepy.math.fade_color(particle=particle,
                                                                    color=(255, 255, 255, 0),
                                                                    progress=particle.inverted_progress)
                # render shapes
                self.trail_particle_system.make_shape()

                # post shape creation manipulation
                for particle in self.trail_particle_system.particles:
                    particle.shape.angle += 5

            
            
            if self.is_clicked:
                for _ in range(1):
                    self.click_particle_system.emit(
                        particlepy.particle.Particle(shape=particlepy.shape.Circle(radius=50,
                                                                                color=(255, 255, 255, 200),
                                                                                alpha=255),
                                                    position = pg.mouse.get_pos(),
                                                    velocity = (0, 0),
                                                    delta_radius = 3))
                self.is_clicked = False
            # click particle color manipulation
            for particle in self.click_particle_system.particles:
                particle.shape.alpha = particlepy.math.fade_alpha(particle=particle,
                                                                alpha = 0,
                                                                progress=particle.inverted_progress)

            # click particle render shapes
            self.click_particle_system.make_shape()

            # click particle post shape creation manipulation
            for particle in self.click_particle_system.particles:
                particle.shape.angle += 5
                
            
            if self.game_active:
                for level in LEVEL_CONFIG:
                    if current_score <= level:
                        BALL_EACH_TURN = LEVEL_CONFIG[level][0] # 1s
                        BALL_LIFE_TIME = LEVEL_CONFIG[level][1]
                        break
                # deltaTime in seconds.
                screen.blit(ground_surface, ground_position)
                ball_list = BallSpawner(ball_list, self.delta_time, self.mouse_pos)
                DisplayScore(current_score)
                cursor.update(pg.mouse.get_pos())
                grid.update()
                
                vfx_explosion.update(delta_time=self.delta_time)
                vfx_particle_explosion.update(delta_time=self.delta_time)
                vfx_particle_miss.update(delta_time=self.delta_time)
                
                for particle in vfx_explosion.particles:
                    particle.shape.alpha = particlepy.math.fade_alpha(particle=particle,
                                                                    alpha = 0,
                                                                    progress=particle.inverted_progress)
                for particle in vfx_particle_explosion.particles:
                    particle.shape.alpha = particlepy.math.fade_alpha(particle=particle,
                                                                    alpha = 0,
                                                                    progress=particle.inverted_progress)
                for particle in vfx_particle_miss.particles:
                    particle.shape.alpha = particlepy.math.fade_alpha(particle=particle,
                                                                    alpha = 0,
                                                                    progress=particle.inverted_progress)

                vfx_explosion.make_shape()
                vfx_particle_explosion.make_shape()
                vfx_particle_miss.make_shape()
                
                for particle in vfx_explosion.particles:
                    particle.shape.angle += 5
                for particle in vfx_particle_explosion.particles:
                    particle.shape.angle += 5
                    
                vfx_explosion.render(surface=screen)
                vfx_particle_explosion.render(surface=screen)
                vfx_particle_miss.render(surface=screen)
                
            else:
                ball_list.clear()
                screen.blit(ground_surface, ground_position)
                DisplayIntro()
                cursor.update(pg.mouse.get_pos())
            
            self.click_particle_system.render(surface=screen)
            # render trail particles
            self.trail_particle_system.render(surface=screen)
                
            pg.display.update()
            self.clock.tick(TARGET_FPS)
            
        pg.quit()


Game = Gameplay()
Game.Awake()
Game.Run()