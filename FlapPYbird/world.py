import pygame, random
from charakters import Bird, Plane, Mexbird
from obstacles import Pipe,Building, Burrito
from game import GameIndicator
from settings import WIDTH, HEIGHT, obstacleGap, obstacleSize, obstacle_pair_sizes, import_sprite


class World:
    def __init__(self, screen, current_theme="bird"):
        self.screen = screen
        self.current_theme = current_theme  # Store the current theme
        self.worldShift = 0
        self.current_x = 0
        self.gravity = 0.5
        self.currentObstacle = None
        self.obstacles = pygame.sprite.Group()  # Renamed to obstacles
        self.player = pygame.sprite.GroupSingle()
        self._generate_world()
        self.playing = False
        self.gameOver = False
        self.passed = True
        self.game = GameIndicator(screen)
        self.gameOverImg = pygame.image.load("assets/terrain/gameover.png")
        self.gameOverImg = pygame.transform.scale(self.gameOverImg, (400, 100))

        explosion_images = import_sprite("assets/terrain/explosion")
        burrito_explosion_images = import_sprite("assets/terrain/burrito_explosion")
        self.burrito_explosion_images = [pygame.transform.scale(image, (100, 100)) for image in burrito_explosion_images]

        self.explosion_images = [pygame.transform.scale(image, (100, 100)) for image in explosion_images]
        self.explosion_index = 0
        self.explosion_delay = 100 # Adjust as needed
        self.explosion_triggered = False



    def _add_obstacle(self):
        print(self.current_theme)
        if self.current_theme == "bird":
            # Add bird obstacles (pipes)
            pipe_pair_size = random.choice(obstacle_pair_sizes)
            topPipeHeight, bottomPipeHeight = pipe_pair_size[0] * obstacleSize, pipe_pair_size[1] * obstacleSize
            pipeTop = Pipe((WIDTH, 0 - (bottomPipeHeight + obstacleGap)), obstacleSize, HEIGHT, True)
            pipeBottom = Pipe((WIDTH, topPipeHeight + obstacleGap), obstacleSize, HEIGHT, False)
            self.obstacles.add(pipeTop)
            self.obstacles.add(pipeBottom)
            self.currentObstacle = pipeTop
        if self.current_theme == "mexbird":
            # Add bird obstacles (burritos)
            mexpipe_pair_size = random.choice(obstacle_pair_sizes)
            topPipeHeight, bottomPipeHeight = mexpipe_pair_size[0] * obstacleSize, mexpipe_pair_size[1] * obstacleSize
            pipeTop = Burrito((WIDTH, 0 - (bottomPipeHeight + obstacleGap)), obstacleSize, HEIGHT, True)
            pipeBottom = Burrito((WIDTH, topPipeHeight + obstacleGap), obstacleSize, HEIGHT, False)
            self.obstacles.add(pipeTop)
            self.obstacles.add(pipeBottom)
            self.currentObstacle = pipeTop
        elif self.current_theme == "plane":
            # Add plane obstacles (buildings)
            building_pair_size = random.choice(obstacle_pair_sizes)
            topBuildingHeight, bottomBuildingHeight = building_pair_size[0] * obstacleSize, building_pair_size[1] * obstacleSize
            buildingTop = Building((WIDTH, 0 - (bottomBuildingHeight + obstacleGap)), obstacleSize, HEIGHT, True)
            buildingBottom = Building((WIDTH, topBuildingHeight + obstacleGap), obstacleSize, HEIGHT, False)
            self.obstacles.add(buildingTop)
            self.obstacles.add(buildingBottom)
            self.currentObstacle = buildingTop

    def _generate_world(self):
        self._add_obstacle()
        if self.current_theme == "bird":
            bird = Bird((WIDTH//2 - obstacleSize, HEIGHT//2 - obstacleSize), 30)
            self.player.add(bird)
        if self.current_theme == "mexbird":
            bird = Mexbird((WIDTH//2 - obstacleSize, HEIGHT//2 - obstacleSize), 30)
            self.player.add(bird)
        if self.current_theme == "plane":
            plane = Plane((WIDTH//2 - obstacleSize, HEIGHT//2 - obstacleSize), 30)
            self.player.add(plane)

    def _scroll_x(self):
        if self.playing:
            self.worldShift = -6
        else:
            self.worldShift = 0

    def _apply_gravity(self, player):
        if self.current_theme == "bird":
            if self.playing or self.gameOver:
                player.direction.y += self.gravity
                player.rect.y += player.direction.y
        if self.current_theme == "mexbird":
            if self.playing:
                player.direction.y += self.gravity
                player.rect.y += player.direction.y

        if self.current_theme == "plane":
            if self.playing:
                player.direction.y += self.gravity 
                player.rect.y += player.direction.y

    
    #def _animate(self):
    #    sprites = self.explosionImg
    #    spriteIndex = (self.frameIndex // self.explosionAnimationDelay) % len(sprites)
    #    self.image = sprites[spriteIndex]
    #    self.frameIndex += 1
    #    self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
    #    self.mask = pygame.mask.from_surface(self.image)
    #    if self.frameIndex // self.animationDelay > len(sprites):
    #        self.frameIndex = 0

    def _handle_collisions(self, player):
        bird = self.player.sprite
        if pygame.sprite.groupcollide(self.player,self.obstacles, False, False) or bird.rect.bottom >= HEIGHT or bird.rect.top <= 0:

            if self.current_theme == "plane" and not self.explosion_triggered:
                collisionX = (bird.rect.centerx) - 10
                collisionY = (bird.rect.centery) + 10
                
                self.screen.blit(self.explosion_images[self.explosion_index // 5], (collisionX - 50, collisionY - 100))
                self.explosion_index += 1
                if self.explosion_index >= len(self.explosion_images) * 5:
                    self.explosion_triggered = True
                    self.explosion_index = 0
                    pass

            elif self.current_theme == "mexbird" and not self.explosion_triggered:
                collisionX = (bird.rect.centerx) - 10
                collisionY = (bird.rect.centery) + 10                
                self.screen.blit(self.burrito_explosion_images[self.explosion_index // 5], (collisionX - 50, collisionY - 100))
                self.explosion_index += 1
                if self.explosion_index >= len(self.burrito_explosion_images) * 5:
                    self.explosion_triggered = True
                    self.explosion_index = 0
                    pass
            self.playing = False
            self.gameOver = True
            if self.gameOver:
                self.screen.blit(self.gameOverImg,(100, 200))
        else:
            if bird.rect.x >= self.currentObstacle.rect.centerx:
                bird.score += 1
                self.passed = True

    def update(self, playerEvent=None):
        if self.current_theme == "bird":
            if self.currentObstacle.rect.centerx <= (WIDTH // 2) - obstacleSize:
                self._add_obstacle()
            self.obstacles.update(self.worldShift)
            self.obstacles.draw(self.screen)
        elif self.current_theme == "mexbird":
            if self.currentObstacle.rect.centerx <= (WIDTH // 2) - obstacleSize:
                self._add_obstacle()
            self.obstacles.update(self.worldShift)
            self.obstacles.draw(self.screen)
        elif self.current_theme == "plane":
            if self.currentObstacle.rect.centerx <= (WIDTH // 2) - obstacleSize:
                self._add_obstacle()
            self.obstacles.update(self.worldShift)
            self.obstacles.draw(self.screen)


        self._apply_gravity(self.player.sprite)
        self._scroll_x()
        self._handle_collisions(self.player.sprite)
        
        if playerEvent == "jump" and not self.gameOver:
            playerEvent = True
        elif playerEvent == "restart":
            self.gameOver = False
            self.explosion_triggered = False
            self.obstacles.empty()
            self.player.empty()
            self.player.score = 0
            self._generate_world()
        else:
            playerEvent = False

        if not self.playing:
            self.game.instructions()
        self.player.update(playerEvent)
        self.player.draw(self.screen)
        self.game.show_score(self.player.sprite.score)


