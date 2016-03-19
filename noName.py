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
    
    def make_NME():
        enemy_img = random.choice(["rocket", "meteor1"])
        rand_x = random.choice([-150, -50, 50, 150])
        if rand_x == -150 or rand_x == 50:
            NME = codesters.Sprite(enemy_img, rand_x, -400)
            if enemy_img == "meteor1":
                NME.turn_left(90)
            rand_speed = random.randint(2, 3)
            NME.set_y_speed(rand_speed)
        if rand_x == -50 or rand_x == 150:
            NME = codesters.Sprite(enemy_img, rand_x, 400)
            if enemy_img == "meteor1":
                NME.turn_right(90)
            else:
                NME.turn_left(180) 
            rand_speed = random.randint(-3, -2)
            NME.set_y_speed(rand_speed)
        NME.set_size(0.5)
        gameSprites.append(NME)
    
    def interval():
        make_NME()
    stage.event_interval(interval, 1)   
    
    y = 150
    for counter in range(4):
        goal = codesters.Sprite("meteor2", 350, y)
        goal.set_size(3)
        gameSprites.append(goal)
        y -= 100

    def up_key():
        ufo.move_up(10)
    stage.event_key("up", up_key)
    def down_key():
        ufo.move_down(10)
    stage.event_key("down", down_key)
    def left_key():
        ufo.move_left(10)
    stage.event_key("left", left_key)
    def right_key():
        ufo.move_right(10)
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
    
    result_text = codesters.Text(" ")
    def collision(sprite, hit_sprite):
        image = hit_sprite.get_image_name() 
        if image == "meteor2":
            result_text.set_text("YOU WON!")
            result_text.set_color("green")
        if image == "rocket" or image == "meteor1":
            global lives
            lives -= 1
            stage.remove_sprite(hit_sprite)
            lives_display.update(lives)
            if lives == 0:
                result_text.set_text("YOU LOST!")
                result_text.set_color("red")
                sprite.go_to(0, -240)
            else:
                sprite.go_to(-230, 0)
        if image == "alien1" or image == "alien2":
            global points
            points += 1
            points_display.update(points)
            stage.remove_sprite(hit_sprite)
    ufo.event_collision(collision)

start()



