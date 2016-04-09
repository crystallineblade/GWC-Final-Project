import time

def start():
    stage.set_background("mars")
    startSprites = []

    start_text = codesters.Text("Game Demo", 0, 50, "white")
    start_text.set_size(1.5)
    startSprites.append(start_text)
    
    start_game_b = codesters.Rectangle(-100, -50, 150, 40, "gray")
    instruction_b = codesters.Rectangle(100, -50, 150, 40, "gray")
    start_game_b.set_opacity(0.25)
    instruction_b.set_opacity(0.25)
    startSprites.append(start_game_b)
    startSprites.append(instruction_b)

    start_game = codesters.Text("Start Game", -100, -50, "silver")
    instruction = codesters.Text("Instructions", 100, -50, "silver")
    startSprites.append(start_game)
    startSprites.append(instruction)
    
    copy = codesters.Text("JS GWC Calabazas Copyright 2016", 205, -240, "gray")
    copy.set_size(0.25)
    startSprites.append(copy)
    
    def click():
        x = stage.click_x()
        y = stage.click_y()
        if x <= -25 and x >= -175 and y <= -30 and y >= -75:
            for sprite in startSprites:
                stage.remove_sprite(sprite)
            game()
        if x <= 175 and x >= 25 and y <= -30 and y >= -75:
            for sprite in startSprites:
                stage.remove_sprite(sprite)
            instructions()
    stage.event_click(click)

def instructions():
    iSprites = []
    IT = codesters.Text("Instructions", 0, 200, "white")
    IT.set_size(1.5)
    text = codesters.Text("You are an alien from the planet X-9000, and humans have started invading your planet! You must help pick up your fellow aliens and escape to another planet!", 0, 150, "silver")
    iSprites.append(IT)
    iSprites.append(text)
    
    keys = codesters.Text("Keys", 0, 65, "white")
    keys.set_size(1.25)
    ktext = codesters.Text("Use arrow keys to move.", 0, 30, "silver")
    iSprites.append(keys)
    iSprites.append(ktext)
    
    objectives = codesters.Text("Objectives", 0, -25, "white")
    objectives.set_size(1.25)
    otext = codesters.Text("Dodge rockets and meteors to survive. Help aliens to collect points. Land on the planet X-9001 to win!", 0, -65, "silver")
    iSprites.append(objectives)
    iSprites.append(otext)
    
    start_game_b = codesters.Rectangle(-100, -175, 150, 40, "gray")
    back_b = codesters.Rectangle(100, -175, 150, 40, "gray")
    start_game_b.set_opacity(0.25)
    back_b.set_opacity(0.25)
    iSprites.append(start_game_b)
    iSprites.append(back_b)

    start_game = codesters.Text("Start Game", -100, -175, "silver")
    back = codesters.Text("Back to Menu", 100, -175, "silver")
    iSprites.append(start_game)
    iSprites.append(back)

    def click():
        x = stage.click_x()
        y = stage.click_y()
        if x <= -25 and x >= -175 and y <= -155 and y >= -195:
            for sprite in iSprites:
                stage.remove_sprite(sprite)
            game()
        if x <= 175 and x >= 25 and y <= -155 and y >= -195:
            for sprite in iSprites:
                stage.remove_sprite(sprite)
            start()
    stage.event_click(click)

def game():
    global stop
    stop = 0
    gameSprites = []
    stage.set_background("scrollingspace")
    
    start_ground = codesters.Rectangle(-250, 0, 75, 500, "gray")
    stage.disable_all_walls()
    gameSprites.append(start_ground)
    
    global points
    points = 0
    global lives
    lives = 3
    points_display = codesters.Display(points, -200, 200)
    lives_display = codesters.Display(lives, -125, 200)
    
    ufo = codesters.Sprite("ufo", -230, 0)
    ufo.set_size(0.3)
    gameSprites.append(ufo)
    
    result_text = codesters.Text(" ")
    gameSprites.append(result_text)
    def collision(sprite, hit_sprite):
        image = hit_sprite.get_image_name() 
        if image == "meteor2":
            result_text.set_text("YOU WON!")
            result_text.set_color("green")
            stop = 1
            print ("STOP IS TRUE WIN")
            for sprite in gameSprites:
                stage.remove_sprite(sprite)
            stage.wait(2)
            win()
        if image == "rocket" or image == "meteor1":
            global lives
            lives -= 1
            stage.remove_sprite(hit_sprite)
            lives_display.update(lives)
            if lives == 0:
                result_text.set_text("YOU LOST!")
                result_text.set_color("red")
                sprite.go_to(0, -240)
                stop = 1
                print ("STOP IS TRUE LOSE")
                for sprite in gameSprites:
                    stage.remove_sprite(sprite)
                lose()
            else:
                sprite.go_to(-230, 0)
                stage.wait(1)
        if image == "alien1" or image == "alien2":
            global points
            points += 1
            points_display.update(points)
            stage.remove_sprite(hit_sprite)
    ufo.event_collision(collision)
    
    def make_NME1():
        if stop == 0:
            enemy_img = random.choice(["rocket", "meteor1"])
            NME = codesters.Sprite(enemy_img, -150, -400)
            NME.set_size(0.5)
            if enemy_img == "meteor1":
                NME.turn_left(90)
            rand_speed = random.randint(2,3)
            NME.set_y_speed(rand_speed)
            gameSprites.append(NME)
        else:
            return
    def make_NME3():
        if stop == 0:
            enemy_img = random.choice(["rocket", "meteor1"])
            NME = codesters.Sprite(enemy_img, 50, -400)
            NME.set_size(0.5)
            if enemy_img == "meteor1":
                NME.turn_left(90)
            rand_speed = random.randint(2,3)
            NME.set_y_speed(rand_speed)
            gameSprites.append(NME)
        else:        
            return
    def make_NME2():
        if stop == 0:
            enemy_img = random.choice(["rocket", "meteor1"])
            NME = codesters.Sprite(enemy_img, -50, 400)
            NME.set_size(0.5)
            if enemy_img == "meteor1":
                NME.turn_right(90)
            else:
                NME.turn_left(180)
            rand_speed = random.randint(-3,-2)
            NME.set_y_speed(rand_speed)
            gameSprites.append(NME)
        else:
            return
    def make_NME4():
        if stop == 0:
            enemy_img = random.choice(["rocket", "meteor1"])
            NME = codesters.Sprite(enemy_img, 150, 400)
            NME.set_size(0.5)
            if enemy_img == "meteor1":
                NME.turn_right(90)
            else:
                NME.turn_left(180)
            rand_speed = random.randint(-3,-2)
            NME.set_y_speed(rand_speed)
            gameSprites.append(NME)
        else:        
            return

    def interval():
        if stop == 0:
            make_NME2()
            make_NME4()
        else:
            return
    stage.event_interval(interval, 3)

    y = 150
    for counter in range(4):
        goal = codesters.Sprite("meteor2", 350, y)
        goal.set_size(3)
        gameSprites.append(goal)
        y -= 100

    def rand():
        if stop == 0:
            my_var = random.randint(1, 4)
            if my_var == 1:
                make_NME1()
            if my_var == 2:
                make_NME3()
        else:
            return
    def up_key():
        if stop == 0:
            ufo.move_up(10)
        else:
            return
    stage.event_key("up", up_key)
    def down_key():
        if stop == 0:
            ufo.move_down(10)
        else:
            return
    stage.event_key("down", down_key)
    def left_key():
        if stop == 0:
            ufo.move_left(10)
            rand()
        else:
            return
    stage.event_key("left", left_key)
    def right_key():
        if stop == 0:
            ufo.move_right(10)
            rand()
        else:
            return
    stage.event_key("right", right_key)
    
    for counter in range(3):    
        rand_x = random.randint(-100, -50)
        rand_y = random.randint(-250, 250)
        rand_add = random.randint(100, 150)
        img_list = ["alien1", "alien2"]
        randompoint = random.choice(img_list)
        x = rand_x + (rand_add * counter)
        point = codesters.Sprite(randompoint, x, rand_y)
        point.set_size(0.3)
        gameSprites.append(point)

def win():
    stage.set_background("jupiter")
    wSprites = []
    
    wtext = codesters.Text("YOU WON!", 0, 200, "green")
    wSprites.append(wtext)
    wtext.set_size(1.5)
    
    swtext = codesters.Text("Congratulations! You have reached planet X-9001! You are a national hero!", 0, 150, "white")
    wSprites.append(swtext)
    
    trophy = codesters.Sprite("trophy", 0, 0)
    wSprites.append(trophy)
    trophy.turn_right(360)
    
    swtext2 = codesters.Text("Here is your reward!", 0, -100, "white")
    swtext3 = codesters.Text("Would you like to return to menu, or play again?", 0, -150, "white")
    wSprites.append(swtext2)
    wSprites.append(swtext3)
    
    start_game_b = codesters.Rectangle(-100, -200, 150, 40, "gray")
    back_b = codesters.Rectangle(100, -200, 150, 40, "gray")
    start_game_b.set_opacity(0.25)
    back_b.set_opacity(0.25)
    wSprites.append(start_game_b)
    wSprites.append(back_b)

    start_game = codesters.Text("Play Again", -100, -200, "silver")
    back = codesters.Text("Back to Menu", 100, -200, "silver")
    wSprites.append(start_game)
    wSprites.append(back)

    def click():
        x = stage.click_x()
        y = stage.click_y()
        if x <= -25 and x >= -175 and y <= -180 and y >= -220:
            for sprite in wSprites:
                stage.remove_sprite(sprite)
            game()
        if x <= 175 and x >= 25 and y <= -180 and y >= -220:
            for sprite in wSprites:
                stage.remove_sprite(sprite)
            start()
    stage.event_click(click)
    


def lose():
    stage.set_background("jupiter")

start()



