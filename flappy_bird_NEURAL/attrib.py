from math import floor
import pygame
from numpy import array, random, reshape
from genetic import Population


def do_overlap(rect1, rect2):
    l1, r1 = rect1.topleft, rect1.bottomright
    l2, r2 = rect2.topleft, rect2.bottomright
    if r1[0] < l2[0] or r2[0] < l1[0]:
        return False
    if r2[1] < l1[1] or r1[1] < l2[1]:
        return False
    return True

class Color:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 153, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)

class Game:
    WIDTH = 640
    HEIGHT = 480
    FRAME_RATE = 1200
    FRAMES = 0
    TITLE = 'Flappy bird'
    EXIT = False
    GAME_OVER = False
    ICON_PATH = 'res/icon.jpg'
    MANUAL = False

    def initialize():
        pygame.init()
        icon = pygame.image.load(Game.ICON_PATH)
        pygame.display.set_icon(icon)
        pygame.display.set_caption(Game.TITLE)
        screen = pygame.display.set_mode(Game.get_dimensions())
        feature_limits = array([Game.HEIGHT, 100, Game.HEIGHT, Game.HEIGHT, Game.WIDTH])
        Game.feature_limits = reshape(feature_limits, (1,-1))
        clock = pygame.time.Clock()
        population = Population(pop_size=30, feature_limits=Game.feature_limits)
        pipes = []
        background_image = pygame.image.load('res/background.png').convert()
        return screen, clock, population, pipes, background_image

    def reset():
        Game.FRAMES = 0
        pipes = []
        return pipes

    def check_for_collision(population, pipes):
        for pipe in pipes:
            upper_rect, lower_rect = pipe.get_pipe_rects()
            for individual in population.individuals:
                if not individual.bird.game_over:
                    bird_rect = individual.bird.get_rect()
                    touch_pipes = do_overlap(bird_rect, upper_rect) or do_overlap(bird_rect, lower_rect)
                    if touch_pipes:
                        individual.bird.game_over = True

        for individual in population.individuals:
            bird = individual.bird
            if not bird.game_over and (bird.posy < 0 or bird.posy+bird.height > Game.HEIGHT):
                bird.game_over = True

    def update_scores(population):
        for individual in population.individuals:
            bird = individual.bird
            if not bird.game_over:
                individual.bird.score = Game.FRAMES

    def update_objects(population, pipes):
        pipes = Pipe.move_pipes(pipes)
        for individual in population.individuals:
            if not individual.bird.game_over:
                individual.bird.update()
        population.update(Pipe.get_nearest_pipe(population.individuals[0].bird, pipes))
        Game.check_for_collision(population, pipes)
        Game.update_scores(population)

    def get_dimensions():
        return (Game.WIDTH, Game.HEIGHT)

    def draw_screen(screen, population, pipes, background_image):
        Game.FRAMES += 1
        screen.blit(background_image, (0, 0))
        for individual in population.individuals:
            bird = individual.bird
            if not bird.game_over:
                screen.blit(bird.image, (bird.posx, bird.posy))
        for pipe in pipes:
            upper_rect, lower_rect = pipe.get_pipe_rects()
            pygame.draw.rect(screen, Color.DARK_GREEN, upper_rect)
            pygame.draw.rect(screen, Color.DARK_GREEN, lower_rect)
        pygame.display.update()

    def loop(screen, clock, population, pipes, background_image):
        while not Game.EXIT:
            Game.update_objects(population, pipes)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game.EXIT = True
                elif event.type == pygame.KEYDOWN and Game.MANUAL:
                    if event.key == pygame.K_UP:
                        population.individuals[0].bird.fly()
            if Game.are_all_birds_dead(population):
                population.evolve()
                population.reset_individuals_to_inital_state()
                pipes = Game.reset()
            Game.draw_screen(screen, population, pipes, background_image)
            clock.tick(Game.FRAME_RATE)

    def are_all_birds_dead(population):
        for individual in population.individuals:
            if not individual.bird.game_over:
                return False
        return True

class Bird:
    ANIMATION_RATE = 5

    def __init__(self):
        self.posx = 0
        self.posy = int(Game.HEIGHT/2)
        filename = 'res/bird.png'
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(Color.BLACK)
        rect = self.image.get_rect()
        self.width, self.height = rect.width, rect.height
        self.velocity = 0
        self.gravity = 0.08
        self.color = (
            random.randint(256),
            random.randint(256),
            random.randint(256),
        )
        self.score = 0
        self.game_over = False
        self.last_update = 0

    def get_center(self):
        x = self.posx + self.radius
        y = self.posy + self.radius
        return (x, y)

    def update(self):
        t = Game.FRAMES - self.last_update
        if t > Bird.ANIMATION_RATE:
            u = self.velocity
            a = self.gravity
            s = self.posy
            self.posy += floor((u*t) + (0.5*(a*t*t)))
            self.velocity = u + a*t
            self.last_update = Game.FRAMES

    def fly(self):
        self.velocity = -3

    def get_rect(self):
        return pygame.rect.Rect(self.posx, self.posy, self.width, self.height)

class Pipe:
    gap_width = 175
    width = 40
    space_between_pipes = 350
    stepx = 5
    ANIMATION_RATE = 5

    def __init__(self):
        self.gap_start = random.randint(0, high=Game.HEIGHT - Pipe.gap_width)
        self.gap_end = self.gap_start + Pipe.gap_width
        self.posx = Game.WIDTH
        self.last_update = 0

    def update(self):
        t = Game.FRAMES - self.last_update
        if t > Pipe.ANIMATION_RATE:
            self.posx -= Pipe.stepx
            self.last_update = Game.FRAMES

    def get_pipe_rects(self):
        pipe_position = (self.posx, 0)
        pipe_dimensions = (self.width, self.gap_start)
        upper_rect = pygame.Rect(pipe_position, pipe_dimensions)
        pipe_position = (self.posx, self.gap_end)
        pipe_dimensions = (self.width, Game.HEIGHT - self.gap_end)
        lower_rect = pygame.Rect(pipe_position, pipe_dimensions)
        return upper_rect, lower_rect

    def move_pipes(pipes):
        if len(pipes) > 0:
            last_pipe = pipes[-1]
            if last_pipe.posx + Pipe.width + Pipe.space_between_pipes < Game.WIDTH:
                pipes.append(Pipe())
            first_pipe = pipes[0]
            if first_pipe.posx + Pipe.width < 0:
                del pipes[0]
        else:
            pipes.append(Pipe())
        for pipe in pipes:
            pipe.update()
        return pipes

    def get_nearest_pipe(bird, pipes):
        for pipe in pipes:
            if bird.posx < pipe.posx + pipe.width:
                return pipe
