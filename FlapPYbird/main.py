import pygame
import sys
import os

from settings import WIDTH, HEIGHT, groundSpace
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT + groundSpace))
pygame.display.set_caption("Flappy Bird")

class Main:
    def __init__(self, screen):
        self.screen = screen
        self.bgImg = pygame.image.load("assets/terrain/background-day.png")
        self.bgImg = pygame.transform.scale(self.bgImg, (WIDTH, HEIGHT))
        self.groundImg = ""
        self.birdGroundImg = pygame.image.load("assets/terrain/bird-base.png")
        self.birdGroundImg = pygame.transform.scale(self.birdGroundImg, ((WIDTH + 40), groundSpace))
        self.planeGroundImg = pygame.image.load("assets/terrain/plane-base.png")
        self.planeGroundImg = pygame.transform.scale(self.planeGroundImg, ((WIDTH + 40), groundSpace))
        self.mexBirdGroundImg = pygame.image.load("assets/terrain/mex-bird-base.jpg")
        self.mexBirdGroundImg = pygame.transform.scale(self.mexBirdGroundImg, ((WIDTH + 40), groundSpace))
        self.groundScroll = 0
        self.scrollSpeed = -3.75
        self.FPS = pygame.time.Clock()
        self.stopGroundScroll = False

        # Load bird and plane images
        self.bird_images = self.load_images_from_folder("assets/bird")
        self.plane_images = self.load_images_from_folder("assets/plane")
        self.mexBird_images = self.load_images_from_folder("assets/mex-bird")
        self.tower_image = pygame.image.load("assets/terrain/tower.png").convert_alpha()
        self.animation_delay = 100
        self.animate_buttons = True
        self.frame_index = 0
        self.game_started = False  

        # Button size
        self.button_width = 34
        self.button_height = 24

        # Theme variable
        self.current_theme = "bird"  # Default theme
        self.groundImg = self.birdGroundImg
    
    def handle_click(self, button):
        if button == "bird":
            print("Bird theme selected")
            self.current_theme = "bird"  # Change the current theme
            self.groundImg = self.birdGroundImg
            self.scrollSpeed = -3.75
        if button == "mexbird":
            print("Mexican bird theme selected")
            self.current_theme = "mexbird"  # Change the current theme
            self.groundImg = self.mexBirdGroundImg
            self.scrollSpeed = -3.75
        elif button == "plane":
            print("Plane theme selected")
            self.current_theme = "plane"  # Change the current theme
            self.scrollSpeed = -5
            self.groundImg = self.planeGroundImg
            
        # Pass the current theme to the World instance again
        self.world = World(screen, self.current_theme)

    def load_images_from_folder(self, folder):
        images = []
        for filename in os.listdir(folder):
            path = os.path.join(folder, filename)
            image = pygame.image.load(path).convert_alpha()
            images.append(image)
        return images
    

    def resize_images_to_match(self, source_images, target_size):
        resized_images = []
        for image in source_images:
            resized_image = pygame.transform.scale(image, target_size)
            resized_images.append(resized_image)
        return resized_images

    def main(self):
        world = World(screen, self.current_theme)  # Initialize world here
        while True:
            self.stopGroundScroll = world.gameOver
            self.screen.blit(self.bgImg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if not world.playing and not world.gameOver:
                        world.playing = True
                        self.game_started = True  # Game has started
                    if event.key == pygame.K_SPACE:
                        world.update("jump")
                    if event.key == pygame.K_r:
                        world.update("restart")
                        self.game_started = False  # Reset game started flag when restarting

                elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_started:  # Only handle clicks if the game has not started
                    mouse_pos = pygame.mouse.get_pos()
                    button_clicked = self.is_clicked(mouse_pos)
                    if button_clicked:
                        self.handle_click(button_clicked)
                        # Recreate the World instance with the updated theme
                        world = World(screen, self.current_theme)

            
            if self.current_theme == "bird":
                self.screen.blit(self.groundImg, (self.groundScroll, HEIGHT))
            if self.current_theme == "mexbird":
                self.screen.blit(self.groundImg, (self.groundScroll, HEIGHT))
            if self.current_theme == "plane":
                self.screen.blit(self.planeGroundImg, (self.groundScroll, HEIGHT))
            world.update()
            
            # Animate buttons if enabled and game has not started
            if self.animate_buttons and not self.game_started:
                self.animate_buttons = self.animate_buttons_on_screen()

            if not self.stopGroundScroll:
                self.groundScroll += self.scrollSpeed
                if abs(self.groundScroll) > 35:
                    self.groundScroll = 0

            pygame.display.update()
            self.FPS.tick(60)

    def animate_buttons_on_screen(self):
        button_x = 10
        button_y = 10

        if self.frame_index // self.animation_delay >= len(self.bird_images):
            self.frame_index = 0

        # Resize images to match the specified button size
        resized_plane_images = self.resize_images_to_match(self.plane_images, (self.button_width, self.button_height))
        resized_mexbird_images = self.resize_images_to_match(self.mexBird_images, (self.button_width, self.button_height))

        # animate pictures
        bird_image = self.bird_images[self.frame_index // self.animation_delay]
        plane_image = resized_plane_images[self.frame_index // self.animation_delay]
        mexbird_image = resized_mexbird_images[self.frame_index // self.animation_delay]
        
        # Adjusted positions for buttons
        bird_button_pos = (button_x, button_y)
        plane_button_pos = (button_x + self.button_width + 10, button_y)
        mexbird_button_pos = (button_x + self.button_width + 55, button_y)
        

        # button image drawn
        self.screen.blit(bird_image, bird_button_pos)
        self.screen.blit(plane_image, plane_button_pos)
        self.screen.blit(mexbird_image, mexbird_button_pos)

        self.frame_index += 1

        return True

    def is_clicked(self, mouse_pos):
        button_x = 10
        button_y = 10

        # Button hitbox
        bird_button_rect = pygame.Rect(button_x, button_y, self.button_width, self.button_height)
        plane_button_rect = pygame.Rect(button_x + self.button_width + 10, button_y, self.button_width, self.button_height)
        mexbird_button_rect = pygame.Rect(button_x + self.button_width + 55, button_y, self.button_width, self.button_height)

        if bird_button_rect.collidepoint(mouse_pos):
            return "bird"
        elif plane_button_rect.collidepoint(mouse_pos):
            return "plane"
        elif mexbird_button_rect.collidepoint(mouse_pos):
            return "mexbird"
        else:
            return None

    


if __name__ == "__main__":
    play = Main(screen)
    play.main()
