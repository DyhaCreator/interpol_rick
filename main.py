import random as rnd
import math
import pygame

WIDTH = 1920 // 2
HEIGHT = 1080 // 2
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graphics")
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
def cel(x):
    return x
def activation(x):
    #x = min(-2, max(x, 2))
    return 1 / (1 + math.exp(-x)) * 2 - 1
x = 0
y = 0

w = [0] * 2
deep = [0] * 1
bias = [0] * 2
learnRate = 0.0001
start = 0
end = 1

for i in range(len(w)):
    w[i] = [0] * len(deep)
    for j in range(len(w[0])):
        w[i][j] = rnd.random()
        #w[i][j] = 0
#x = rnd.random() * 2 - 1
#w[0][0] = 1.8
#w[1][0] = 1.1
for i in range(len(bias)):
    bias[i] = rnd.random()
    #bias[i] = 0

for i in range(1000000):
    x = rnd.random()
    y = 0
    for j in range(len(deep)):
        deep[j] = activation(x * w[0][j] + bias[0])
    for j in range(len(deep)):
        y += deep[j] * w[1][j] + bias[1]
    y = round(y, 10)
    #print('y -',y)
    #print('err -', cel(x) - y)
    h = learnRate
    for k in range(len(bias)):
        hy = 0
        for j in range(len(deep)):
            if k == 0:
                deep[j] = activation(x * w[0][j] + bias[0] + h)
            else:
                deep[j] = activation(x * w[0][j] + bias[0])
        for j in range(len(deep)):
            if k == 1:
                hy += deep[j] * w[1][j] + bias[1] + h
            else:
                hy += deep[j] * w[1][j] + bias[1]
        hy = round(hy, 10)
        d = abs(cel(x) - round(y, 10)) - abs(cel(x) - round(hy, 10))
        s = d / h
        bias[k] += s * learnRate
    for j in range(len(w)):
        for k in range(len(w[j])):
            hy = 0
            for l in range(len(deep)):
                if (j == 0 and k == l):
                    deep[l] = activation(x * (w[0][l] + h) + bias[0])
                else:
                    deep[l] = activation(x * w[0][l] + bias[0])
            for l in range(len(deep)):
                if(j == 1 and k == l):
                    hy += deep[l] * (w[1][l] + h) + bias[1]
                else:
                    hy += deep[l] * w[1][l] + bias[1]
            hy = round(hy, 10)
            d = (cel(x) - y) - (cel(x) - hy)
            s = d / h
            print(d, s)
            w[j][k] += s * learnRate
    print(w)
    if(i % 1000 == 0):
        zoomy = 100
        screen.fill((0,0,0))
        light = 100
        pygame.draw.line(sc, (light, light, light), [WIDTH // 2, 0], [WIDTH // 2, HEIGHT], 1)
        pygame.draw.line(sc, (light, light, light), [0, HEIGHT // 2], [WIDTH, HEIGHT // 2], 1)
        pygame.draw.line(sc, (light, light, light), [100 + WIDTH // 2, HEIGHT // 2 - 10], [100 + WIDTH // 2, HEIGHT // 2 + 10], 1)
        for px in range(-WIDTH // 2, WIDTH // 2):
            X = px / 100
            y = cel(X) * zoomy
            pygame.draw.circle(sc, (0, 0, 255), (px + WIDTH // 2, HEIGHT // 2 - y), 2)
            y = 0
            for j in range(len(deep)):
                deep[j] = activation(X * w[0][j] + bias[0])
            for j in range(len(deep)):
                y += deep[j] * w[1][j] + bias[1]
            y = round(y, 10)
            pygame.draw.circle(sc, (255, 0, 0), (px + WIDTH // 2, HEIGHT // 2 - (y * zoomy)), 2)

            for j in range(len(w)):
                for k in range(len(w[j])):
                    hy = 0
                    for l in range(len(deep)):
                        if (j == 0 and k == l):
                            deep[l] = activation(X * (w[0][l] + h) + bias[0])
                        else:
                            deep[l] = activation(X * w[0][l] + bias[0])
                    for l in range(len(deep)):
                        if (j == 1 and k == l):
                            hy += deep[l] * (w[1][l] + h) + bias[1]
                        else:
                            hy += deep[l] * w[1][l] + bias[1]
                    hy = round(hy, 10)
                    d = abs(cel(x) - y) - abs(cel(x) - hy)
                    s = d / h
                    #w[j][k] -= s * learnRate
                    '''if(j == 0):
                        pygame.draw.circle(sc, (0, 255, 255), (px + WIDTH // 2, HEIGHT // 2 - s * zoomy), 1)
                    else:
                        pygame.draw.circle(sc, (255, 0, 255), (px + WIDTH // 2, HEIGHT // 2 - s * zoomy), 1)'''

            #print(cel(X), y, cel(X) - y)
            y = (cel(X) - y) * zoomy
            pygame.draw.circle(sc, (0, 255, 0), (px + WIDTH // 2, HEIGHT // 2 - y), 2)

        pygame.display.flip()

x = 1
hy = 0
for l in range(len(deep)):
    deep[l] = activation(x * w[0][l] + bias[0])
for l in range(len(deep)):
    hy += deep[l] * w[1][l] + bias[1]
hy = round(activation(hy), 10)
serr = cel(x) - hy
while x < end:
    hy = 0
    for l in range(len(deep)):
        deep[l] = activation(x * w[0][l] + bias[0])
    for l in range(len(deep)):
        hy += deep[l] * w[1][l] + bias[1]
    hy = round(activation(hy), 10)
    serr = cel(x) - hy
    serr /= 2
    x += 0.01
print(abs(serr))
print(w)
print(bias)
input()