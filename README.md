# Star-Strikers

Python game built with the module pygame.

## Goal

Live as long as you can while protecting the earth from enemies.
The earth health bar is at the left and the spaceship health is at the right.

### Controls

To move the spaceship you can use the WASD keys or the arrow keys.

You can press the left SHIFT to deploy the shield. However, you have a limited amount of shield energy.
The longer you hold SHIFT, the more the energy goes down. At 0 energy, you can no longer use the shield. 

To shoot bullets, press the SPACE key.

#### Attacking

Enemies have 10 health points. When you completly kill them, they wiil pause. But it 10 seconds or so, they will come back a full power. Every time you pause an enemy, earth health will go up by 1 and your shield energy will also increase.

##### Defending

Enemies will rain bullets at you. To defend, you take out your shield and block the bullets from hitting earth. Without the shield, the bullets will take damage on the player. 

###### Power Ups

There are five powerups you can get.

Health Powerup: Increases you spaceship health by 1 every time.

Bullet Powerup: Increases the amount bullets you can shoot rapidly.

Speed Powerup: Boosts the speed of your spaceship.

Energy Powerup: Increases the energy of your shield when the energy is lower than 45 (Megawatts).

Time Powerup: Makes the enemy bullets slower and easier to block.
