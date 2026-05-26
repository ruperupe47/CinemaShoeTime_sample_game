
import player_cons
import random
import enmy_efect_dis

def damage(app, GS, key, damage):
    now_x = app.prayer.Prayer_conmaas_x
    now_y = app.prayer.Prayer_conmaas_y  
    break_bool = False

    dirs = [
        (-1, 0),  # 0: 左 (A)
        (1, 0),   # 1: 右 (D)
        (0, -1),  # 2: 上 (W)
        (0, 1)    # 3: 下 (S)
    ]
    
    if key < 0 or key >= len(dirs):
        return
        
    dx, dy = dirs[key]

    for i in range(1):
        target_x = now_x + dx * (i + 1)
        target_y = now_y + dy * (i + 1)
        
        if not (0 <= target_y < len(GS.map_data) and 0 <= target_x < len(GS.map_data[0])):
            continue

        for n in range(len(GS.mob)):
            if GS.mob[n][1][0] == target_x and GS.mob[n][1][1] == target_y:
                break_bool = True
                app.Character_damage(GS.mob[n][0], damage)
                
        for n in range(len(GS.before_mob)):
            if GS.before_mob[n][1][0] == target_x and GS.before_mob[n][1][1] == target_y:
                break_bool = True
                app.Character_damage(GS.before_mob[n][0], damage)
                
        for n in range(len(GS.bos)):
            if GS.bos[n][1][0] == target_x and GS.bos[n][1][1] == target_y:
                break_bool = True
                app.Character_damage(GS.bos[n][0], damage)
                break          

        
        if break_bool:
            break
            
        tile = GS.map_data[target_y][target_x]
        
        if tile == [2, ['岩']]:
            GS.map_data[target_y][target_x] = [2, ['地面']]
            
        elif tile == [2, ['レンガ']] and 30 <= GS.efficiency_meter:
            GS.map_data[target_y][target_x] = [2, ['地面']]     
            
        elif tile == [2, ['シルバーレンガ']] and 50 <= GS.efficiency_meter:
            GS.map_data[target_y][target_x] = [2, ['地面']]  
  
  
def count_damage(app, GS, key, damage,count,cx=0,cy=0):
    now_x = app.prayer.Prayer_conmaas_x
    now_y = app.prayer.Prayer_conmaas_y  
    break_bool = False

    dirs = [
        (-1, 0),  # 0: 左 (A)
        (1, 0),   # 1: 右 (D)
        (0, -1),  # 2: 上 (W)
        (0, 1)    # 3: 下 (S)
    ]
    
    if key < 0 or key >= len(dirs):
        return
        
    dx, dy = dirs[key]

    for i in range(count):
        target_x = now_x + dx * (i + 1)+cx
        target_y = now_y + dy * (i + 1)+cy
        
        if not (0 <= target_y < len(GS.map_data) and 0 <= target_x < len(GS.map_data[0])):
            continue

        for n in range(len(GS.mob)):
            if GS.mob[n][1][0] == target_x and GS.mob[n][1][1] == target_y:
                break_bool = True
                app.Character_damage(GS.mob[n][0], damage)
                
        for n in range(len(GS.before_mob)):
            if GS.before_mob[n][1][0] == target_x and GS.before_mob[n][1][1] == target_y:
                break_bool = True
                app.Character_damage(GS.before_mob[n][0], damage)
                
        for n in range(len(GS.bos)):
            if GS.bos[n][1][0] == target_x and GS.bos[n][1][1] == target_y:
                break_bool = True
                app.Character_damage(GS.bos[n][0], damage)
                break          
        
        if break_bool:
            break
            
        tile = GS.map_data[target_y][target_x]
        
        if tile == [2, ['岩']]:
            GS.map_data[target_y][target_x] = [2, ['地面']]
            
        elif tile == [2, ['レンガ']] and 30 <= GS.efficiency_meter:
            GS.map_data[target_y][target_x] = [2, ['地面']]     
            
        elif tile == [2, ['シルバーレンガ']] and 50 <= GS.efficiency_meter:
            GS.map_data[target_y][target_x] = [2, ['地面']]  
            
              
# 座標計算
def dis_pl(app,GS):
  if app.prayer.Prayer_conmaas_x <= 17:
    dis_x = app.prayer.Prayer_conmaas_x
  elif app.prayer.Prayer_conmaas_x <= 189:
    dis_x = 17
  elif app.prayer.Prayer_conmaas_x <= 203:
    dis_x = app.prayer.Prayer_conmaas_x - 173    
  else:
    dis_x = app.prayer.Prayer_conmaas_x - 173
    
  if app.prayer.Prayer_conmaas_y <= 10:    
    dis_y = app.prayer.Prayer_conmaas_y
  elif app.prayer.Prayer_conmaas_y <= 290:
    dis_y = 11
  else:
    dis_y = app.prayer.Prayer_conmaas_y - 280

  return dis_x,dis_y 
      
    
# エフェクト系統の描写
def under_efect_display(app,GS,move_map_x,move_map_y):
  for name,obj in app.character.items():
    if "モブ_ボム" in name:
      enmy_efect_dis.under_mob_bom_effect(app,GS,name,move_map_x,move_map_y)
  
       
# エフェクト系統の描写
def efect_display(app,GS,move_map_x,move_map_y):
  for name,obj in app.character.items():
    if "ビーム" in name:
      beam_effect(app,GS,name)
    elif "ブーメラン" in name:
      bumerann_effect(app,GS,name)
    elif "カッター" in name:
      cuter_effect(app,GS,name)
    elif "切り" in name:
      cut_effect(app,GS,name)
      
    elif "ミサイル" in name:
      misairu_effect(app,GS,name)
    elif "ハリケーン" in name:
      hariken_effect(app,GS,name)
    elif "トルネード" in name:
      toruned_effect(app,GS,name)  
    elif "ドリル切り" in name:
      dorirucut_effect(app,GS,name)  

    elif "おろし" in name:
      orosi_effect(app,GS,name)
    elif "クラスター" in name:
      misairuran_effect(app,GS,name)
    elif "ロケット" in name:
      rocket_effect(app,GS,name)  
    elif "パンチ" in name:
      panti_effect(app,GS,name)   
      
    elif "モブ_黒_レーザー" in name:
      enmy_efect_dis.mob_beam_bluk_effect(app,GS,name,move_map_x,move_map_y)
    elif "モブ_白_レーザー" in name:
      enmy_efect_dis.mob_beam_white_effect(app,GS,name,move_map_x,move_map_y)
    elif "モブ_ボム" in name:
      enmy_efect_dis.mob_bom_effect(app,GS,name,move_map_x,move_map_y)






# ビーム
def beam(app,GS,name):
  GS.lock = True
  GS.beam = True
  app.prayer.hyper_muteki = True
  
  if app.character[name].Initialization == True:
    pp = random.randint(0,2)
    if pp == 0:
      app.SE_play("エンペラー_1_1")
    elif pp == 1:
      app.SE_play("エンペラー_1_2")
    else:
      app.SE_play("エンペラー_1_3")
    app.character[name].Initialization = False
    app.BGM_create("戦艦系砲弾音","音声素材/エフェクト/nc417019_戦艦系砲弾音.wav")
    app.BGM_volume("戦艦系砲弾音",30)
            
  app.BGM_play("戦艦系砲弾音")
  if GS.Peeled == 0:
    key  = 0
    # count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,-1,0)
    # count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,1,0)
    count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,0,-1)
    count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,0,0)
    count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,0,1)
  elif GS.Peeled == 1:
    key  = 1
    # count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,-1,0)
    # count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,1,0)
    count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,0,-1)
    count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,0,0)
    count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,0,1)
  elif GS.Peeled == 2:
    key  = 2
    # count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,0,0)
    # count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,0,1)
    count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,-1,0)
    count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,0,0)
    count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,1,0)
  elif GS.Peeled == 3:
    key  = 3
    # count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,0,0)
    # count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,0,1)
    count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,-1,0)
    count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,0,0)
    count_damage(app, GS, key, (20+GS.plus_damage)*3,app.character[name].memori_1,1,0)
  
  app.character[name].memori_1 += 1
  if 20 <= app.character[name].memori_1:
    GS.clock_1 = 0
    GS.beam = False
    app.BGM_memory_delete("戦艦系砲弾音")
    GS.enrgy_flag = True

  if 20 <= app.character[name].memori_1:    
    app.Crank_up_Character(name)
    print(app.character)
    app.prayer.hyper_muteki = False   
    GS.lock = False
    app.character[name].memori_1 = 0


def beam_effect(app,GS,name):    
  app.character[name].memori_1 += 1
  if GS.Peeled == 0:
    x = -1
    y = 0
  elif GS.Peeled == 1:
    x = 1
    y = 0
  elif GS.Peeled == 2:
    x = 0
    y = -1
  elif GS.Peeled == 3:
    x = 0
    y = 1
    
  app.set_color(0,255,50)
  dis_x,dis_y = dis_pl(app,GS)
  for i in range(app.character[name].memori_1):
    if GS.Peeled == 0:
      if i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y-1, 5+dis_x+x-i,0+dis_y+y-1 ,0,23 , 1) 
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y, 5+dis_x+x-i,0+dis_y+y ,0,23 , 1) 
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y+1, 5+dis_x+x-i,0+dis_y+y+1 ,0,23 , 1) 
      else:
        app.rect_animation_fps_setting(5+dis_x+x-i,0+dis_y+y-1, 5+dis_x+x-i,0+dis_y+y-1 ,0,23 , 1) 
        app.rect_animation_fps_setting(5+dis_x+x-i,0+dis_y+y, 5+dis_x+x-i,0+dis_y+y ,0,23 , 1) 
        app.rect_animation_fps_setting(5+dis_x+x-i,0+dis_y+y+1, 5+dis_x+x-i,0+dis_y+y+1 ,0,23 , 1) 
    elif GS.Peeled == 1:
      if i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y-1, 5+dis_x+x+i,0+dis_y+y-1 ,0,23 , 1) 
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y, 5+dis_x+x+i,0+dis_y+y ,0,23 , 1) 
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y+1, 5+dis_x+x+i,0+dis_y+y+1 ,0,23 , 1) 
      else:
        app.rect_animation_fps_setting(5+dis_x+x+i,0+dis_y+y-1, 5+dis_x+x+i,0+dis_y+y-1 ,0,23 , 1) 
        app.rect_animation_fps_setting(5+dis_x+x+i,0+dis_y+y, 5+dis_x+x+i,0+dis_y+y ,0,23 , 1)    
        app.rect_animation_fps_setting(5+dis_x+x+i,0+dis_y+y+1, 5+dis_x+x+i,0+dis_y+y+1,0,23 , 1)      
    elif GS.Peeled == 2:
      if i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x+x-1,0+dis_y+y, 5+dis_x+x-1,0+dis_y+y-i,0,23 , 1) 
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y, 5+dis_x+x,0+dis_y+y-i ,0,23 , 1) 
        app.rect_animation_fps_setting(5+dis_x+x+1,0+dis_y+y, 5+dis_x+x+1,0+dis_y+y-i ,0,23 , 1) 
      else:
        app.rect_animation_fps_setting(5+dis_x+x-1,0+dis_y+y-i, 5+dis_x+x-1,0+dis_y+y-i,0,23 , 1)     
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y-i, 5+dis_x+x,0+dis_y+y-i ,0,23 , 1) 
        app.rect_animation_fps_setting(5+dis_x+x+1,0+dis_y+y-i, 5+dis_x+x+1,0+dis_y+y-i,0,23 , 1)         
    elif GS.Peeled == 3:
      if i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x+x-1,0+dis_y+y, 5+dis_x+x-1,0+dis_y+y+i ,0,23 , 1) 
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y, 5+dis_x+x,0+dis_y+y+i ,0,23 , 1) 
        app.rect_animation_fps_setting(5+dis_x+x+1,0+dis_y+y, 5+dis_x+x+1,0+dis_y+y+i ,0,23 , 1) 
      else:
        app.rect_animation_fps_setting(5+dis_x+x-1,0+dis_y+y+i, 5+dis_x+x-1,0+dis_y+y+i ,0,23 , 1)         
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y+i, 5+dis_x+x,0+dis_y+y+i ,0,23 , 1)   
        app.rect_animation_fps_setting(5+dis_x+x+1,0+dis_y+y+i, 5+dis_x+x+1,0+dis_y+y+i ,0,23 , 1)               



# ブーメラン
def bumerann(app,GS,name):
  GS.lock = True
  GS.bumerann_en = True
  app.prayer.hyper_muteki = True
  if app.character[name].Initialization == True:
    pp = random.randint(0,3)
    if pp == 0:
      app.SE_play("エンペラー_2_1")
    elif pp == 1:
      app.SE_play("エンペラー_2_2")
    elif pp == 2:
      app.SE_play("エンペラー_2_3")
    else:
      app.SE_play("エンペラー_2_4")
      
    app.character[name].Initialization = False
    app.BGM_create("ブーメラン","音声素材/エフェクト/nc133514_【効果音ラボ】ブーメラン.mp3")
    app.BGM_volume("ブーメラン",30)
  app.BGM_play("ブーメラン")
    
  if 1 <= app.character[name].memori_1:
    GS.lock = False
  
  if GS.Peeled == 0:
    key  = 0
    count_damage(app, GS, key, 20+GS.plus_damage,1,-app.character[name].memori_1-1,-1)
    count_damage(app, GS, key, 20+GS.plus_damage,1,-app.character[name].memori_1-1,1)
  elif GS.Peeled == 1:
    key  = 1
    count_damage(app, GS, key, 20+GS.plus_damage,1,app.character[name].memori_1-1,-1)
    count_damage(app, GS, key, 20+GS.plus_damage,1,app.character[name].memori_1-1,1)
  elif GS.Peeled == 2:
    key  = 2
    count_damage(app, GS, key, 20+GS.plus_damage,1,-1,-app.character[name].memori_1-1)
    count_damage(app, GS, key, 20+GS.plus_damage,1,1,-app.character[name].memori_1-1)
  elif GS.Peeled == 3:
    key  = 3
    count_damage(app, GS, key, 20+GS.plus_damage,1,-1,app.character[name].memori_1-1)
    count_damage(app, GS, key, 20+GS.plus_damage,1,1,app.character[name].memori_1-1)
  
    
  if 10 <= app.character[name].memori_1:
    GS.clock_2 = 0
    GS.lock = False
    GS.bumerann_en = False
    app.Crank_up_Character(name)
    print(app.character)
    app.BGM_memory_delete("ブーメラン")
    GS.enrgy_flag = True
    app.prayer.hyper_muteki = False   
     
     
def bumerann_effect(app,GS,name):
  app.character[name].memori_1 += 1
  
  dis_x,dis_y = dis_pl(app,GS)
  if app.character[name].memori_1 == 1:
    if GS.Peeled == 0:
      app.character[name].memori_2 = 1
      app.character[name].memori_3 = 0
      app.character[name].memori_4 = 0
    elif GS.Peeled == 1:
      app.character[name].memori_2 = -1
      app.character[name].memori_3 = 0  
      app.character[name].memori_4 = 1    
    elif GS.Peeled == 2:
      app.character[name].memori_2 = 0
      app.character[name].memori_3 = 1    
      app.character[name].memori_4 = 2 
    elif GS.Peeled == 3:
      app.character[name].memori_2 = 0
      app.character[name].memori_3 = -1  
      app.character[name].memori_4 = 3         
      
  x = app.character[name].memori_2
  y = app.character[name].memori_3
  
  if app.character[name].memori_2 == 1:
    move_x = -(app.character[name].memori_1) + 1
    ani_x = -1
    y_1 = -1
    y_2 = 1
    move_y = 0
    ani_y = 0
    x_1 = 0
    x_2 = 0
  elif app.character[name].memori_2 == -1:
    move_x = app.character[name].memori_1 -1
    ani_x = 1
    y_1 = -1
    y_2 = 1
    move_y = 0
    ani_y = 0
    x_1 = 0
    x_2 = 0
  elif app.character[name].memori_3 == 1:
    move_x = 0
    ani_x = 0
    y_1 = 0
    y_2 = 0
    move_y = -(app.character[name].memori_1) + 1
    ani_y = -1
    x_1 = 1
    x_2 = -1
  elif app.character[name].memori_3 == -1:
    move_x = 0
    ani_x = 0
    y_1 = 0
    y_2 = 0
    move_y = app.character[name].memori_1 -1
    ani_y = 1
    x_1 = 1
    x_2 = -1
       
       
  if app.character[name].memori_4 == 0:
    imag_1 = "右鎌_A"
    imag_2 = "右鎌_D"
    app.character[name].memori_4 = 1
  elif app.character[name].memori_4 == 1:
    imag_1 = "右鎌_W"
    imag_2 = "右鎌_S"
    app.character[name].memori_4 =2
  elif app.character[name].memori_4 == 2:
    imag_1 = "右鎌_D"
    imag_2 = "右鎌_A"
    app.character[name].memori_4 =3
  elif app.character[name].memori_4 == 3:
    imag_1 = "右鎌_S"
    imag_2 = "右鎌_W"
    app.character[name].memori_4 =0


  app.image_rect_animation_fps_setting_free_size(imag_1,5+dis_x-x+move_x+x_1,0+dis_y-y+move_y+y_1, 5+dis_x-x+move_x+ani_x+x_1,0+dis_y-y+move_y+y_1+ani_y ,0,23)     
  app.image_rect_animation_fps_setting_free_size(imag_2,5+dis_x-x+move_x+x_2,0+dis_y-y+move_y+y_2, 5+dis_x-x+move_x+ani_x+x_2,0+dis_y-y+move_y+y_2+ani_y ,0,23)      
  
  
# カッター
def cuter(app,GS,name):
  GS.lock = True
  GS.cuter_en = True
  if app.character[name].Initialization == True:
    pp = random.randint(0,2)
    if pp == 0:
      app.SE_play("エンペラー_3_1")
    elif pp == 1:
      app.SE_play("エンペラー_3_2")
    else:
      app.SE_play("エンペラー_3_3")
      
    app.character[name].Initialization = False
    app.BGM_create("高速移動","音声素材/エフェクト/nc478417_高速移動する音【効果音】.mp3")
    app.BGM_volume("高速移動",30)
  app.BGM_play("高速移動")
  app.prayer.hyper_muteki = True
  
  if GS.Peeled == 0:
    key  = 0
  elif GS.Peeled == 1:
    key  = 1
  elif GS.Peeled == 2:
    key  = 2
  elif GS.Peeled == 3:
    key  = 3
  
  damage(app,GS,key,20+GS.plus_damage)       
  now_x = app.prayer.Prayer_conmaas_x
  now_y = app.prayer.Prayer_conmaas_y

  break_bool = False
  
  count = 2
  if key == 0:# 左,A
      for i in range(count):
        A_tile = GS.map_data[now_y][now_x-i-1]
        if A_tile != [1, [(175, 223, 228)]] and A_tile != [2, ['レンガ']] and A_tile != [2, ['シルバーレンガ']] and A_tile != [2, ['岩']]:    
          # for n in range(len(GS.mob)):
          #   if GS.mob[n][1][0] == now_x-i-1 and GS.mob[n][1][1] == now_y:
          #     break_bool = True
          #     break
          # for n in range(len(GS.bos)):
          #   if GS.bos[n][1][0] == now_x-i-1 and GS.bos[n][1][1] == now_y:
          #     break_bool = True
          #     break          
          # if break_bool == True:
          #   break
          app.prayer.Prayer_conmaas_x -= 1
          app.prayer.memori_1 -= 1
        else:
          break
  elif key == 1:# 右,D
      for i in range(count):
         D_tile = GS.map_data[now_y][now_x+i+1]
         if D_tile != [1, [(175, 223, 228)]] and D_tile != [2, ['レンガ']] and D_tile != [2, ['シルバーレンガ']] and D_tile != [2, ['岩']]:
          # for n in range(len(GS.mob)):
          #   if GS.mob[n][1][0] == now_x+i+1 and GS.mob[n][1][1] == now_y:
          #     break_bool = True
          #     break
          # for n in range(len(GS.bos)):
          #   if GS.bos[n][1][0] == now_x+i+1 and GS.bos[n][1][1] == now_y:
          #     break_bool = True
          #     break          
          # if break_bool == True:
          #   break
          app.prayer.Prayer_conmaas_x += 1
          app.prayer.memori_1 += 1
         else:
          break
  elif key == 2:# 上,W 
      for i in range(count):
        W_tile = GS.map_data[now_y-i-1][now_x]
        if W_tile != [1, [(175, 223, 228)]] and W_tile != [2, ['レンガ']] and W_tile != [2, ['シルバーレンガ']] and W_tile != [2, ['岩']]:
          # for n in range(len(GS.mob)):
          #   if GS.mob[n][1][0] == now_x and GS.mob[n][1][1] == now_y-i-1:
          #     break_bool = True
          #     break
          # for n in range(len(GS.bos)):
          #   if GS.bos[n][1][0] == now_x and GS.bos[n][1][1] == now_y-i-1:
          #     break_bool = True
          #     break          
          # if break_bool == True:
          #   break          
          app.prayer.Prayer_conmaas_y -= 1
          app.prayer.memori_2 -= 1
        else:
          break
  elif key == 3:# 下,S 
      for i in range(count):
        S_tile = GS.map_data[now_y+i+1][now_x]
        if S_tile != [1, [(175, 223, 228)]] and S_tile != [2, ['レンガ']] and S_tile != [2, ['シルバーレンガ']] and S_tile != [2, ['岩']]:
          # for n in range(len(GS.mob)):
          #   if GS.mob[n][1][0] == now_x and GS.mob[n][1][1] == now_y+i+1:
          #     break_bool = True
          #     break
          # for n in range(len(GS.bos)):
          #   if GS.bos[n][1][0] == now_x and GS.bos[n][1][1] == now_y+i+1:
          #     break_bool = True
          #     break          
          # if break_bool == True:
          #   break
          app.prayer.Prayer_conmaas_y += 1
          app.prayer.memori_2 += 1
        else:
          break

    
  if 10 <= app.character[name].memori_1:
    GS.clock_3 = 0
    GS.lock = False
    GS.cuter_en = False
    app.Crank_up_Character(name)
    print(app.character)
    app.BGM_memory_delete("高速移動")
    GS.enrgy_flag = True
    app.prayer.hyper_muteki = False
    
    
def cuter_effect(app,GS,name):
  app.character[name].memori_1 += 1


# 切り
def cut(app,GS,name):
  GS.lock = True
  GS.cut_en = True
  if app.character[name].Initialization == True:
    pp = random.randint(0,2)
    if pp == 0:
      app.SE_play("エンペラー_4_1")
    elif pp == 1:
      app.SE_play("エンペラー_4_2")
    else:
      app.SE_play("エンペラー_4_3")
    app.character[name].Initialization = False
    app.BGM_create("斬撃","音声素材/エフェクト/nc306909_ザクッと鋭い斬撃.wav")
    app.BGM_volume("斬撃",30)
  app.BGM_play("斬撃")
  app.prayer.hyper_muteki = True
  GS.lock = False
  if GS.Peeled == 0:
    key  = 0
  elif GS.Peeled == 1:
    key  = 1
  elif GS.Peeled == 2:
    key  = 2
  elif GS.Peeled == 3:
    key  = 3
    
  
  damage(app,GS,key,40+GS.plus_damage)       
  
  if 2 <= app.character[name].memori_1:
    GS.clock_4 = 0
    GS.lock = False
    GS.cut_en = False
    app.Crank_up_Character(name)
    print(app.character)
    app.BGM_memory_delete("斬撃")
    GS.enrgy_flag = True
    app.prayer.hyper_muteki = False


def cut_effect(app,GS,name):
  app.character[name].memori_1 += 1
  





# ミサイル        
def misairu(app,GS,name):
  GS.lock = True
  GS.misairu_ka = True
  if app.character[name].Initialization == True:
    pp = random.randint(0,99)
    if pp == 0:
      app.SE_play("カイザー_1_3")
    elif pp == 1:
      app.SE_play("カイザー_1_2")
    else:
      app.SE_play("カイザー_1_1")
      
    app.character[name].Initialization = False
    app.BGM_create("ミサイル","音声素材/エフェクト/nc439592_攻撃魔法・ミサイル系爆発音４.wav")
    app.BGM_volume("ミサイル",30)
  app.BGM_play("ミサイル") 
  app.prayer.hyper_muteki = True 
  
  if GS.Peeled == 0:
    key  = 0
    count_damage(app, GS, key, 10+GS.plus_damage,1,-app.character[name].memori_1-1,0)
  elif GS.Peeled == 1:
    key  = 1
    count_damage(app, GS, key, 10+GS.plus_damage,1,app.character[name].memori_1-1,0)
  elif GS.Peeled == 2:
    key  = 2
    count_damage(app, GS, key, 10+GS.plus_damage,1,0,-app.character[name].memori_1-1)
  elif GS.Peeled == 3:
    key  = 3
    count_damage(app, GS, key, 10+GS.plus_damage,1,0,app.character[name].memori_1-1) 
  
  if 2 <= app.character[name].memori_1:
    GS.lock = False
    GS.enrgy_flag = True
    app.prayer.hyper_muteki = False
  
  if 10 <= app.character[name].memori_1:
    GS.clock_2 = 0
    GS.lock = False
    GS.misairu_ka = False
    app.Crank_up_Character(name)
    print(app.character)
    app.BGM_memory_delete("ミサイル")
    GS.enrgy_flag = True
    app.prayer.hyper_muteki = False
     
     
def misairu_effect(app,GS,name):
  app.character[name].memori_1 += 1
  
  dis_x,dis_y = dis_pl(app,GS)
  if app.character[name].memori_1 == 1:
    if GS.Peeled == 0:
      app.character[name].memori_2 = 1
      app.character[name].memori_3 = 0
      app.character[name].memori_4 = 0
    elif GS.Peeled == 1:
      app.character[name].memori_2 = -1
      app.character[name].memori_3 = 0  
      app.character[name].memori_4 = 1    
    elif GS.Peeled == 2:
      app.character[name].memori_2 = 0
      app.character[name].memori_3 = 1    
      app.character[name].memori_4 = 2 
    elif GS.Peeled == 3:
      app.character[name].memori_2 = 0
      app.character[name].memori_3 = -1  
      app.character[name].memori_4 = 3             
      
  x = app.character[name].memori_2
  y = app.character[name].memori_3
  
  if app.character[name].memori_2 == 1:
    move_x = -(app.character[name].memori_1) + 1
    ani_x = -1
    y_1 = 0
    move_y = 0
    ani_y = 0
    x_1 = 0
  elif app.character[name].memori_2 == -1:
    move_x = app.character[name].memori_1 -1
    ani_x = 1
    y_1 =0
    move_y = 0
    ani_y = 0
    x_1 = 0
  elif app.character[name].memori_3 == 1:
    move_x = 0
    ani_x = 0
    y_1 = 0
    move_y = -(app.character[name].memori_1) + 1
    ani_y = -1
    x_1 = 0
  elif app.character[name].memori_3 == -1:
    move_x = 0
    ani_x = 0
    y_1 = 0
    move_y = app.character[name].memori_1 -1
    ani_y = 1
    x_1 = 0

  # app.rect_animation_fps_setting(5+dis_x-x+move_x+x_1,0+dis_y-y+move_y+y_1, 5+dis_x-x+move_x+ani_x+x_1,0+dis_y-y+move_y+y_1+ani_y ,0,23, 1)  
  if app.character[name].memori_4 == 0:
    imag_1 = "ドリル_A"
    
  elif app.character[name].memori_4 == 1:
    imag_1 = "ドリル_D"
    
  elif app.character[name].memori_4 == 2:
    imag_1 = "ドリル_W"
    
  elif app.character[name].memori_4 == 3:
    imag_1 = "ドリル_S"

  app.image_rect_animation_fps_setting_free_size(imag_1,5+dis_x-x+move_x+x_1,0+dis_y-y+move_y+y_1, 5+dis_x-x+move_x+ani_x+x_1,0+dis_y-y+move_y+y_1+ani_y ,0,23)  
  


# ハリケーン
def hariken(app,GS,name):
  if app.character[name].Initialization == True:
    pp = random.randint(0,2)
    if pp == 0:
      app.SE_play("カイザー_2_1")
    elif pp == 1:
      app.SE_play("カイザー_2_2")
    else:
      app.SE_play("カイザー_2_3")
    app.character[name].Initialization = False
    app.BGM_create("ハリケーン","音声素材/エフェクト/nc70864_強い風２.mp3")
    app.BGM_volume("ハリケーン",30)
  app.BGM_play("ハリケーン") 
  app.prayer.hyper_muteki = True 
  
  GS.lock = True
  GS.hariken_kai = True
  if 10 <= app.character[name].memori_1:
    GS.clock_1 = 0
    GS.lock = False
    GS.hariken_kai = False
    app.Crank_up_Character(name)
    print(app.character)
    app.BGM_memory_delete("ハリケーン")
    GS.enrgy_flag = True
    app.prayer.hyper_muteki = False


def hariken_effect(app,GS,name):    
  app.character[name].memori_1 += 1
  if GS.Peeled == 0:
    x = -1
    y = 0
  elif GS.Peeled == 1:
    x = 1
    y = 0
  elif GS.Peeled == 2:
    x = 0
    y = -1
  elif GS.Peeled == 3:
    x = 0
    y = 1
  
  app.set_color(255)
  dis_x,dis_y = dis_pl(app,GS)
  for i in range(app.character[name].memori_1):
    if GS.Peeled == 0:
      if i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y, 5+dis_x+x-i,0+dis_y+y ,0,23 , 1)
      else:
        app.rect_animation_fps_setting(5+dis_x+x-i,0+dis_y+y, 5+dis_x+x-i,0+dis_y+y ,0,23 , 1)
    elif GS.Peeled == 1:
      if i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y, 5+dis_x+x+i,0+dis_y+y ,0,23 , 1) 
      else:
        app.rect_animation_fps_setting(5+dis_x+x+i,0+dis_y+y, 5+dis_x+x+i,0+dis_y+y ,0,23 , 1)     
    elif GS.Peeled == 2:
      if i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y, 5+dis_x+x,0+dis_y+y-i ,0,23 , 1) 
      else:
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y-i, 5+dis_x+x,0+dis_y+y-i ,0,23 , 1) 
    elif GS.Peeled == 3:
      if i == app.character[name].memori_1-1:
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y, 5+dis_x+x,0+dis_y+y+i ,0,23 , 1) 
      else:    
        app.rect_animation_fps_setting(5+dis_x+x,0+dis_y+y+i, 5+dis_x+x,0+dis_y+y+i ,0,23 , 1)    
        
  if GS.Peeled == 0:
    key  = 0
    count_damage(app, GS, key, 10+GS.plus_damage,app.character[name].memori_1,0,0)
  elif GS.Peeled == 1:
    key  = 1
    count_damage(app, GS, key, 10+GS.plus_damage,app.character[name].memori_1,0,0)
  elif GS.Peeled == 2:
    key  = 2
    count_damage(app, GS, key, 10+GS.plus_damage,app.character[name].memori_1,0,0)
  elif GS.Peeled == 3:
    key  = 3
    count_damage(app, GS, key, 10+GS.plus_damage,app.character[name].memori_1,0,0) 
        

# トルネード
def toruned(app,GS,name):
  GS.lock = False
  GS.toruned_kai = True
  if app.character[name].Initialization == True:
    pp = random.randint(0,2)
    if pp == 0:
      app.SE_play("カイザー_3_1")
    elif pp == 1:
      app.SE_play("カイザー_3_2")
    else:
      app.SE_play("カイザー_3_3")
    app.character[name].Initialization = False
    app.BGM_create("トルネード","音声素材/エフェクト/nc133698_【効果音ラボ】ドリル.mp3")
    app.BGM_volume("トルネード",30)
  app.BGM_play("トルネード")  
  app.prayer.hyper_muteki = True
  
  if GS.Peeled == 0:
    key  = 0
  elif GS.Peeled == 1:
    key  = 1
  elif GS.Peeled == 2:
    key  = 2
  elif GS.Peeled == 3:
    key  = 3
  
  damage(app,GS,key,10+GS.plus_damage)       
  now_x = app.prayer.Prayer_conmaas_x
  now_y = app.prayer.Prayer_conmaas_y

  break_bool = False
  
  count = 4
  if key == 0:# 左,A
      for i in range(count):
        A_tile = GS.map_data[now_y][now_x-i-1]
        if A_tile != [1, [(175, 223, 228)]] and A_tile != [2, ['レンガ']] and A_tile != [2, ['シルバーレンガ']] and A_tile != [2, ['岩']]:    
          # for n in range(len(GS.mob)):
          #   if GS.mob[n][1][0] == now_x-i-1 and GS.mob[n][1][1] == now_y:
          #     break_bool = True
          #     break
          # for n in range(len(GS.bos)):
          #   if GS.bos[n][1][0] == now_x-i-1 and GS.bos[n][1][1] == now_y:
          #     break_bool = True
          #     break          
          # if break_bool == True:
          #   break
          app.prayer.Prayer_conmaas_x -= 1
          app.prayer.memori_1 -= 1
        else:
          break
  elif key == 1:# 右,D
      for i in range(count):
         D_tile = GS.map_data[now_y][now_x+i+1]
         if D_tile != [1, [(175, 223, 228)]] and D_tile != [2, ['レンガ']] and D_tile != [2, ['シルバーレンガ']] and D_tile != [2, ['岩']]:
          # for n in range(len(GS.mob)):
          #   if GS.mob[n][1][0] == now_x+i+1 and GS.mob[n][1][1] == now_y:
          #     break_bool = True
          #     break
          # for n in range(len(GS.bos)):
          #   if GS.bos[n][1][0] == now_x+i+1 and GS.bos[n][1][1] == now_y:
          #     break_bool = True
          #     break          
          # if break_bool == True:
          #   break
          app.prayer.Prayer_conmaas_x += 1
          app.prayer.memori_1 += 1
         else:
          break
  elif key == 2:# 上,W 
      for i in range(count):
        W_tile = GS.map_data[now_y-i-1][now_x]
        if W_tile != [1, [(175, 223, 228)]] and W_tile != [2, ['レンガ']] and W_tile != [2, ['シルバーレンガ']] and W_tile != [2, ['岩']]:
          # for n in range(len(GS.mob)):
          #   if GS.mob[n][1][0] == now_x and GS.mob[n][1][1] == now_y-i-1:
          #     break_bool = True
          #     break
          # for n in range(len(GS.bos)):
          #   if GS.bos[n][1][0] == now_x and GS.bos[n][1][1] == now_y-i-1:
          #     break_bool = True
          #     break          
          # if break_bool == True:
          #   break          
          app.prayer.Prayer_conmaas_y -= 1
          app.prayer.memori_2 -= 1
        else:
          break
  elif key == 3:# 下,S 
      for i in range(count):
        S_tile = GS.map_data[now_y+i+1][now_x]
        if S_tile != [1, [(175, 223, 228)]] and S_tile != [2, ['レンガ']] and S_tile != [2, ['シルバーレンガ']] and S_tile != [2, ['岩']]:
          # for n in range(len(GS.mob)):
          #   if GS.mob[n][1][0] == now_x and GS.mob[n][1][1] == now_y+i+1:
          #     break_bool = True
          #     break
          # for n in range(len(GS.bos)):
          #   if GS.bos[n][1][0] == now_x and GS.bos[n][1][1] == now_y+i+1:
          #     break_bool = True
          #     break          
          # if break_bool == True:
          #   break
          app.prayer.Prayer_conmaas_y += 1
          app.prayer.memori_2 += 1
        else:
          break
  
  
  if 5 <= app.character[name].memori_1:
    GS.clock_3 = 0
    GS.lock = False
    GS.toruned_kai = False
    app.Crank_up_Character(name)
    print(app.character)
    app.BGM_memory_delete("トルネード")
    GS.enrgy_flag = True
    app.prayer.hyper_muteki = False
    
def toruned_effect(app,GS,name):
  app.character[name].memori_1 += 1       



# ドリル切り
def dorirucut(app,GS,name):
  GS.lock = False
  GS.dorirucut_kai = True
  app.prayer.hyper_muteki = True

  if app.character[name].Initialization == True:
    pp = random.randint(0,30)
    if pp == 0:
      app.SE_play("カイザー_4_3")
    elif pp == 1:
      app.SE_play("カイザー_4_2")
    else:
      app.SE_play("カイザー_4_1")
    app.character[name].Initialization = False
    app.BGM_create("ドリル斬撃","音声素材/エフェクト/nc84890_効果音_ゲーム_ドリル風音源.wav")
    app.BGM_volume("ドリル斬撃",30)
  app.BGM_play("ドリル斬撃")
  
  if GS.Peeled == 0:
    key  = 0
  elif GS.Peeled == 1:
    key  = 1
  elif GS.Peeled == 2:
    key  = 2
  elif GS.Peeled == 3:
    key  = 3
    
    
  num =  random.randint(0,10)
  if num == 3: 
    plu = 3
    app.SE_play("Over Drive")
  else:
     plu = 1 
         
  damage(app,GS,key,(10+GS.plus_damage)*plu)  
  if 1 <= app.character[name].memori_1:
    GS.lock = False
    GS.dorirucut_kai = False
    GS.enrgy_flag = True
    
    
  if 5 <= app.character[name].memori_1:
    GS.clock_4 = 0
    app.Crank_up_Character(name)
    print(app.character)
    app.BGM_memory_delete("ドリル斬撃")
    GS.enrgy_flag = True
    app.prayer.hyper_muteki = False


def dorirucut_effect(app,GS,name):
  app.character[name].memori_1 += 1
  
  


  
# おろし
def orosi(app,GS,name):
  GS.enrgy_flag = False
  GS.lock = True
  GS.orosi_mika = True
  app.prayer.hyper_muteki = True
  if app.character[name].Initialization == True:
    pp = random.randint(0,2)
    if pp == 0:
      app.SE_play("ミカド_1_1")
    elif pp == 1:
      app.SE_play("ミカド_1_2")
    else:
      app.SE_play("ミカド_1_3")
    app.character[name].Initialization = False
    app.BGM_create("おろし","音声素材/エフェクト/nc98571_武器振る音01.wav")
    app.BGM_volume("おろし",80)
  app.BGM_play("おろし")
  
  key = 0
  for x in range(9):
    for y in range(9):
      xt = x -4
      yt = y - 4
      count_damage(app, GS, key, 10+GS.plus_damage,1,xt,yt)
  

  if 10 <= app.character[name].memori_1:
    GS.clock_1 = 0
    GS.lock = False
    GS.orosi_mika = False
    app.Crank_up_Character(name)
    print(app.character)
    app.BGM_memory_delete("おろし")
    GS.enrgy_flag = True
    app.prayer.hyper_muteki = False
     
     
def orosi_effect(app,GS,name):
  app.character[name].memori_1 += 1.
  dis_x,dis_y = dis_pl(app,GS)
    
  for x in range(9):
    for y in range(9):
       xt = x -4
       yt = y - 4
    #  if not(xt == 0 and  yt == 0):
       num = random.randint(0, 3)
       ors = random.randint(1, 2)
       if ors == 1:
         img = "おろし_1"
       elif ors == 2:
         img = "おろし_2"  
              
       if num == 0:
         imag = img+"_W"
       elif num == 1:
         imag = img+"_A"
       elif num ==2:
         imag = img+"_S"
       elif num == 3:
         imag = img+"_D"         
       app.image_rect_animation_fps_setting_free_size(imag,5+dis_x+xt,0+dis_y+yt, 5+dis_x+xt,0+dis_y+yt,0,23)     
       
       
# ミサイル群
def misairuran(app, GS, name):
    GS.lock = True
    GS.misairuran_mika = True
    app.prayer.hyper_muteki = True

    if app.character[name].Initialization == True:
      pp = random.randint(0,2)
      if pp == 0:
        app.SE_play("ミカド_2_1")
      elif pp == 1:
        app.SE_play("ミカド_2_2")
      else:
        app.SE_play("ミカド_2_3")
      app.character[name].Initialization = False
      app.BGM_create("ミサイル群", "音声素材/エフェクト/nc222377_トマホーク巡航ミサイル発射音.mp3")
      app.BGM_volume("ミサイル群", 20)
    app.BGM_play("ミサイル群")  

    if 1 <= app.character[name].memori_1:
        app.character[name].memori_5 = [1, 1, 1]
    
    if 2 <= app.character[name].memori_1:
      GS.lock = False
      # GS.clock_2 = 0
      GS.enrgy_flag = True
      app.prayer.hyper_muteki = False
      
    if 10 <= app.character[name].memori_1:
        GS.lock = False
        GS.misairuran_mika = False
        app.Crank_up_Character(name)
        print(app.character)
        app.BGM_memory_delete("ミサイル群")
        GS.enrgy_flag = True
        app.prayer.hyper_muteki = False
        return
        
    dist = app.character[name].memori_1
    
    key = GS.Peeled
    
    total_damage = 10 + GS.plus_damage

    if key == 0:   
        count_damage(app, GS, key, total_damage, count=1, cx=-dist, cy=-1) 
        count_damage(app, GS, key, total_damage, count=1, cx=-dist, cy=0)  
        count_damage(app, GS, key, total_damage, count=1, cx=-dist, cy=1)  
        
    elif key == 1:  
        count_damage(app, GS, key, total_damage, count=1, cx=dist, cy=-1)  
        count_damage(app, GS, key, total_damage, count=1, cx=dist, cy=0)   
        count_damage(app, GS, key, total_damage, count=1, cx=dist, cy=1)  
        
    elif key == 2: 
        count_damage(app, GS, key, total_damage, count=1, cx=-1, cy=-dist) 
        count_damage(app, GS, key, total_damage, count=1, cx=0,  cy=-dist) 
        count_damage(app, GS, key, total_damage, count=1, cx=1,  cy=-dist) 
        
    elif key == 3:  
        count_damage(app, GS, key, total_damage, count=1, cx=-1, cy=dist)  
        count_damage(app, GS, key, total_damage, count=1, cx=0,  cy=dist)  
        count_damage(app, GS, key, total_damage, count=1, cx=1,  cy=dist)  
     
def misairuran_effect(app,GS,name):
  app.character[name].memori_1 += 1
  if app.character[name].memori_1 == 1:
    return
  
  dis_x,dis_y = dis_pl(app,GS)
  if app.character[name].memori_1 != 1:
    if GS.Peeled == 0:
      app.character[name].memori_2 = 1
      app.character[name].memori_3 = 0
      app.character[name].memori_4 = 0
      takenoko_1_x = 0
      takenoko_2_x = 0
      takenoko_3_x = 0
      takenoko_1_y = -1
      takenoko_2_y = 0
      takenoko_3_y = 1
    elif GS.Peeled == 1:
      app.character[name].memori_2 = -1
      app.character[name].memori_3 = 0  
      app.character[name].memori_4 = 1 
      takenoko_1_x = 0
      takenoko_2_x = 0
      takenoko_3_x = 0
      takenoko_1_y = -1
      takenoko_2_y = 0
      takenoko_3_y = 1  
    elif GS.Peeled == 2:
      app.character[name].memori_2 = 0
      app.character[name].memori_3 = 1    
      app.character[name].memori_4 = 2 
      takenoko_1_x = -1
      takenoko_2_x = 0
      takenoko_3_x = 1
      takenoko_1_y = 0
      takenoko_2_y = 0
      takenoko_3_y = 0
    elif GS.Peeled == 3:
      app.character[name].memori_2 = 0
      app.character[name].memori_3 = -1  
      app.character[name].memori_4 = 3  
      takenoko_1_x = -1
      takenoko_2_x = 0
      takenoko_3_x = 1
      takenoko_1_y = 0
      takenoko_2_y = 0
      takenoko_3_y = 0           
      
  x = app.character[name].memori_2
  y = app.character[name].memori_3
  
  if app.character[name].memori_2 == 1:
    move_x = -(app.character[name].memori_1) + 1
    ani_x = -1
    y_1 = 0
    move_y = 0
    ani_y = 0
    x_1 = 0
  elif app.character[name].memori_2 == -1:
    move_x = app.character[name].memori_1 -1
    ani_x = 1
    y_1 =0
    move_y = 0
    ani_y = 0
    x_1 = 0
  elif app.character[name].memori_3 == 1:
    move_x = 0
    ani_x = 0
    y_1 = 0
    move_y = -(app.character[name].memori_1) + 1
    ani_y = -1
    x_1 = 0
  elif app.character[name].memori_3 == -1:
    move_x = 0
    ani_x = 0
    y_1 = 0
    move_y = app.character[name].memori_1 -1
    ani_y = 1
    x_1 = 0

  # app.rect_animation_fps_setting(5+dis_x-x+move_x+x_1,0+dis_y-y+move_y+y_1, 5+dis_x-x+move_x+ani_x+x_1,0+dis_y-y+move_y+y_1+ani_y ,0,23, 1)  
  if app.character[name].memori_4 == 0:
    imag_1 = "タケノコ_A"
  elif app.character[name].memori_4 == 1:
    imag_1 = "タケノコ_D"
  elif app.character[name].memori_4 == 2:
    imag_1 = "タケノコ_W"
  elif app.character[name].memori_4 == 3:
    imag_1 = "タケノコ_S"
  print(app.character[name].memori_4 )


  if app.character[name].memori_5[0] == 1:
    app.image_rect_animation_fps_setting_free_size(imag_1,5+dis_x-x+move_x+x_1+takenoko_1_x,0+dis_y-y+move_y+y_1+takenoko_1_y, 5+dis_x-x+move_x+ani_x+x_1+takenoko_1_x,0+dis_y-y+move_y+y_1+ani_y+takenoko_1_y ,0,23)  
  if app.character[name].memori_5[1] == 1:
    app.image_rect_animation_fps_setting_free_size(imag_1,5+dis_x-x+move_x+x_1+takenoko_2_x,0+dis_y-y+move_y+y_1+takenoko_2_y, 5+dis_x-x+move_x+ani_x+x_1+takenoko_2_x,0+dis_y-y+move_y+y_1+ani_y+takenoko_2_y ,0,23)  
  if app.character[name].memori_5[2] == 1:
    app.image_rect_animation_fps_setting_free_size(imag_1,5+dis_x-x+move_x+x_1+takenoko_3_x,0+dis_y-y+move_y+y_1+takenoko_3_y, 5+dis_x-x+move_x+ani_x+x_1+takenoko_3_x,0+dis_y-y+move_y+y_1+ani_y+takenoko_3_y ,0,23)    



# ミサイル群
def rocket(app, GS, name):
    GS.lock = True
    GS.rocket_mika = True
    app.prayer.hyper_muteki = True
    
    if app.character[name].Initialization == True:
      pp = random.randint(0,3)
      if pp == 0:
        app.SE_play("ミカド_3_1")
      elif pp == 1:
        app.SE_play("ミカド_3_2")
      elif pp == 2:
        app.SE_play("ミカド_3_3")
      else:
        app.SE_play("ミカド_3_4")
      app.character[name].Initialization = False
      app.BGM_create("ロケット", "音声素材/エフェクト/nc393090_ロケットランチャー・発射.mp3")
      app.BGM_volume("ロケット", 20)
    app.BGM_play("ロケット")  
    
    if 1 <= app.character[name].memori_1:
        app.character[name].memori_5 = [1, 1, 1, 1]

    if 2 <= app.character[name].memori_1:
      GS.lock = False
      app.prayer.hyper_muteki = False
      # GS.clock_3 = 0
          
    if 10 <= app.character[name].memori_1:
        GS.lock = False
        GS.rocket_mika = False
        app.Crank_up_Character(name)
        print(app.character)
        app.BGM_memory_delete("ロケット")
        GS.enrgy_flag = True
        app.prayer.hyper_muteki = False
        return  
        
    dist = app.character[name].memori_1
    total_damage = 10 + GS.plus_damage
    
    count_damage(app, GS, key=0, damage=total_damage, count=dist, cx=0, cy=0) 
    count_damage(app, GS, key=1, damage=total_damage, count=dist, cx=0, cy=0)
    count_damage(app, GS, key=2, damage=total_damage, count=dist, cx=0, cy=0) 
    count_damage(app, GS, key=3, damage=total_damage, count=dist, cx=0, cy=0) 
     
     
def rocket_effect(app,GS,name):
  app.character[name].memori_1 += 1
  if app.character[name].memori_1 == 1:
    return
  
  dis_x,dis_y = dis_pl(app,GS)
  
  move = app.character[name].memori_1-1
  
  
  if app.character[name].memori_5[0] == 1:
    imag_1="タケノコ_A"
    app.image_rect_animation_fps_setting_free_size(imag_1,5+dis_x-move,0+dis_y, 5+dis_x-move-1,0+dis_y ,0,23)

  if app.character[name].memori_5[1] == 1:
    imag_1="タケノコ_D"
    app.image_rect_animation_fps_setting_free_size(imag_1,5+dis_x+move,0+dis_y, 5+dis_x+move+1,0+dis_y ,0,23)  
  
  if app.character[name].memori_5[2] == 1:
    imag_1="タケノコ_W"
    app.image_rect_animation_fps_setting_free_size(imag_1,5+dis_x,0+dis_y-move, 5+dis_x ,0+dis_y-move-1 ,0,23)  
    
  if app.character[name].memori_5[3] == 1:
    imag_1="タケノコ_S"
    app.image_rect_animation_fps_setting_free_size(imag_1,5+dis_x,0+dis_y+move, 5+dis_x ,0+dis_y+move+1 ,0,23)     
  

# パンチ
def panti(app,GS,name):
  GS.lock = True
  app.prayer.hyper_muteki = True

  if app.character[name].Initialization == True:
    pp = random.randint(0,2)
    if pp == 0:
        app.SE_play("ミカド_4_1")
    elif pp == 1:
        app.SE_play("ミカド_4_2")
    else:
        app.SE_play("ミカド_4_3")
        
    app.character[name].Initialization = False
    app.BGM_create("パンチ","音声素材/エフェクト/nc455820_大撃破パンチ.wav")
    app.BGM_volume("パンチ",20)
  app.BGM_play("パンチ")
  
  if GS.Peeled == 0:
    key  = 0
  elif GS.Peeled == 1:
    key  = 1
  elif GS.Peeled == 2:
    key  = 2
  elif GS.Peeled == 3:
    key  = 3
    
  damage(app,GS,key,10+GS.plus_damage)  
  if 2 <= app.character[name].memori_1:
    GS.lock = False
    GS.dorirucut_kai = False  
    GS.enrgy_flag = True 
  
  if 5 <= app.character[name].memori_1:
    GS.clock_4 = 0
    GS.lock = False
    # GS.cut_en = False
    app.Crank_up_Character(name)
    print(app.character)
    app.BGM_memory_delete("パンチ")
    GS.enrgy_flag = True
    app.prayer.hyper_muteki = False


def panti_effect(app,GS,name):
  app.character[name].memori_1 += 1