import os
import sys

import pygame
import requests

map_request = "http://static-maps.yandex.ru/1.x"
params = {
    'll': ','.join(['37.530887', '55.703118']),
    'l': 'sat',
    'spn': ','.join(['0.002', '0.002'])
}

response = requests.get(map_request, params)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)
