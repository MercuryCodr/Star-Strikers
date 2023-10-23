import pygame
import os
import random
import asyncio

rec = 0

pygame.font.init()
pygame.mixer.init()

w, h = 900, 650
WIN = pygame.display.set_mode((w, h))
pygame.display.set_caption("Star Strikers")

#Sound effects
laser = pygame.mixer.Sound("Star Strikers - Copy\short laser.wav")
cannonshot = pygame.mixer.Sound("Star Strikers - Copy\shooter.mp3")
playercolision = pygame.mixer.Sound("Star Strikers - Copy\colision2.mp3")
earthhit = pygame.mixer.Sound("Star Strikers - Copy\spacecol.mp3")
gameover = pygame.mixer.Sound("Star Strikers - Copy\game.wav")
shieldsound = pygame.mixer.Sound("Star Strikers - Copy\shieldsound.wav")
rewardsound = pygame.mixer.Sound("Star Strikers - Copy\ereward.wav")
hit = pygame.mixer.Sound("Star Strikers - Copy\enemyhit.mp3")

FPS = 60

#Fonts
score_font = pygame.font.SysFont('Roboto', 20)
r_font = pygame.font.SysFont('Impact', 40)
r_font2 = pygame.font.SysFont('Impact', 60)


#Shots
ahit = pygame.USEREVENT + 1
ahit2 = pygame.USEREVENT + 2 
planet_news = pygame.USEREVENT + 3
he = pygame.USEREVENT + 4
playerhit = pygame.USEREVENT + 5
energyboost  = pygame.USEREVENT + 6
healthboost  = pygame.USEREVENT + 7
bulletboost = pygame.USEREVENT + 8
speedboost = pygame.USEREVENT + 9
timeboost = pygame.USEREVENT + 10

#Time
clock = pygame.time.Clock()

#Sprite size
sw, sh = 80, 70
aw, ah = 60, 50
bw, bh = 40,45
esize = 1000

#Color
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0,0,0)

#Sprite load
spaceship_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'spaceship.png'))
alien_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'alien.png'))
bullet_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'blue.png'))
fire_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'red.png'))
earth_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'earth.png'))
shield_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'shield.png'))
heart_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'heart2.png'))
energy_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'bolt.png'))
back_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'space.png'))
game_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'gameover.png'))
gun_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'bulletpower.png'))
r_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'speedpower.png'))
clock_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'clock.png'))
h_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'heart.png'))
asteroids_image = pygame.image.load(
    os.path.join('Star Strikers - Copy', 'comet.png'))

#Sprite list
spaceship = pygame.transform.rotate(pygame.transform.scale(
    spaceship_image, (sw, sh)), 0)
alien = pygame.transform.rotate(pygame.transform.scale(
    alien_image, (aw, ah)), 0)
bull = pygame.transform.rotate(pygame.transform.scale(
    bullet_image, (bw, bh)), 90)
fireball = pygame.transform.rotate(pygame.transform.scale(
    fire_image, (bw, bh)), -90)
earth = pygame.transform.rotate(pygame.transform.scale(
    earth_image, (esize, esize)), 0)
shield = pygame.transform.rotate(pygame.transform.scale(
    shield_image, (sw + 10, 40)), 0)
heart = pygame.transform.rotate(pygame.transform.scale(
    heart_image, (20, 20)), 0)
bolt = pygame.transform.rotate(pygame.transform.scale(
    energy_image, (20, 20)), 0)
back = pygame.transform.rotate(pygame.transform.scale(
    back_image, (900, 650)), 0)
game = pygame.transform.rotate(pygame.transform.scale(
    game_image, (400, 450)), 0)
asteroid = pygame.transform.rotate(pygame.transform.scale(
    asteroids_image, (30, 30)), 320)
    
def draw(player, a1, a2, player_bullets, abullet, alien_bull, abullet2, alien_bull2, bars, bars2, pbars, spacebars, energy, score, player_health, planet_health, p1, power1, power2, power3, power4, power5, asteroids, health_rotation, energy_rotation, bullet_rotation, speed_rotation, time_rotation):
    WIN.blit(back, (0,0))
    WIN.blit(spaceship, (player.x,player.y))
    WIN.blit(alien, (a1.x, a1.y))
    WIN.blit(alien, (a2.x, a2.y))
    WIN.blit(earth, (450 - esize//2, 520))
    WIN.blit(heart, (785, 625))

    text = score_font.render(str(round(score)), 1, white)
    WIN.blit(text, (10, 450))

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LSHIFT] and energy > 0:
        WIN.blit(shield, (player.x -5, player.y - 10))
        shieldred = pygame.Rect(player.x + 15, player.y + 80, 60, 10)
        shieldgreen = pygame.Rect(player.x + 15, player.y + 80, energy, 10)
        WIN.blit(bolt, (player.x - 5, player.y + 75))
        pygame.draw.rect(WIN, (red), shieldred)
        pygame.draw.rect(WIN, (green), shieldgreen) 
        armour = pygame.Rect(player.x -4, player.y -5, 90, 100)

        if armour.colliderect(abullet):
            shieldsound.play()
            alien_bull.remove(abullet)

        elif armour.colliderect(abullet2):
            shieldsound.play()
            alien_bull2.remove(abullet2)

        for aster in asteroids:
            if armour.colliderect(aster):
                shieldsound.play()
                asteroids.remove(aster)
    
    if not keys_pressed[pygame.K_LSHIFT]:
        speed = 7

    for bullet in player_bullets:
        WIN.blit(bull, (bullet.x, bullet.y))

    for bullet in player_bullets:
       WIN.blit(bull, (bullet.x, bullet.y))
    
    for abullet in alien_bull:
       WIN.blit(fireball, (abullet.x, abullet.y))
       abullet.y += 2
    for abullet2 in alien_bull2:
       WIN.blit(fireball, (abullet2.x, abullet2.y))
       abullet2.y += 2
    for aster in asteroids:
        WIN.blit(asteroid, (aster.x, aster.y))  

    #Power Ups
    for p1 in power1:
        bolt2 = pygame.transform.rotate(pygame.transform.scale(
    energy_image, (30, 30)), energy_rotation)
        WIN.blit(bolt2, (p1.x, p1.y))    
    for p2 in power2:
        hea = pygame.transform.rotate(pygame.transform.scale(
    h_image, (25, 25)), health_rotation)
        WIN.blit(hea, (p2.x, p2.y)) 
    for p3 in power3:
        gun = pygame.transform.rotate(pygame.transform.scale(
    gun_image, (30, 30)), bullet_rotation)
        WIN.blit(gun, (p3.x, p3.y))
    for p4 in power4:
        rocket = pygame.transform.rotate(pygame.transform.scale(
    r_image, (30, 30)), speed_rotation)
        WIN.blit(rocket, (p4.x, p4.y))      
    for p5 in power5:
        clockk = pygame.transform.rotate(pygame.transform.scale(
    clock_image, (30, 30)), time_rotation)
        WIN.blit(clockk, (p5.x, p5.y))  

    healthred = pygame.Rect(a1.x, 5, 60, 5)
    healthgreen = pygame.Rect(a1.x, 5, bars, 5)

    healthred2 = pygame.Rect(a2.x, 85, 60, 5)
    healthgreen2 = pygame.Rect(a2.x, 85, bars2, 5)

    pygame.draw.rect(WIN, (red), healthred)
    pygame.draw.rect(WIN, (green), healthgreen)

    pygame.draw.rect(WIN, (red), healthred2)
    pygame.draw.rect(WIN, (green), healthgreen2)

    planetred = pygame.Rect(10, 490, 15, 150)
    planetgreen = pygame.Rect(10, 490, 15, pbars)

    pygame.draw.rect(WIN, (red), planetred)
    pygame.draw.rect(WIN, (green), planetgreen)

    playerred = pygame.Rect(810, 630, 80, 10)
    playergreen = pygame.Rect(810, 630, spacebars, 10)

    pygame.draw.rect(WIN, (red), playerred)
    pygame.draw.rect(WIN, (green), playergreen) 

    if player_health == 0 or planet_health == 0:
        WIN.blit(back, (0,0))
        WIN.blit(game, (250, 100))
        rtext = r_font.render("Score: " + str(round(score)), 5, white)
        WIN.blit(rtext, (350, 400))


    pygame.display.update()


def p(player, speed):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and player.x > 5:
        player.x -= speed
    if keys_pressed[pygame.K_d] and player.x < 810:
        player.x += speed
    if keys_pressed[pygame.K_s] and player.y <= 450:
        player.y += speed
    if keys_pressed[pygame.K_w] and player.y >= 200:
        player.y -= speed
    
    if keys_pressed[pygame.K_LEFT] and not keys_pressed[pygame.K_a] and player.x > 5:
        player.x -= speed
    if keys_pressed[pygame.K_RIGHT] and not keys_pressed[pygame.K_d] and player.x < 810:
        player.x += speed
    if keys_pressed[pygame.K_DOWN] and not keys_pressed[pygame.K_s] and player.y <= 450:
        player.y += speed
    if keys_pressed[pygame.K_UP] and not keys_pressed[pygame.K_w]  and player.y >= 200:
        player.y -= speed


def pbullets(player_bullets, a1, a2, player_health, planet_health):
    for bullet in player_bullets:
        bullet.y -= 7
        if a1.colliderect(bullet):
            if player_health != 0 or planet_health != 0:
                pygame.event.post(pygame.event.Event(ahit))
                player_bullets.remove(bullet)
        elif a2.colliderect(bullet):
            if player_health != 0 or planet_health != 0:
                pygame.event.post(pygame.event.Event(ahit2))
                player_bullets.remove(bullet)
        elif bullet.y <= -30:
            player_bullets.remove(bullet)

def alien_bullets(alien_bull, alien_bull2, abullet, planet, player, asteroids, bullspeed2):
    for abullet in alien_bull:
        if planet.colliderect(abullet):
            earthhit.play()
            pygame.event.post(pygame.event.Event(planet_news))
            alien_bull.remove(abullet)
        elif player.colliderect(abullet):
            playercolision.play()
            pygame.event.post(pygame.event.Event(playerhit))
            alien_bull.remove(abullet)
        elif abullet.y >= 630:
            alien_bull.remove(abullet)

    for abullet2 in alien_bull2:
        if planet.colliderect(abullet2):
            earthhit.play()
            pygame.event.post(pygame.event.Event(planet_news))
            alien_bull2.remove(abullet2)
        elif player.colliderect(abullet2):
            playercolision.play()
            pygame.event.post(pygame.event.Event(playerhit))
            alien_bull2.remove(abullet2)
        elif abullet2.y >= 630:
            alien_bull2.remove(abullet2)

    for aster in asteroids:
        aster.y += bullspeed2
        if planet.colliderect(aster):
            earthhit.play()
            pygame.event.post(pygame.event.Event(planet_news))
            asteroids.remove(aster)
        elif player.colliderect(aster):
            playercolision.play()
            pygame.event.post(pygame.event.Event(playerhit))
            asteroids.remove(aster)


def powerups(power1, p1, player, planet, power2, power3, power4, power5):
    for p1 in power1:
        p1.y += 3
        if player.colliderect(p1):
            rewardsound.set_volume(0.4)
            rewardsound.play()
            pygame.event.post(pygame.event.Event(energyboost))
            power1.remove(p1)
        if planet.colliderect(p1):
            power1.remove(p1)

    for p2 in power2:
        p2.y += 3
        if player.colliderect(p2):
            rewardsound.set_volume(0.4)
            rewardsound.play()
            pygame.event.post(pygame.event.Event(healthboost))
            power2.remove(p2)
        if planet.colliderect(p2):
            power2.remove(p2)

    for p3 in power3:
        p3.y += 3
        if player.colliderect(p3):
            rewardsound.set_volume(0.4)
            rewardsound.play()
            pygame.event.post(pygame.event.Event(bulletboost))
            power3.remove(p3)
        if planet.colliderect(p3):
            power3.remove(p3)

    for p4 in power4:
        p4.y += 3
        if player.colliderect(p4):
            rewardsound.set_volume(0.4)
            rewardsound.play()
            pygame.event.post(pygame.event.Event(speedboost))
            power4.remove(p4)
        if planet.colliderect(p4):
            power4.remove(p4)

    for p5 in power5:
        p5.y += 3
        if player.colliderect(p5):
            rewardsound.set_volume(0.4)
            rewardsound.play()
            pygame.event.post(pygame.event.Event(timeboost))
            power5.remove(p5)
        if planet.colliderect(p5):
            power5.remove(p5)

def pause_button(score):
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    shieldsound.play()
                    pause = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        WIN.blit(back, (0, 0))

        pausetext = r_font.render("Score: " + str(round(score)), 5, white)
        pausetext3 = score_font.render("Press C to Continue", 1, white)

        WIN.blit(pausetext3, (380, 300))
        WIN.blit(pausetext, (375, 350))

        pygame.display.update()

        clock.tick(5)
            
async def main():
    #Rectangles
    player = pygame.Rect(w/2 - 45, h/2 + 100, sw, sh)
    a1 = pygame.Rect(10, 10, aw, ah)
    a2 = pygame.Rect(w-70, 90, aw, ah)
    planet = pygame.Rect(130, 540, 660, 10)

    #Alien movements
    switch = 0
    switch2 = 1

    cannon = 0
    n = 0

    #bullets
    player_bullets = []
    alien_bull = []
    alien_bull2 = []
    power1 = []
    power2 = []
    power3 = []
    power4 = []
    power5 = []
    asteroids = []

    #Health
    alien_health = 10
    alien_health2 = 10
    planet_health = 20
    player_health = 10

    #Alien speed
    vel = 4
    vel2 = 4

    #Time count
    time = 0
    time2 = 0

    #All counts 
    shoot = 0
    shoot2 = 0
    bars = 60
    bars2 = 60
    pbars = 150
    spacebars = 80
    energy = 60
    sr = 0
    score = 1
    sn = 0.06
    nb = 0

    max_bullets = 1

    bullspeed = 1
    bullspeed2 = 3
    speed = 7
    an = 1

    #Power Rotation
    energy_rotation = 0
    health_rotation = 0
    bullet_rotation = 0
    speed_rotation = 0
    time_rotation = 0

    run = True
    
    while run:
        if player_health == 0 or planet_health == 0:
            sr+= 1
            if sr == 1:
                sn = 0

        score = score + (sn)
        shoot += 1
        shoot2 += 1
        clock.tick(FPS)

        #Power Ups
        rec = random.randrange(100, 800)
        rec4 = random.randrange(1, 6)

        p1 = pygame.Rect(rec, -35, 30, 30)
        if round(score) % 85 == 0 and len(power1) <= 1 and rec4 == 1 and len(power3) == 0 and len(power2) == 0 and len(power4) == 0 and len(power5) == 0 and energy <= 45:
            power1.append(p1)
        
        rec2 = random.randrange(100, 800)
        p2 = pygame.Rect(rec2, -35, 30, 30)
        if round(score) % 75 == 0 and len(power2) <= 1 and rec4 == 2 and len(power3) == 0 and len(power1) == 0 and len(power4) == 0 and len(power5) == 0:
            power2.append(p2)
        
        rec3 = random.randrange(100, 800)
        p3 = pygame.Rect(rec3, -35, 30, 30)
        if round(score) % 100 == 0 and len(power3) <= 1 and rec4 == 3 and len(power2) == 0 and len(power1) == 0 and len(power4) == 0 and len(power5) == 0:
            power3.append(p3)
        
        rec44 = random.randrange(100, 800)
        p4 = pygame.Rect(rec44, -35, 30, 30)
        if round(score) % 75 == 0 and len(power4) <= 1 and rec4 == 4 and len(power2) == 0 and len(power1) == 0 and len(power3) == 0 and len(power5) == 0:
            power4.append(p4)

        rec55 = random.randrange(100, 800)
        p5 = pygame.Rect(rec55, -35, 30, 30)
        if round(score) % 100 == 0 and len(power5) <= 1 and rec4 == 5 and len(power2) == 0 and len(power1) == 0 and len(power3) == 0 and len(power4) == 0:
            power5.append(p5)
        
        rando = random.randrange(200, 650)
        aster = pygame.Rect(rando + 50, -50, 30, 30)
        if round(score) % 60 == 0 and len(asteroids) <= 1:
            asteroids.append(aster)
        
        if player_health == 0 or planet_health == 0:
            if nb == 0:
                gameover.play()
                nb += 1

        #Alien 1 movement
        if 830 > a1.x > 0 and switch == 0: #first alien
            a1.x += vel
            if a1.x == 830:
                switch += 1  

        if switch == 1:
            if 10 <= a1.x <= 830 or a1.x == 830: #first alien
                a1.x -= vel
                if a1.x == 10:
                    switch -= 1

        #Alien 1 movement
        if switch2 == 1:
            if 10 <= a2.x <= 830 or a2.x == 830: #second alien
                a2.x -= vel2
                if a2.x == 10:
                    switch2 -= 1
        if 830 > a2.x > 0 and switch2 == 0: #second alien
            a2.x += vel2
            if a2.x == 830:
                switch2 += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            #Alien events
            if event.type == ahit and alien_health - an != -1:
                hit.set_volume(0.2)
                hit.play()
                alien_health -= an
                bars -= 6 * an

            if event.type == ahit and alien_health - 1 != -1 and energy + 0.5 <= 60:
                energy += 0.5

            if event.type == ahit2 and alien_health2 - an != -1:
                hit.set_volume(0.2)
                hit.play()
                alien_health2 -= an
                bars2 -= 6 * an

            if event.type == ahit2 and alien_health2 - 1 != -1 and energy + 0.5 <= 60:
                energy += 0.5
            
            #Power Ups
            if event.type == energyboost and energy + 15 <= 60 and planet_health != 0 and player_health != 0:
                energy += 15

            if event.type == healthboost and player_health + 1 <= 10 and planet_health != 0 and player_health != 0:
                player_health += 1
                spacebars += 8
            
            if event.type == bulletboost and planet_health != 0 and player_health != 0:
                max_bullets += 0.5

            if event.type == speedboost and planet_health != 0 and player_health != 0:
                speed += 0.25

            if event.type == timeboost and bullspeed - 0.1 > 0 and bullspeed2 - 0.1 > 0:
                bullspeed -= 0.1
                bullspeed -= 0.1

            #Planet/Player events
            if event.type == planet_news and planet_health - 1 != -1:
                planet_health -= 1
                pbars -= 7.5
            if event.type == playerhit and player_health - 1 != -1:
                player_health -= 1
                n = 1
                spacebars -= 8

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(player_bullets) < max_bullets and nb == 0:
                        laser.play()
                        cannon += 1
                        if cannon % 2 > 0:
                            n=15
                        elif cannon % 2 == 0:
                            n=-60
                        bullet = pygame.Rect(
                            player.x + player.width//2 + n, player.y, bw, bh)
                        player_bullets.append(bullet)

                if event.key == pygame.K_q:
                    quit()
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    if player_health != 0 and planet_health != 0:
                        shieldsound.play()
                        pause_button(score)
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and energy - 0.02 >= 0:
            energy -= 0.02
        
        #Alien Bulltes
        abullet = pygame.Rect(a1.x + a1.width//2 -20, a1.y + 50, bw, bh)

        if shoot >= 170 and alien_health != 0 and nb == 0:
            if 790 >=a1.x >= 130:
                cannonshot.set_volume(0.3)
                cannonshot.play()
                alien_bull.append(abullet)
                shoot = 0
        for abullet in alien_bull:
            abullet.y += bullspeed
        
        abullet2 = pygame.Rect(a2.x + a2.width//2 -20, a2.y + 50, bw, bh)
        if shoot2 >= 170 and alien_health2 != 0 and nb == 0:
            if 790 >= a2.x >= 130:
                cannonshot.set_volume(0.3)
                cannonshot.play()
                alien_bull2.append(abullet2)
                shoot2 = 0

        for abullet2 in alien_bull2:
            abullet2.y += bullspeed
        
        #Power up rotation
        for p1 in power1:
            energy_rotation += 1
        for p2 in power2:
            health_rotation += 1
        for p3 in power3:
            bullet_rotation += 1
        for p4 in power4:
            speed_rotation += 1
        for p5 in power5:
            time_rotation += 1

        #alien health
        if alien_health == 0 and time == 0:
            rewardsound.set_volume(0.4)
            rewardsound.play()
        if alien_health == 0:
            vel = 0
            time += 1
        if alien_health == 0 and time == 1 and planet_health < 20:
            pbars += 7.5
            planet_health += 1

        if time >= 400:
            alien_health = 10
            vel = 4
            bars = 60
            time = 0

        if alien_health2 == 0 and time2 == 0:
            rewardsound.set_volume(0.4)
            rewardsound.play()
        if alien_health2 == 0:
            vel2 = 0
            time2 += 1
        if alien_health2 == 0 and time2 == 1 and planet_health < 2:
            pbars += 7.5
            planet_health += 1

        if time2 >= 400:
            alien_health2 = 10
            vel2 = 4
            bars2 = 60
            time2 = 0

        draw(player, a1, a2, player_bullets, abullet, alien_bull, abullet2, alien_bull2, bars, bars2, pbars, spacebars, energy, score, player_health, planet_health, p1, power1, power2, power3, power4, power5, asteroids, health_rotation, energy_rotation, bullet_rotation, speed_rotation, time_rotation)
        p(player, speed)
        pbullets(player_bullets, a1, a2, planet_health, player_health)
        alien_bullets(alien_bull, alien_bull2, abullet, planet, player, asteroids, bullspeed2)
        powerups(power1, p1, player, planet, power2, power3, power4, power5)
        
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
