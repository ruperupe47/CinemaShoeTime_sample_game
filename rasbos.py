
import mob
import random


# ラスボス   
def seimei_enemies(app,GS,name):
  if app.character[name].Initialization == True:
    app.character[name].Initialization = False
    app.character[name].memori_1 = [[0,0,0,0],[0,0,0,0]] # 行動
    app.character[name].memori_2 = 0 # 向き
    app.character[name].memori_0 = 0
    app.character[name].lock = True
    app.character[name].memori_6  = 0
    
    app.character[name].HP = 1000000
    # app.character[name].HP = 3000


  if app.character[name].lock == True:    
    is_in_area = (89 <= app.prayer.Prayer_conmaas_x <= 120 and 3 <= app.prayer.Prayer_conmaas_y <= 28)
    if app.character[name].HP <= 5000 or is_in_area:
      app.character[name].lock = False
      if app.prayer.role == "エンペラー":
        app.SE_play("セイメイ_起動_エンペラー")
      elif app.prayer.role == "カイザー":
        app.SE_play("セイメイ_起動_カイザー")
      elif app.prayer.role == "ミカド":
        app.SE_play("セイメイ_起動_ミカド")
      elif app.prayer.role == "マシン":
        app.SE_play("セイメイ_起動_マシン")
      app.character[name].lock = False
    
    
  if app.character[name].lock == False:
    seimei_action(app,GS,name)
  print(app.character[name].HP)
    
  app.character[name].TPS_clock += 1
  
  
  if app.character[name].death_flag == True:
      app.character[name].death_flag = False
      for name,obj in app.character.items():
       app.Crank_up_Character(name)
      app.Crank_up()
      GS.status = "エンド"
  


 
def seimei_weak_attack(app,GS,name,element):
  if 20 <= app.character[name].TPS_clock:
    if True:
      app.character[name].TPS_clock = 0
      
      if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or  (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y-1) or (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y-2):    
       app.prayer_damage(300+app.prayer.defence)
       
       pp = random.randint(0,3)
       if pp == 0:
         app.SE_play("セイメイ_攻撃_1")
       elif pp == 1:
          app.SE_play("セイメイ_攻撃_2")
       else:
          app.SE_play("悪魔の笑い声")
        
       app.character[name].TPS_clock = 0
    
      if (app.character[name].Character_conmaas_x+3 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or  (app.character[name].Character_conmaas_x+3 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y-1) or (app.character[name].Character_conmaas_x+3 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y-2):    
        app.prayer_damage(300+app.prayer.defence)
        pp = random.randint(0,3)
        if pp == 0:
           app.SE_play("セイメイ_攻撃_1")
        elif pp == 1:
            app.SE_play("セイメイ_攻撃_2")
        else:
            app.SE_play("悪魔の笑い声")
    

      if (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y-1 == app.prayer.Prayer_conmaas_y) or  (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y-1) or (app.character[name].Character_conmaas_x+2 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y-1):    
        app.prayer_damage(300+app.prayer.defence)
        pp = random.randint(0,3)
        if pp == 0:
           app.SE_play("セイメイ_攻撃_1")
        elif pp == 1:
            app.SE_play("セイメイ_攻撃_2")
        else:
            app.SE_play("悪魔の笑い声")
    
      if (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y+3 == app.prayer.Prayer_conmaas_y) or  (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y+3) or (app.character[name].Character_conmaas_x+2 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y+3):    
        app.prayer_damage(300+app.prayer.defence)
        pp = random.randint(0,3)
        if pp == 0:
           app.SE_play("セイメイ_攻撃_1")
        elif pp == 1:
            app.SE_play("セイメイ_攻撃_2")
        else:
            app.SE_play("悪魔の笑い声")
            
        app.character[name].TPS_clock = 0
    
    
    
def arch_enemy_special_attack(app,GS,name):
  probability = random.randint(0, 100)
  
  if 70 <= probability:
    probability = random.randint(0, 2)
    app.SE_play("セイメイ_特殊_1")
    
    
    if probability == 0:
      names = "モブ_黒_レーザー"
      app.go_on_stage(names + "_" + str(GS.num))
      app.character[names + "_" + str(GS.num)].memori_1 = 0
      app.character[names + "_" + str(GS.num)].role = "モブ_黒_レーザー"
      app.character[names + "_" + str(GS.num)].memori_0 = name
      app.character[names + "_" + str(GS.num)].Character_conmaas_x = app.character[name].Character_conmaas_x
      app.character[names + "_" + str(GS.num)].Character_conmaas_y = app.character[name].Character_conmaas_y
      app.character[names + "_" + str(GS.num)].before_key = app.character[name].before_key
      GS.num += 1
    
    if probability == 1:
      names = "モブ_白_レーザー"
      app.go_on_stage(names + "_" + str(GS.num))
      app.character[names + "_" + str(GS.num)].memori_1 = 0
      app.character[names + "_" + str(GS.num)].role = "モブ_白_レーザー"
      app.character[names + "_" + str(GS.num)].memori_0 = name
      app.character[names + "_" + str(GS.num)].Character_conmaas_x = app.character[name].Character_conmaas_x
      app.character[names + "_" + str(GS.num)].Character_conmaas_y = app.character[name].Character_conmaas_y
      app.character[names + "_" + str(GS.num)].before_key = app.character[name].before_key
      GS.num += 1
    
    if probability == 2:
      names = "モブ_ボム"
      x_ = probability = random.randint(-10, 10)
      y_ = probability = random.randint(-10, 10)
      
      app.go_on_stage(names + "_" + str(GS.num))
      app.character[names + "_" + str(GS.num)].memori_1 = 0
      app.character[names + "_" + str(GS.num)].role = "モブ_ボム"
      app.character[names + "_" + str(GS.num)].memori_0 = name
      app.character[names + "_" + str(GS.num)].Character_conmaas_x = app.prayer.Prayer_conmaas_x + x_
      app.character[names + "_" + str(GS.num)].Character_conmaas_y = app.prayer.Prayer_conmaas_y + y_
      app.character[names + "_" + str(GS.num)].before_key = app.character[name].before_key
      GS.num += 1
      
      
def creater(app,GS,name,element):
  # if 100 <= app.character[name].memori_6:
  if True:
    app.character[name].memori_6 = 0
     
    be_x = app.prayer.Prayer_conmaas_x - (app.wight_mathpiece//3)-5
    af_x = app.prayer.Prayer_conmaas_x + (app.wight_mathpiece//3)+5
    be_y = app.prayer.Prayer_conmaas_y - (app.height_mathpiece//3)-5
    af_y = app.prayer.Prayer_conmaas_y + (app.height_mathpiece//3)+5
    
    bools = True 
    app.SE_play("つるはし") 
    # app.SE_play("つるはし") 
    # app.SE_play("つるはし") 
    # app.SE_play("つるはし") 
    # app.SE_play("つるはし") 
    
    
    for i in range(10):
     bools = True
     num =  random.randint(0,20)
     if num == 3:
       while bools == True :
        mob_x = random.randint(be_x, af_x)
        mob_y = random.randint(be_y, af_y)
        num = random.randint(0,3)
        
        if mob_x <= 4:
          continue
        elif len(GS.map_data[0])-4 <= mob_x:
          continue
        if mob_y <= 4:
          continue
        elif len(GS.map_data)-4 <= mob_y:
          continue  
        
        GS.map_data[mob_y][mob_x] = [2, ['シルバーレンガ']]
        bools = False
      
       
    if GS.mob_count <= 50:
      name = "モブ"+str(GS.counter)
      app.go_on_stage(name)
      bools = True

      be_x = app.prayer.Prayer_conmaas_x - (app.wight_mathpiece//3)-5
      af_x = app.prayer.Prayer_conmaas_x + (app.wight_mathpiece//3)+5
      be_y = app.prayer.Prayer_conmaas_y - (app.height_mathpiece//3)-5
      af_y = app.prayer.Prayer_conmaas_y + (app.height_mathpiece//3)+5

      while bools == True :      
        mob_x = random.randint(be_x, af_x)
        mob_y = random.randint(be_y, af_y)
        num = random.randint(0,3)
        
        if mob_x <= 1:
          continue
        elif len(GS.map_data[0])-1 <= mob_x:
          continue
        if mob_y <= 1:
          continue
        elif len(GS.map_data)-1 <= mob_y:
          continue
      
        if GS.map_data[mob_y][mob_x] != [1, [(175, 223, 228)]] and GS.map_data[mob_y][mob_x] != [2, ['レンガ']] and GS.map_data[mob_y][mob_x] != [2, ['シルバーレンガ']] and GS.map_data[mob_y][mob_x] != [2, ['岩']]:
          if num == 0:
            mob_y = be_y
            if mob_y <= 0:
              mob_y = 3
            app.character[name].Character_conmaas_x = mob_x
            app.character[name].Character_conmaas_y = mob_y
          if num == 1:
            mob_y = af_y
            if len(GS.map_data)-1 <= mob_y:
              mob_y = len(GS.map_data)-3
            app.character[name].Character_conmaas_x = mob_x
            app.character[name].Character_conmaas_y = mob_y      
                  
          if num == 2:
            mob_x = be_x
            if mob_x <= 0:
              mob_x = 3
            app.character[name].Character_conmaas_x = mob_x
            app.character[name].Character_conmaas_y = mob_y
          if num == 3:
            mob_x = af_x
            if len(GS.map_data[0])-1 <= mob_x:
              mob_x = len(GS.map_data[0])-4
            app.character[name].Character_conmaas_x = mob_x
            app.character[name].Character_conmaas_y = mob_y        
          app.character[name].memori_2 = 0
          bools = False
          GS.mob_count += 1
          GS.counter += 1
          GS.mob.append([name,(mob_x,mob_y)])
          # print([name,(mob_x,mob_y)])
        else:
         continue
       
      app.character[name].role = "守り手"  
      app.character[name].sub_role = "鬼_3"
      app.character[name].memori_1 = [[0,0,0,0],[0,0,0,0]]
  
    
       
def creater_2(app,GS,name,element):
  # if 100 <= app.character[name].memori_6:
  if True:
    app.character[name].memori_6 = 0
    if GS.mob_count <= 50:
      name = "モブ"+str(GS.counter)
      app.go_on_stage(name)
      bools = True

      be_x = app.prayer.Prayer_conmaas_x - (app.wight_mathpiece//3)-5
      af_x = app.prayer.Prayer_conmaas_x + (app.wight_mathpiece//3)+5
      be_y = app.prayer.Prayer_conmaas_y - (app.height_mathpiece//3)-5
      af_y = app.prayer.Prayer_conmaas_y + (app.height_mathpiece//3)+5

      while bools == True :      
        mob_x = random.randint(be_x, af_x)
        mob_y = random.randint(be_y, af_y)
        num = random.randint(0,3)
        
        if mob_x <= 1:
          continue
        elif len(GS.map_data[0])-1 <= mob_x:
          continue
        if mob_y <= 1:
          continue
        elif len(GS.map_data)-1 <= mob_y:
          continue
      
        if GS.map_data[mob_y][mob_x] != [1, [(175, 223, 228)]] and GS.map_data[mob_y][mob_x] != [2, ['レンガ']] and GS.map_data[mob_y][mob_x] != [2, ['シルバーレンガ']] and GS.map_data[mob_y][mob_x] != [2, ['岩']]:
          if num == 0:
            mob_y = be_y
            if mob_y <= 0:
              mob_y = 3
            app.character[name].Character_conmaas_x = mob_x
            app.character[name].Character_conmaas_y = mob_y
          if num == 1:
            mob_y = af_y
            if len(GS.map_data)-1 <= mob_y:
              mob_y = len(GS.map_data)-3
            app.character[name].Character_conmaas_x = mob_x
            app.character[name].Character_conmaas_y = mob_y      
                  
          if num == 2:
            mob_x = be_x
            if mob_x <= 0:
              mob_x = 3
            app.character[name].Character_conmaas_x = mob_x
            app.character[name].Character_conmaas_y = mob_y
          if num == 3:
            mob_x = af_x
            if len(GS.map_data[0])-1 <= mob_x:
              mob_x = len(GS.map_data[0])-4
            app.character[name].Character_conmaas_x = mob_x
            app.character[name].Character_conmaas_y = mob_y        
          app.character[name].memori_2 = 0
          bools = False
          GS.mob_count += 1
          GS.counter += 1
          GS.mob.append([name,(mob_x,mob_y)])
          # print([name,(mob_x,mob_y)])
        else:
         continue
       
      app.character[name].role = "守り手"  
      app.character[name].sub_role = "鬼_3"
      app.character[name].memori_1 = [[0,0,0,0],[0,0,0,0]]
  
     
      
def seimei_action(app,GS,name):
  app.character[name].memori_6 += 1
  
  x = app.character[name].Character_conmaas_x
  y = app.character[name].Character_conmaas_y
      
  view_left  = x - app.wight_mathpiece
  view_right = x + app.wight_mathpiece
  view_up    = y - app.height_mathpiece
  view_down  = y + app.height_mathpiece


  if app.character[name].death_flag == True:
    GS.death_mob += 1
    GS.power_count += 1
    app.Crank_up_Character(name)
    GS.mob_count -= 1
    return


  app.character[name].memori_1 = mob.bot_input_generator(GS.map_data, (x,y), (app.prayer.Prayer_conmaas_x,app.prayer.Prayer_conmaas_y))

  if not app.character[name].memori_1:
    app.character[name].before_key = ""
    return
    
  element = app.character[name].memori_1.pop(0)
  # [a,d,w,s]
  action(app,GS,name,element)
  
  x = app.character[name].Character_conmaas_x
  y = app.character[name].Character_conmaas_y
  

  GS.bos = [] 
  GS.bos.append(["セイメイ",(x,y)])  
  GS.bos.append(["セイメイ",(x+1,y)])  
  GS.bos.append(["セイメイ",(x+2,y)])  
  GS.bos.append(["セイメイ",(x,y+1)])  
  GS.bos.append(["セイメイ",(x+1,y+1)])  
  GS.bos.append(["セイメイ",(x+2,y+1)])  
  GS.bos.append(["セイメイ",(x,y+2)])  
  GS.bos.append(["セイメイ",(x+1,y+2)])  
  GS.bos.append(["セイメイ",(x+2,y+2)])  

  if 800000 <= app.character[name].HP:
    seimei_weak_attack(app,GS,name,element) 
  elif 500000 <= app.character[name].HP:
    arch_enemy_special_attack(app,GS,name)
    seimei_weak_attack(app,GS,name,element) 
    creater_2(app,GS,name,element)
  elif 300000 <= app.character[name].HP:
    arch_enemy_special_attack(app,GS,name)
    seimei_weak_attack(app,GS,name,element) 
    creater(app,GS,name,element)
  else:
    arch_enemy_special_attack(app,GS,name)
    seimei_weak_attack(app,GS,name,element) 
    creater(app,GS,name,element)  
  
  
  

def action(app,GS,name,element):

  # [a,d,w,s]
  if element[0] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or  (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y-1) or (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y-2):
      app.character[name].before_key = ""
    else:
      app.character[name].before_key = "A"
      break_bool = False
      for n in range(len(GS.before_mob)):
        if GS.before_mob[n][1][0] == app.character[name].Character_conmaas_x-1 and GS.before_mob[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break
      for n in range(len(GS.mob)):
        if GS.mob[n][1][0] == app.character[name].Character_conmaas_x-1 and GS.mob[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break
      if break_bool == False:
        app.character[name].memori_2 = 0
        app.character[name].Character_conmaas_x -= 1
      else:
        app.character[name].before_key = ""
        
  elif element[1] == 1:
    if (app.character[name].Character_conmaas_x+3 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or  (app.character[name].Character_conmaas_x+3 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y-1) or (app.character[name].Character_conmaas_x+3 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y-2):
      app.character[name].before_key = ""
    else:
      app.character[name].before_key = "D"
      break_bool = False
      for n in range(len(GS.before_mob)):
        if GS.before_mob[n][1][0] == app.character[name].Character_conmaas_x+1 and GS.before_mob[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break
      for n in range(len(GS.mob)):
        if GS.mob[n][1][0] == app.character[name].Character_conmaas_x+1 and GS.mob[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break
      if break_bool == False:
        app.character[name].memori_2 = 1
        app.character[name].Character_conmaas_x += 1  
      else:
        app.character[name].before_key = ""
        
  elif element[2] == 1:
    if (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y-1 == app.prayer.Prayer_conmaas_y) or  (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y-1) or (app.character[name].Character_conmaas_x+2 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y-1):
      app.character[name].before_key = ""
    else:
      break_bool = False
      app.character[name].before_key = "W"
      for n in range(len(GS.before_mob)):
        if GS.before_mob[n][1][0] == app.character[name].Character_conmaas_x and GS.before_mob[n][1][1] == app.character[name].Character_conmaas_y-1:
          break_bool = True
          break
      for n in range(len(GS.mob)):
        if GS.mob[n][1][0] == app.character[name].Character_conmaas_x and GS.mob[n][1][1] == app.character[name].Character_conmaas_y-1:
          break_bool = True
          break
      if break_bool == False:
        app.character[name].memori_2 = 2
        app.character[name].Character_conmaas_y -= 1
      else:
        app.character[name].before_key = ""
        
  elif element[3] == 1:
    if (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y+3 == app.prayer.Prayer_conmaas_y) or  (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y+3) or (app.character[name].Character_conmaas_x+2 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y+3):
      app.character[name].before_key = ""
    else:
      app.character[name].before_key = "S"
      break_bool = False
      for n in range(len(GS.before_mob)):
        if GS.before_mob[n][1][0] == app.character[name].Character_conmaas_x and GS.before_mob[n][1][1] == app.character[name].Character_conmaas_y+1:
          break_bool = True
          break
      for n in range(len(GS.mob)):
        if GS.mob[n][1][0] == app.character[name].Character_conmaas_x and GS.mob[n][1][1] == app.character[name].Character_conmaas_y+1:
          break_bool = True
          break
      if break_bool == False:
        app.character[name].memori_2 = 3
        app.character[name].Character_conmaas_y += 1    
      else:
        app.character[name].before_key = ""
  
  GS.mob.append([name,(app.character[name].Character_conmaas_x,app.character[name].Character_conmaas_y)])
    
    

