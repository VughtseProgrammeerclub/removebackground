import pygame
import pygame.camera
from pygame.locals import *

from rembg import remove
from PIL import Image

pygame.init()

gameDisplay = pygame.display.set_mode((640,480))

pygame.camera.init()
print (pygame.camera.list_cameras())
cam = pygame.camera.Camera("TOSHIBA Web Camera - HD",(640,480))
cam.start()
while True:
   img = cam.get_image()
   pygame.image.save(img, "input.png")
   input_path='input.png'
   output_path='output.png'
   input = Image.open(input_path)
   output = remove(input)
   output.save(output_path)

   gameDisplay.blit(img,(0,0))
   pygame.display.update()
   for event in pygame.event.get() :
      if event.type == pygame.QUIT :
         cam.stop()
         pygame.quit()
         exit()