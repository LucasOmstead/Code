# ---------------------------------------------------------------------------- #
#                                                                              #
#   Name: Lucas Omstead    Date: Mar. 16th 2021                                #
#   Program Name:   Tricky Gauntlet!; tricky_gauntlet.py                       #
#                                                                              #
#   Description:    This program is a simple game. Each player tries to        #
#                   collect the star before the other player.  The first to 10 #
#                   points wins.                                               #
#                                                                              #
#   Interactions:   The players play this game entirely with keyboard          #
#                   controls:                                                  #
#                   * [w/up] moves up.                                         #
#                   * [a/left] moves left.                                     #
#                   * [d/right] moves right.                                   #
#                   * [s/down] moves down.                                     #
#                                                                              #
# ---------------------------------------------------------------------------- #

import random


app.started = False
app.finished = False
# Player icons
player2 = Star(300, 300, 30, 6, fill='red', roundness=0, visible=False)
player1 = Star(100, 300, 30, 6, fill='blue', roundness=0, visible=False)
# Points Tally
player1pts = Label(0, 50, 50, size=60, fill='blue', visible=False)
player2pts = Label(0, 350, 50, size=60, fill='red', visible=False)

p1wins = Label('Player 1 wins!', 200, 200, size=60, visible=False)
p2wins = Label("Player 2 wins!", 200, 200, size=60, visible=False)

Objective = Star(random.randint(1, 400), random.randint(1, 400), 30, 5, fill='green', roundness=70, visible=False)
# Starting box
started1 = Label('Start?', 200, 200, size=60, visible=True)
started2 = Rect(100, 150, 200, 100, fill=None, border='black')
started = Group(started1, started2)
smileygen = Circle(0, 0, 1)
# Restart Box
finished = Label('Restart?', 340, 30, size=30, visible=False)
# Steps per second
app.stepsPerSecond = 10


def onMousePress(mouseX, mouseY):
    if started.contains(mouseX, mouseY):
        app.started = True
        started.visible = False
        Objective.visible = True
        player1.visible = True
        player2.visible = True
        player1pts.visible = True
        player2pts.visible = True
    if finished.contains(mouseX, mouseY) and app.finished:
        player1pts.value = 0
        player2pts.value = 0
        player1.centerX = 100
        player2.centerX = 300
        player1.centerY = 300
        player2.centerY = 300
        player1pts.visible = True
        player2pts.visible = True
        player1.visible = True
        player2.visible = True
        Objective.visible = True
        app.started = True
        app.finished = False
        started.visible = False
        finished.visible = False
        player1.roundness = 0
        player2.roundness = 0
        p1wins.visible = False
        p2wins.visible = False


def onKeyHold(keys):
    if app.started:

        if 'w' in keys:
            player1.centerY -= 10
        if 's' in keys:
            player1.centerY += 10
        if 'd' in keys:
            player1.centerX += 10
        if 'a' in keys:
            player1.centerX -= 10
        if player2.hitsShape(Objective):
            player2pts.value += 1
            player2.roundness += 10
            Objective.centerX = random.randint(1, 400)
            Objective.centerY = random.randint(1, 400)
            if Objective.hitsShape(player1) or Objective.hitsShape(player2):
                Objective.centerX = random.randint(1, 400)
                Objective.centerY = random.randint(1, 400)
            if player2pts.value >= 10:
                p2wins.visible = True
                Objective.centerX = random.randint(1, 400)
                app.started = False
                Objective.visible = False
                player1pts.visible = False
                player1.visible = False
                app.finished = True
                finished.visible = True
        if 'i' in keys:
            player2.centerY -= 10
        if 'k' in keys:
            player2.centerY += 10
        if 'j' in keys:
            player2.centerX -= 10
        if 'l' in keys:
            player2.centerX += 10
        if player1.hitsShape(Objective):
            player1pts.value += 1
            player1.roundness += 10
            Objective.centerX = random.randint(1, 400)
            Objective.centerY = random.randint(1, 400)
            if Objective.hitsShape(player1) or Objective.hitsShape(player2):
                Objective.centerX = random.randint(1, 400)
                Objective.centerY = random.randint(1, 400)
            if player1pts.value >= 10:
                Objective.visible = False
                player2.visible = False
                player2pts.visible = False
                p1wins.visible = True
                app.started = False
                app.finished = True
                finished.visible = True
        if 'i' in keys and player2.centerY <= 0:
            player2.centerY = 400
        if 'k' in keys and player2.centerY >= 400:
            player2.centerY = 0
        if 'j' in keys and player2.centerX <= 0:
            player2.centerX = 400
        if 'l' in keys and player2.centerX >= 400:
            player2.centerX = 0
        if 'w' in keys and player1.centerY <= 0:
            player1.centerY = 400
        if 's' in keys and player1.centerY >= 400:
            player1.centerY = 0
        if 'd' in keys and player1.centerX >= 400:
            player1.centerX = 0
        if 'a' in keys and player1.centerX <= 0:
            player1.centerX = 400
        # Doesn't work very well yet
        if ((Objective.centerX - player1.centerX) ** 2 + (Objective.centerY - player1.centerY) ** 2) ** .5 < (
                (Objective.centerX - player2.centerX) ** 2 + (Objective.centerY - player2.centerX) ** 2) ** .5:
            if Objective.centerX < player1.centerX and Objective.centerY < player1.centerY:
                Objective.centerX -= 2
                Objective.centerY -= 2
            elif Objective.centerX <= player1.centerX and Objective.centerY >= player1.centerY:
                Objective.centerX -= 2
                Objective.centerY += 2
            elif Objective.centerX > player1.centerX and Objective.centerY < player1.centerY:
                Objective.centerX += 2
                Objective.centerY -= 2
            else:
                Objective.centerX += 2
                Objective.centerY += 2
        else:
            if Objective.centerX < player2.centerX and Objective.centerY < player2.centerY:
                Objective.centerX -= 2
                Objective.centerY -= 2
            elif Objective.centerX <= player2.centerX and Objective.centerY >= player2.centerY:
                Objective.centerX -= 2
                Objective.centerY += 2
            elif Objective.centerX > player2.centerX and Objective.centerY < player2.centerY:
                Objective.centerX += 2
                Objective.centerY -= 2
            else:
                Objective.centerX += 2
                Objective.centerY += 2
        if Objective.centerX > 400:
            Objective.centerX = 0
        if Objective.centerY > 400:
            Objective.centerY = 0
        if Objective.centerY < 0:
            Objective.centerY = 400
        if Objective.centerX < 0:
            Objective.centerX = 400