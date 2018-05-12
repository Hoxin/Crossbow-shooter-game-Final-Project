# Crossbow-shooter-game-Final-Project

This is my final project for my Intro to Computer Science class. For this project, I decided to create a survival based top down shooter 
game. I based the game off of a copmuter game I used to play when I was in elementary school called Medieval Rampage, which is a top down
shooter where you play an archer killing waves of enemies. I thought this would be a cool project to work on as it gives me the opportunity
to use all of thh various things I have been taught throughout the semester. Furthermore, I thought creating a survival type shooter would
be cool.

Throughout the making of this project, I got a few of the fundamental concepts from another shooting game. I then expanded from the codes 
create my own version of a survival shooter game. I also used stack overflow for a few quesitons here and there. When it came to creating
images for the player, enemies, and any other image required, I downloaded them off of google, pintrest, the bunny game, or the Medieval 
rampage game my game is based upon. I used photoshop to cut and resize all of the images used. When it came to the arrows, I hand drew them
using adobe photoshop. 

My project is entirely based around the utilization of the pygame library. That being said, I began my project with the fundamental steps of 
importing pygame, and all of the other libraries I would need such as the math and random libraries. I then proceeded to create the screen I 
would use for my game, and set the parameters for said screen. From here, I made my first task drawing the player image I planned to use on 
the screen. I then proceeded to work on moving the player image using the traditional WASD keys Up, left, down, and right respectively. My
next task was to get the player to be able to shoot arrows. Once this was done, I began working on the enemies. I knew I wanted there to 
be multiple enemies active at a time, and I wanted all of them to be able to "follow" or "track" my the player as he/she moves around 
trying to shoot the enemies. This was the first major stump I had, as the bunny game I was using as a guide only moved thier enemies in a 
set direction. Furthermore, I wanted there to be different kinds of enemies with different images, speeds, attack power, etc. Eventually,
I figured this issue out by creating an enemy class, and then within my game loop creating instances of enemies with the enemy class, each 
different attributes. After I worked out the movement with the enemies, the next task I had to do was to create the collisions between the
enemies and the player, as well as between the arrows the player shoots and the enemies. After this, the core of my game was complete. It 
was here that I decided I wanted to add much more to the game to create more diversity and customization. This entailed creating different 
kinds of arrows the player can use that each have their own unique mechanics. At the time this README is being created, I am working on 
unique mechanics for the various arrows. I am also working on creating a round system, where after several rounds will culminate in a 
"boss fight", adn then continue on with stronger enemies. I also plan to add unique enemy mechanics, wehre same may shoot projectilces at 
plyaer, etc. 

Overall, while I was coding this project, a focus of mine was to code the game so it runs as efficientlt as possible. This entailed 
utilizing classes and functions to easily be called throughout the game loop.

Overall, I had a great time making this game. Although I will be presenting this project roughly two days after this README is created, 
I plan to keep working on this game, and update this README if any major changes happen. 

Thanks for playing!
