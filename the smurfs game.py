  

from gamelib import*
game = Game(800,600,"The Smurfs",60)
bk = Image("maze.png",game)
                               

title = Image("logo.png",game)
title.y -= 200

story = Image("story.png",game)
story.resizeBy(-40)
story.y += 100

howtoplay = Image("howtoplay.png",game)
howtoplay.resizeBy(-40)
howtoplay.y += 150
play = Image("play.png",game)
play.resizeBy(-40)
play.y += 200


bk.resizeTo(800,600)
Richin = Image("Richin.jpg",game,use_alpha=False)
Richin.resizeBy(-50)
Richin.setSpeed(11,60)#set speed in o
Jaydinoroon = Image("Jaydinoroon.jpg", game,use_alpha=False)
Jaydinoroon.resizeBy(-50)
Jaydinoroon.setSpeed(11,60)
Anota = Image("Anota.png",game,use_alpha=False)#image object
Anota.resizeBy(-50)
Anota.setSpeed(11,60)
smurf=Image("Smurf.jpg",game,use_alpha=False)
smurf.resizeBy(-80)
smurf.moveTo(450,558)
chest=Image("chest.png",game,use_alpha=False)
chest.resizeBy(-80)
chest.moveTo(400,5)




for index in range(100):
          
     if smurf(index).collidedWith(Richin):
            smurf.health -= 1
 
        
     game.processInput()
     bk.draw()
     Richin.move(True)
     Jaydinoroon.move(True)
     Anota.move(True) 
     Richin.draw()
     Jaydinoroon.draw()
     Anota.draw()
     smurf.draw()
     chest.draw()
     

     
        
     if keys.Pressed[K_UP]:
        smurf.y -= 4
     if keys.Pressed[K_DOWN]:
        smurf.y += 4
     if keys.Pressed[K_RIGHT]:
        smurf.x += 4
     if keys.Pressed[K_LEFT]:
        smurf.x -= 4
     


     game.update(60)
game.quit()
 
 

        
        
    


     
    
    


                                             
 
