import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE,SHIELD_TYPE, HAMMER_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, DUCKING_HAMMER, RUNNING_HAMMER,JUMPING_HAMMER

X_POS = 80
Y_POS = 325
JUMP_VEL = 8.5

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE:DUCKING_SHIELD,HAMMER_TYPE: DUCKING_HAMMER }
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE:JUMPING_SHIELD,HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE:RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
Y_POS_DUCK = 335

class Dinosaur:
    
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.has_power_up = False

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index//5]
        self.ajuste()
        if self.type == SHIELD_TYPE:
            self.dino_rect.y = Y_POS - 40
        else:
            self.dino_rect.y = Y_POS
        self.step_index += 1

        if self.step_index >=10:
            self.step_index = 0

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.ajuste()
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y =  Y_POS
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.dino_duck = False
        self.image = DUCK_IMG[self.type][self.step_index//5]
        if self.type == DEFAULT_TYPE:
            self.image = pygame.transform.scale(self.image, (14*3,19*3))
        elif self.type == SHIELD_TYPE:
            self.image = pygame.transform.scale(self.image,(34*2,32*3.5))
        elif self.type == HAMMER_TYPE:
            self.image = pygame.transform.scale(self.image,(34*2,32*2))
        
        self.dino_rect = self.image.get_rect()
        if self.type == SHIELD_TYPE:
            self.dino_rect.y = Y_POS_DUCK - 50
        else:
            self.dino_rect.y = Y_POS_DUCK

        self.dino_rect.x = X_POS
        self.step_index += 1

        if self.step_index >=10:
            self.step_index = 0
        
    def ajuste(self):
        if self.type == DEFAULT_TYPE:
            self.image = pygame.transform.scale(self.image, (14*3,20*3.5))
        elif self.type == SHIELD_TYPE:
            self.image = pygame.transform.scale(self.image,(34*2,32*3.5))
        elif self.type == HAMMER_TYPE:
            self.image = pygame.transform.scale(self.image,(34*2,32*2))
    def update(self, user_input):
        if (user_input[pygame.K_UP] or user_input[pygame.K_w]) and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        
        elif user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.dino_duck = True 
            self.dino_run = False
        
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True

        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        
    

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))