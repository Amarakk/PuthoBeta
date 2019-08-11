from graphics import *
import time
import random
import pygame as pg
def play_music(music_file, volume=0.8):
    
    
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play(-1)
    

music_file = "kkk.mp3"

volume = 0.8
play_music(music_file, volume)


win=GraphWin("11",1000,1000)
fundo = Image(Point(500,500),"fundo.png")
boneco = Image(Point(500,900),"mickey.png")
enemy = Image(Point(150,150),"Pateta.gif")
welcome = Text(Point(300,900),"jogo do mickey garai")

startgame = Text(Point(900,900),"aperta ai pra começar")
winmessage = Text(Point(500,500),"GANHOOOOO")
fundo.draw(win)
boneco.draw(win)
time.sleep(1)
welcome.draw(win)
time.sleep(1)
startgame.draw(win)
win.getMouse()
welcome.undraw()
startgame.undraw()
enemy.draw(win)
errorcount = 0
num1= random.randint(150,790)
num2= random.randint(150,790)
error = Image(Point(num1,num2),"tenor.png")
erros = Text(Point(100,900),"Erros:")
erros.draw(win)
direcaoinimigo=10
shot=False
shotinimigo=False
contaerros = Text(Point(130,900),str(errorcount))
direcaotiro=-50
pos = boneco.getAnchor()
enemypos = enemy.getAnchor()
tiro = Image(Point(pos.x,pos.y-100),"laser.png")
tiroinimigo = Image(Point(enemypos.x,enemypos.y+100),"laser.png")
c=0
tempo=0

while True:

    contaerros.setText(str(errorcount))



    pos = boneco.getAnchor()
    
    enemypos = enemy.getAnchor()
    movimento = win.checkKey()
    num1= random.randint(150,790)
    num2= random.randint(150,790)
    if enemypos.getX()<900 and enemypos.getX()>149:
        enemy.move(direcaoinimigo,0)
    else:
        direcaoinimigo*=-1
        enemy.move(direcaoinimigo,0)
    
    if tempo%2==0 and tempo !=0:
        tiroinimigo = Image(Point(enemypos.x,enemypos.y+100),"laser.png")
        tiroinimigo.draw(win)
        shotinimigo=True
        tempo=0
        c=0
    if shotinimigo==True:
        tiroinimigo.move(0,-direcaotiro/2)
    if tiroinimigo.getAnchor().getY() > 1000:
        tiroinimigo.undraw()
    
    if movimento == "Right":
        boneco.move(10,0)
    if movimento == "Left":
        boneco.move(-10,0)
    if movimento == "space":
        tiro = Image(Point(pos.x,pos.y-100),"laser.png")
        tiro.draw(win)
        shot = True

    if shot == True:
        
        
        tiro.move(0,direcaotiro)
    
        
    if tiro.getAnchor().getX() <= enemypos.getX() + 110 and tiro.getAnchor().getX() >= enemypos.getX() - 130 and tiro.getAnchor().getY() <= enemypos.getY() :
        winmessage.draw(win)
        enemy.undraw()
        tiro.undraw()
        boom = Image(Point(enemypos.x,enemypos.y),"boom.gif")
        boom.draw(win)
        error.undraw()
        win.getMouse()
        win.close()

    if tiro.getAnchor().getY() < 0:
        error.undraw()
        shot = False
        tiro.undraw()
        tiro = Image(Point(pos.x,1000),"laser.png")
        contaerros.undraw()
        errorcount += 1
        contaerros.setText(str(errorcount))


        error = Image(Point(num1,num2),"tenor.png")

        error.draw(win)
        contaerros.draw(win)




    c+=1
    tempo=c//60
    time.sleep(1/60)
win.getMouse()
win.close()
