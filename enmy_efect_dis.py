def origin(app,GS):
  if app.prayer.Prayer_conmaas_x <= 17:
    gen_x = 0
  elif app.prayer.Prayer_conmaas_x <= 189:
    gen_x = app.prayer.Prayer_conmaas_x-17
  else:
    gen_x = 173

    
  if app.prayer.Prayer_conmaas_y <= 11:    
      gen_y = 0
  elif app.prayer.Prayer_conmaas_y <= 290:
      gen_y = app.prayer.Prayer_conmaas_y - 11
  else:
      gen_y = 280
    
  # print(app.prayer.Prayer_conmaas_x,gen_x)
  # print(app.prayer.Prayer_conmaas_y,gen_y)
  # print("")
  return gen_x,gen_y




# モブ_黒_レーザー
def mob_beam_bluk(app,GS,name):  
  if app.character[name].Initialization == True:
    app.character[name].Initialization = False
    app.BGM_create("nc425826_ビーム音","音声素材/敵エフェクト/nc425826_ビーム音.wav")
    app.BGM_volume("nc425826_ビーム音",20)
  app.SE_play("nc425826_ビーム音")
  
  app.character[name].memori_1 += 1
  if 5 <= app.character[name].memori_1:
    app.Crank_up_Character(name)
    # print(app.character)
    app.BGM_memory_delete("nc425826_ビーム音")

  
  
def mob_beam_bluk_effect(app,GS,name,move_map_x,move_map_y):
  gen_x,gen_y = origin(app,GS)
  
  dis_x = app.character[name].Character_conmaas_x - gen_x
  dis_y = app.character[name].Character_conmaas_y - gen_y  
  # print(name)
  
  if app.character[name].before_key == "":
    imag = "護符_W"
  elif app.character[name].before_key == "W":
    imag = "護符_W"
  elif app.character[name].before_key == "A":
    imag = "護符_A"
  elif app.character[name].before_key == "S":
    imag = "護符_S"
  elif app.character[name].before_key == "D":
    imag = "護符_D"
    
  app.set_color(0)
  if app.character[name].before_key == "":
    pass
  elif app.character[name].before_key == "W":
    x = move_map_x
    y = move_map_y
    for i in range(app.character[name].memori_1):
      if app.character[name].memori_1%2 == 0 and app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y-i == app.prayer.Prayer_conmaas_y:
        app.prayer_damage(50+app.prayer.defence) 
           
      if i == 0:
        app.image_rect_animation_fps_setting_free_size(imag,5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y ,0,23) 
      elif i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y-i ,0,23 , 1)
      else:
        app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y-i, 5+dis_x,0+dis_y-i ,0,23 , 1)
        
  elif app.character[name].before_key == "S":
    x = move_map_x
    y = move_map_y
    for i in range(app.character[name].memori_1):
      if app.character[name].memori_1%2 == 0 and app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y+i == app.prayer.Prayer_conmaas_y:
          app.prayer_damage(50+app.prayer.defence) 
           
      if i == 0:
        app.image_rect_animation_fps_setting_free_size(imag,5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y ,0,23) 
      elif i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y+i ,0,23 , 1)
      else:
        app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y+i, 5+dis_x,0+dis_y+i ,0,23 , 1)
        
  elif app.character[name].before_key == "A":
    x = move_map_x
    y = move_map_y
    for i in range(app.character[name].memori_1):
      if app.character[name].memori_1%2 == 0 and app.character[name].Character_conmaas_x-i == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y:
          app.prayer_damage(50+app.prayer.defence) 
           
      if i == 0:
        app.image_rect_animation_fps_setting_free_size(imag,5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y ,0,23) 
      elif i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y, 5+dis_x-i,0+dis_y ,0,23 , 1)
      else:
        app.rect_animation_fps_setting(5+dis_x-x-i,0+dis_y-y, 5+dis_x-i,0+dis_y ,0,23 , 1)
  
  elif app.character[name].before_key == "D":
    x = move_map_x
    y = move_map_y
    for i in range(app.character[name].memori_1):
      if app.character[name].memori_1%2 == 0 and app.character[name].Character_conmaas_x+i == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y:
          app.prayer_damage(50+app.prayer.defence) 
           
      if i == 0:
        app.image_rect_animation_fps_setting_free_size(imag,5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y ,0,23) 
      elif i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y, 5+dis_x+i,0+dis_y ,0,23 , 1)
      else:
        app.rect_animation_fps_setting(5+dis_x-x+i,0+dis_y-y, 5+dis_x+i,0+dis_y ,0,23 , 1)
        
        


# モブ_白_レーザー
def mob_beam_white(app,GS,name):  
  if app.character[name].Initialization == True:
    app.character[name].Initialization = False
    app.BGM_create("nc425826_ビーム音","音声素材/敵エフェクト/nc425826_ビーム音.wav")
    app.BGM_volume("nc425826_ビーム音",20)
  app.SE_play("nc425826_ビーム音")
  
  app.character[name].memori_1 += 1
  if 5 <= app.character[name].memori_1:
    app.Crank_up_Character(name)
    # print(app.character)
    app.BGM_memory_delete("nc425826_ビーム音")

  
  
def mob_beam_white_effect(app,GS,name,move_map_x,move_map_y):
  gen_x,gen_y = origin(app,GS)
  
  dis_x = app.character[name].Character_conmaas_x - gen_x
  dis_y = app.character[name].Character_conmaas_y - gen_y  
  # print(name)
  
  if app.character[name].before_key == "":
    imag = "護符_W"
  elif app.character[name].before_key == "W":
    imag = "護符_W"
  elif app.character[name].before_key == "A":
    imag = "護符_A"
  elif app.character[name].before_key == "S":
    imag = "護符_S"
  elif app.character[name].before_key == "D":
    imag = "護符_D"
    
  app.set_color(255)

  if True:
    x = move_map_x
    y = move_map_y
    for i in range(app.character[name].memori_1):
      if app.character[name].memori_1%2 == 0 and app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y-i == app.prayer.Prayer_conmaas_y:
        app.prayer_damage(50+app.prayer.defence) 
           
      if i == 0:
        app.image_rect_animation_fps_setting_free_size(imag,5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y ,0,23) 
      elif i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y-i ,0,23 , 1)
      else:
        app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y-i, 5+dis_x,0+dis_y-i ,0,23 , 1)
        

    x = move_map_x
    y = move_map_y
    for i in range(app.character[name].memori_1):
      if app.character[name].memori_1%2 == 0 and app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y+i == app.prayer.Prayer_conmaas_y:
          app.prayer_damage(50+app.prayer.defence) 
           
      if i == 0:
        app.image_rect_animation_fps_setting_free_size(imag,5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y ,0,23) 
      elif i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y+i ,0,23 , 1)
      else:
        app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y+i, 5+dis_x,0+dis_y+i ,0,23 , 1)
        

    x = move_map_x
    y = move_map_y
    for i in range(app.character[name].memori_1):
      if app.character[name].memori_1%2 == 0 and app.character[name].Character_conmaas_x-i == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y:
          app.prayer_damage(50+app.prayer.defence) 
           
      if i == 0:
        app.image_rect_animation_fps_setting_free_size(imag,5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y ,0,23) 
      elif i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y, 5+dis_x-i,0+dis_y ,0,23 , 1)
      else:
        app.rect_animation_fps_setting(5+dis_x-x-i,0+dis_y-y, 5+dis_x-i,0+dis_y ,0,23 , 1)
  

    x = move_map_x
    y = move_map_y
    for i in range(app.character[name].memori_1):
      if app.character[name].memori_1%2 == 0 and app.character[name].Character_conmaas_x+i == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y:
          app.prayer_damage(50+app.prayer.defence) 
           
      if i == 0:
        app.image_rect_animation_fps_setting_free_size(imag,5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y ,0,23) 
      elif i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y, 5+dis_x+i,0+dis_y ,0,23 , 1)
      else:
        app.rect_animation_fps_setting(5+dis_x-x+i,0+dis_y-y, 5+dis_x+i,0+dis_y ,0,23 , 1)
        
    
    
        
# 爆発
def mob_bom(app,GS,name):  
  if app.character[name].Initialization == True:
    app.character[name].Initialization = False
  if 11 <= app.character[name].memori_1:
    app.SE_play("爆発音_ehu")
  
  app.character[name].memori_1 += 1
  if 13 <= app.character[name].memori_1:
    app.Crank_up_Character(name)
    # print(app.character)

    
    
def under_mob_bom_effect(app,GS,name,move_map_x,move_map_y):
  gen_x,gen_y = origin(app,GS)
  
  dis_x = app.character[name].Character_conmaas_x - gen_x
  dis_y = app.character[name].Character_conmaas_y - gen_y  
  
  x = move_map_x
  y = move_map_y
  
  app.set_color(242,102,81)
  
  # if app.character[name].memori_1 <= 2:
  #   for x_ in range(app.character[name].memori_1):
  #     for y_ in range(app.character[name].memori_1):
  #       move_x = x_ - 
  #       move_y = y_
  if app.character[name].memori_1 <= 1:
    app.rect_animation_fps_setting(5+dis_x-x,0+dis_y-y, 5+dis_x,0+dis_y ,0,23 , 1)
  elif app.character[name].memori_1 <= 5:
    app.rect_animation_fps_setting(5+dis_x-x-1,0+dis_y-y-1, 5+dis_x-1,0+dis_y-1 ,0,23 , 3) 
  elif app.character[name].memori_1 <= 10:
    app.rect_animation_fps_setting(5+dis_x-x-2,0+dis_y-y-2, 5+dis_x-2,0+dis_y-2 ,0,23 , 5) 
  
  
def mob_bom_effect(app,GS,name,move_map_x,move_map_y):
  gen_x,gen_y = origin(app,GS)
  
  dis_x = app.character[name].Character_conmaas_x - gen_x
  dis_y = app.character[name].Character_conmaas_y - gen_y  
  
  x = move_map_x
  y = move_map_y
  
  app.set_color(255,255,0)

  if 11 <= app.character[name].memori_1:
    app.rect_animation_fps_setting(5+dis_x-x-2,0+dis_y-y-2, 5+dis_x-2,0+dis_y-2 ,0,23 , 5) 
  
  for x in range(5):
    for y in range(5):
      i = x - 2
      n = y - 2
      if app.character[name].Character_conmaas_x-i == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y-n == app.prayer.Prayer_conmaas_y:
        if 11 <= app.character[name].memori_1:
          app.prayer_damage(100+app.prayer.defence) 