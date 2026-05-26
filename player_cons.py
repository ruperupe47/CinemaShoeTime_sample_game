import random

def control(app,GS,count,skip):    
  now_x = app.prayer.Prayer_conmaas_x
  now_y = app.prayer.Prayer_conmaas_y

  break_bool = False
  if (app.before_Arrow_keys[0] == 1 or app.before_atoz_list[0] == 1) and skip == True:# 左,A
      for i in range(count):
        A_tile = GS.map_data[now_y][now_x-i-1]
        if A_tile != [1, [(175, 223, 228)]] and A_tile != [2, ['レンガ']] and A_tile != [2, ['シルバーレンガ']] and A_tile != [2, ['岩']]:    
          for n in range(len(GS.mob)):
            if GS.mob[n][1][0] == now_x-i-1 and GS.mob[n][1][1] == now_y:
              break_bool = True
              break  
          for n in range(len(GS.bos)):
            if GS.bos[n][1][0] == now_x-i-1 and GS.bos[n][1][1] == now_y:
              break_bool = True
              break          
          if break_bool == True:
            break
          app.prayer.Prayer_conmaas_x -= 1
          app.prayer.memori_1 -= 1
        else:
          break
  elif (app.before_Arrow_keys[1] == 1 or app.before_atoz_list[3] == 1)and skip == True:# 右,D
      for i in range(count):
         D_tile = GS.map_data[now_y][now_x+i+1]
         if D_tile != [1, [(175, 223, 228)]] and D_tile != [2, ['レンガ']] and D_tile != [2, ['シルバーレンガ']] and D_tile != [2, ['岩']]:
          for n in range(len(GS.mob)):
            if GS.mob[n][1][0] == now_x+i+1 and GS.mob[n][1][1] == now_y:
              break_bool = True
              break  
          for n in range(len(GS.bos)):
            if GS.bos[n][1][0] == now_x+i+1 and GS.bos[n][1][1] == now_y:
              break_bool = True
              break          
          if break_bool == True:
            break
          app.prayer.Prayer_conmaas_x += 1
          app.prayer.memori_1 += 1
         else:
          break
  elif (app.before_Arrow_keys[2] == 1 or app.before_atoz_list[22] == 1)and skip == True:# 上,W 
      for i in range(count):
        W_tile = GS.map_data[now_y-i-1][now_x]
        if W_tile != [1, [(175, 223, 228)]] and W_tile != [2, ['レンガ']] and W_tile != [2, ['シルバーレンガ']] and W_tile != [2, ['岩']]:
          for n in range(len(GS.mob)):
            if GS.mob[n][1][0] == now_x and GS.mob[n][1][1] == now_y-i-1:
              break_bool = True
              break  
          for n in range(len(GS.bos)):
            if GS.bos[n][1][0] == now_x and GS.bos[n][1][1] == now_y-i-1:
              break_bool = True
              break          
          if break_bool == True:
            break          
          app.prayer.Prayer_conmaas_y -= 1
          app.prayer.memori_2 -= 1
        else:
          break
  elif (app.before_Arrow_keys[3] == 1 or app.before_atoz_list[18] == 1)and skip == True:# 下,S 
      for i in range(count):
        S_tile = GS.map_data[now_y+i+1][now_x]
        if S_tile != [1, [(175, 223, 228)]] and S_tile != [2, ['レンガ']] and S_tile != [2, ['シルバーレンガ']] and S_tile != [2, ['岩']]:
          for n in range(len(GS.mob)):
            if GS.mob[n][1][0] == now_x and GS.mob[n][1][1] == now_y+i+1:
              break_bool = True
              break  
          for n in range(len(GS.bos)):
            if GS.bos[n][1][0] == now_x and GS.bos[n][1][1] == now_y+i+1:
              break_bool = True
              break          
          if break_bool == True:
            break
          app.prayer.Prayer_conmaas_y += 1
          app.prayer.memori_2 += 1
        else:
          break
        
        

def rimokon(app,GS):
  # ポーズ画面以降
  if app.before_atoz_list[15] == 1:
    GS.begore_status =  "ゲーム"
    GS.status = "blick"
    return
  
  
  bools = True
  while bools == True:
    if GS.efficiency_meter <= 30:
      if GS.power_count <= 0:
        bools = False
      else:
        GS.power_count -= 1
        GS.efficiency_meter += 1
        
        GS.ps_HP = 5
        GS.ps_energy = 5
        app.prayer.MX_energy += 5
        app.prayer.MX_HP += 1
        app.prayer.defence += 5
        GS.plus_damage += 5
    else:
      GS.kimewaza = True
      if GS.power_count <= 2:
         bools = False
      else:
        GS.power_count -= 3
        GS.efficiency_meter += 1
        
        GS.ps_HP = 10
        GS.ps_energy = 10
        app.prayer.MX_energy += 5
        app.prayer.MX_HP += 10
        app.prayer.defence += 5
        GS.plus_damage += 10
  
  if app.prayer.energy <= 0:
    app.prayer.energy = 0
    
  app.prayer.TPS_clock += 1
  if app.prayer.energy < app.prayer.MX_energy and 20 <= app.prayer.TPS_clock and GS.enrgy_flag == True:
    app.prayer.energy += GS.ps_energy
    if app.prayer.MX_energy <= app.prayer.energy:
      app.prayer.energy = app.prayer.MX_energy
      
  if app.prayer.HP < app.prayer.MX_HP and 30 <= app.prayer.TPS_clock and 0 <= app.prayer.energy:
    app.prayer.HP += GS.ps_HP
    if app.prayer.MX_HP <= app.prayer.HP:
      app.prayer.HP = app.prayer.MX_HP
      app.prayer.TPS_clock = 0
  
  # print(app.prayer.MX_HP)
  
  GS.clock_1 += 1
  GS.clock_2 += 1
  GS.clock_3 += 1
  GS.clock_4 += 1
  
  GS.enter_clock += 1 
  if GS.enter_parameter == False and app.before_Enter_key == 1 and 4 <= GS.enter_clock:
    GS.enter_parameter = True
    GS.enter_clock = 0
  elif GS.enter_parameter == True and app.before_Enter_key == 1 and 4 <= GS.enter_clock:
    GS.enter_parameter = False   
    GS.enter_clock = 0

  
  if 2 <= GS.clock:
    skip = True
    GS.clock = 0
  else:
    skip = False
    
    
  if GS.lock == True:
    skip = False
      
  under_tile = GS.map_data[app.prayer.Prayer_conmaas_y][app.prayer.Prayer_conmaas_x]
  A_tile = GS.map_data[app.prayer.Prayer_conmaas_y][app.prayer.Prayer_conmaas_x-1]
  D_tile = GS.map_data[app.prayer.Prayer_conmaas_y][app.prayer.Prayer_conmaas_x+1]
  W_tile = GS.map_data[app.prayer.Prayer_conmaas_y-1][app.prayer.Prayer_conmaas_x]
  S_tile = GS.map_data[app.prayer.Prayer_conmaas_y+1][app.prayer.Prayer_conmaas_x]
  # print(under_tile,A_tile,D_tile,W_tile,S_tile)
  
  
  if app.prayer.role == "エンペラー":
    emper_rimokon(app,GS,skip,under_tile,A_tile,D_tile,W_tile,S_tile)
  elif app.prayer.role == "カイザー":
    kaizer_rimokon(app,GS,skip,under_tile,A_tile,D_tile,W_tile,S_tile)
  elif app.prayer.role == "ミカド":
    mikado_rimokon(app,GS,skip,under_tile,A_tile,D_tile,W_tile,S_tile)
  elif app.prayer.role == "マシン":
    masin_rimokon(app,GS,skip,under_tile,A_tile,D_tile,W_tile,S_tile)
    
  GS.before_mob = GS.mob.copy()
  GS.mob = []
  
  if (app.before_Arrow_keys[0] == 1 or app.before_atoz_list[0] == 1) and skip == True:# 左,A
    app.prayer.prayer_img = app.prayer.memori_3 + "_A"
    GS.Peeled = 0
  elif (app.before_Arrow_keys[1] == 1 or app.before_atoz_list[3] == 1) and skip == True:# 右,D
    app.prayer.prayer_img = app.prayer.memori_3 + "_D"
    GS.Peeled = 1
  elif (app.before_Arrow_keys[2] == 1 or app.before_atoz_list[22] == 1) and skip == True:# 上,W 
    app.prayer.prayer_img = app.prayer.memori_3 + "_W"
    GS.Peeled = 2
  elif (app.before_Arrow_keys[3] == 1 or app.before_atoz_list[18] == 1) and skip == True:# 下,S 
    app.prayer.prayer_img = app.prayer.memori_3 + "_S"
    GS.Peeled = 3
        
  # print(app.prayer.Prayer_conmaas_x,app.prayer.Prayer_conmaas_y)      
  
           
def emper_rimokon(app,GS,skip,under_tile,A_tile,D_tile,W_tile,S_tile):
  
  be_x = app.prayer.Prayer_conmaas_x
  be_y = app.prayer.Prayer_conmaas_y
  
  # 移動
  if GS.enter_parameter == True and skip == True:
    control(app,GS,2,skip)
    
  elif GS.enter_parameter == False and skip == True:
    control(app,GS,1,skip)
           
  if app.prayer.Prayer_conmaas_x != be_x or app.prayer.Prayer_conmaas_y != be_y:
    app.SE_play("巨大ロボット")  
               
  # スキル         
  if app.before_list_0to9[0] == 1 and skip == True: # 分離
    app.prayer.role = "マシン"
    app.prayer.memori_3 = "エンペラー号"
    app.prayer.memori_4 = "分離"
    app.SE_play("エンペラー_分離")
    if GS.Peeled == 0:
      app.prayer.prayer_img = app.prayer.memori_3 + "_A"
    elif GS.Peeled == 1:
      app.prayer.prayer_img = app.prayer.memori_3 + "_D" 
    elif GS.Peeled == 2:
      app.prayer.prayer_img = app.prayer.memori_3 + "_W" 
    elif GS.Peeled == 3:
      app.prayer.prayer_img = app.prayer.memori_3 + "_S"    
    GS.clock_1 = 0
    GS.clock_2 = 0
    GS.cloc_3 = 0
    GS.clock_4 = 0
  elif app.before_list_0to9[1] == 1 and 5 <= GS.clock_1 and skip == True and 100 <= app.prayer.energy and GS.kimewaza == True: # ビーム
    GS.clock_1 = 0
    app.go_on_stage("ビーム"+str(GS.num))
    app.character["ビーム"+str(GS.num)].memori_1 = 0
    GS.num += 1
    app.prayer.energy -= 100
    GS.enrgy_flag = False
  elif app.before_list_0to9[2] == 1 and 10 <= GS.clock_2 and skip == True: # ブーメラン
    GS.clock_2 = 0
    app.go_on_stage("ブーメラン"+str(GS.num))
    app.character["ブーメラン"+str(GS.num)].memori_1 = 0
    GS.num += 1    
    GS.enrgy_flag = False
  elif app.before_list_0to9[3] == 1 and 10 <= GS.clock_3 and skip == True: # カッター
    GS.clock_3 = 0
    app.go_on_stage("カッター"+str(GS.num))
    app.character["カッター"+str(GS.num)].memori_1 = 0
    GS.num += 1
    GS.enrgy_flag = False
  elif app.before_list_0to9[4] == 1 and 5 <= GS.clock_4 and skip == True: # 切り
    GS.clock_4 = 0
    app.go_on_stage("切り"+str(GS.num))
    app.character["切り"+str(GS.num)].memori_1 = 0
    GS.num += 1
    GS.enrgy_flag = False
        
    
def kaizer_rimokon(app,GS,skip,under_tile,A_tile,D_tile,W_tile,S_tile):
  
  be_x = app.prayer.Prayer_conmaas_x
  be_y = app.prayer.Prayer_conmaas_y
  
  if GS.enter_parameter == True and skip == True:
    control(app,GS,6,skip)

  elif GS.enter_parameter == False and skip == True:
    control(app,GS,2,skip)
    
  if app.prayer.Prayer_conmaas_x != be_x or app.prayer.Prayer_conmaas_y != be_y:
    app.SE_play("ロボットSF")      
    
  # スキル         
  if app.before_list_0to9[0] == 1 and skip == True:
    app.prayer.role = "マシン"
    app.prayer.memori_3 = "カイザー号"
    app.prayer.memori_4 = "分離"
    app.SE_play("カイザー_分離")
    if GS.Peeled == 0:
      app.prayer.prayer_img = app.prayer.memori_3 + "_A"
    elif GS.Peeled == 1:
      app.prayer.prayer_img = app.prayer.memori_3 + "_D" 
    elif GS.Peeled == 2:
      app.prayer.prayer_img = app.prayer.memori_3 + "_W" 
    elif GS.Peeled == 3:
      app.prayer.prayer_img = app.prayer.memori_3 + "_S"     
    GS.clock_1 = 0
    GS.clock_2 = 0
    GS.cloc_3 = 0
    GS.clock_4 = 0
  elif app.before_list_0to9[1] == 1 and 10<= GS.clock_1 and skip == True and 30 <= app.prayer.energy and GS.kimewaza == True: # ドリルミサイル
    GS.clock_1 = 0
    app.go_on_stage("ドリルミサイル"+str(GS.num))
    app.character["ドリルミサイル"+str(GS.num)].memori_1 = 0
    GS.num += 1
    app.prayer.energy -= 30
    GS.enrgy_flag = False
  elif app.before_list_0to9[2] == 1 and 10 <= GS.clock_2 and skip == True and 20 <= app.prayer.energy: # ハリケーン
    GS.clock_2 = 0
    app.go_on_stage("ハリケーン"+str(GS.num))
    app.character["ハリケーン"+str(GS.num)].memori_1 = 0
    GS.num += 1    
    app.prayer.energy -= 20
    GS.enrgy_flag = False
  elif app.before_list_0to9[3] == 1 and 10 <= GS.clock_3 and skip == True and 30 <= app.prayer.energy: # トルネード
    GS.clock_3 = 0
    app.go_on_stage("トルネード"+str(GS.num))
    app.character["トルネード"+str(GS.num)].memori_1 = 0
    GS.num += 1
    app.prayer.energy -= 30
    GS.enrgy_flag = False
  elif app.before_list_0to9[4] == 1 and 5 <= GS.clock_4 and skip == True: # ドリル切り
    GS.clock_4 = 0
    app.go_on_stage("ドリル切り"+str(GS.num))
    app.character["ドリル切り"+str(GS.num)].memori_1 = 0
    GS.num += 1          
    GS.enrgy_flag = False  
    
    
    
def mikado_rimokon(app,GS,skip,under_tile,A_tile,D_tile,W_tile,S_tile):
  count = 1
  now_x = app.prayer.Prayer_conmaas_x
  now_y = app.prayer.Prayer_conmaas_y
  break_bool = False
  be_x = app.prayer.Prayer_conmaas_x
  be_y = app.prayer.Prayer_conmaas_y
  
  if skip == True:
    if app.before_Arrow_keys[0] == 1 or app.before_atoz_list[0] == 1:# 左,A
      for i in range(count):
        A_tile = GS.map_data[now_y][now_x-i-1]
        for n in range(len(GS.mob)):
          if GS.mob[n][1][0] == now_x-i-1 and GS.mob[n][1][1] == now_y:
             break_bool = True
             break
        for n in range(len(GS.bos)):
          if GS.bos[n][1][0] == now_x-i-1 and GS.bos[n][1][1] == now_y:
            break_bool = True
            break          
        if break_bool == True:
          break
          
          
        if A_tile == [2, ['岩']]:
          GS.map_data[now_y][now_x-i-1] = [2, ['地面']]
          app.prayer.Prayer_conmaas_x -= 1
          app.prayer.memori_1 -= 1
        elif  A_tile ==  [2, ['レンガ']] and 30 <= GS.efficiency_meter:
          GS.map_data[now_y][now_x-i-1] = [2, ['地面']]
          app.prayer.Prayer_conmaas_x -= 1
          app.prayer.memori_1 -= 1        
        elif  A_tile == [2, ['シルバーレンガ']] and 50 <= GS.efficiency_meter:
          GS.map_data[now_y][now_x-i-1] = [2, ['地面']]
          app.prayer.Prayer_conmaas_x -= 1
          app.prayer.memori_1 -= 1
        elif A_tile != [1, [(175, 223, 228)]] and A_tile != [2, ['レンガ']] and A_tile != [2, ['シルバーレンガ']] and A_tile != [2, ['岩']]:
          app.prayer.Prayer_conmaas_x -= 1
          app.prayer.memori_1 -= 1
        else:
          break      

    elif app.before_Arrow_keys[1] == 1 or app.before_atoz_list[3] == 1:# 右,D
      for i in range(count):
        D_tile = GS.map_data[now_y][now_x+i+1]
        for n in range(len(GS.mob)):
          if GS.mob[n][1][0] == now_x+i+1 and GS.mob[n][1][1] == now_y:
             break_bool = True
             break
        for n in range(len(GS.bos)):
          if GS.bos[n][1][0] == now_x+i+1 and GS.bos[n][1][1] == now_y:
            break_bool = True
            break          
        if break_bool == True:
          break
        
        
        if D_tile == [2, ['岩']]:
          GS.map_data[now_y][now_x+i+1] = [2, ['地面']]
          app.prayer.Prayer_conmaas_x += 1
          app.prayer.memori_1 += 1
        elif  D_tile ==  [2, ['レンガ']] and 30 <= GS.efficiency_meter:
          GS.map_data[now_y][now_x+i+1] = [2, ['地面']]
          app.prayer.Prayer_conmaas_x += 1
          app.prayer.memori_1 += 1        
        elif  D_tile == [2, ['シルバーレンガ']] and 50 <= GS.efficiency_meter:
          GS.map_data[now_y][now_x+i+1] = [2, ['地面']]
          app.prayer.Prayer_conmaas_x += 1
          app.prayer.memori_1 += 1
        elif D_tile != [1, [(175, 223, 228)]] and D_tile != [2, ['レンガ']] and D_tile != [2, ['シルバーレンガ']] and D_tile != [2, ['岩']]:
          app.prayer.Prayer_conmaas_x += 1
          app.prayer.memori_1 += 1    
        else:
         break
          
    elif app.before_Arrow_keys[2] == 1 or app.before_atoz_list[22] == 1:# 上,W 
      for i in range(count):
        W_tile = GS.map_data[now_y-i-1][now_x]
        for n in range(len(GS.mob)):
          if GS.mob[n][1][0] == now_x and GS.mob[n][1][1] == now_y-i-1:
             break_bool = True
             break
        for n in range(len(GS.bos)):
          if GS.bos[n][1][0] == now_x and GS.bos[n][1][1] == now_y-i-1:
            break_bool = True
            break          
        if break_bool == True:
          break
    

        if W_tile == [2, ['岩']]:
          GS.map_data[now_y-i-1][now_x] = [2, ['地面']]
          app.prayer.Prayer_conmaas_y -= 1
          app.prayer.memori_2 -= 1
        elif  W_tile ==  [2, ['レンガ']] and 30 <= GS.efficiency_meter:
          GS.map_data[now_y-i-1][now_x] = [2, ['地面']]
          app.prayer.Prayer_conmaas_y -= 1
          app.prayer.memori_2 -= 1        
        elif  W_tile == [2, ['シルバーレンガ']] and 50 <= GS.efficiency_meter:
          GS.map_data[now_y-i-1][now_x] = [2, ['地面']]
          app.prayer.Prayer_conmaas_y -= 1
          app.prayer.memori_2 -= 1
        elif W_tile != [1, [(175, 223, 228)]] and W_tile != [2, ['レンガ']] and W_tile != [2, ['シルバーレンガ']] and W_tile != [2, ['岩']]:
          app.prayer.Prayer_conmaas_y -= 1
          app.prayer.memori_2 -= 1         
        else:
          break          
       
        
    elif app.before_Arrow_keys[3] == 1 or app.before_atoz_list[18] == 1:# 下,S 
      for i in range(count):
        S_tile = GS.map_data[now_y+i+1][now_x]
        for n in range(len(GS.mob)):
          if GS.mob[n][1][0] == now_x and GS.mob[n][1][1] == now_y+i+1:
             break_bool = True
             break
        for n in range(len(GS.bos)):
          if GS.bos[n][1][0] == now_x and GS.bos[n][1][1] == now_y+i+1:
            break_bool = True
            break          
        if break_bool == True:
          break
        
        
        if S_tile == [2, ['岩']]:
          GS.map_data[now_y+i+1][now_x] = [2, ['地面']]
          app.prayer.Prayer_conmaas_y += 1
          app.prayer.memori_2 += 1
        elif  S_tile ==  [2, ['レンガ']] and 30 <= GS.efficiency_meter:
          GS.map_data[now_y+i+1][now_x]= [2, ['地面']]
          app.prayer.Prayer_conmaas_y += 1
          app.prayer.memori_2 += 1        
        elif  S_tile == [2, ['シルバーレンガ']] and 50 <= GS.efficiency_meter:
          GS.map_data[now_y+i+1][now_x] = [2, ['地面']]
          app.prayer.Prayer_conmaas_y += 1
          app.prayer.memori_2 += 1
        elif S_tile != [1, [(175, 223, 228)]] and S_tile != [2, ['レンガ']] and S_tile != [2, ['シルバーレンガ']] and S_tile != [2, ['岩']]:
          app.prayer.Prayer_conmaas_y += 1
          app.prayer.memori_2 += 1   
        else:
          break


  if app.prayer.Prayer_conmaas_x != be_x or app.prayer.Prayer_conmaas_y != be_y:
    app.SE_play("キャタピラ走行")  
    
    
  # スキル         
  if app.before_list_0to9[0] == 1 and skip == True:
    app.prayer.role = "マシン"
    app.prayer.memori_3 = "ミカド号"
    app.prayer.memori_4 = "分離"
    app.SE_play("ミカド_分離")
    if GS.Peeled == 0:
      app.prayer.prayer_img = app.prayer.memori_3 + "_A"
    elif GS.Peeled == 1:
      app.prayer.prayer_img = app.prayer.memori_3 + "_D" 
    elif GS.Peeled == 2:
      app.prayer.prayer_img = app.prayer.memori_3 + "_W" 
    elif GS.Peeled == 3:
      app.prayer.prayer_img = app.prayer.memori_3 + "_S"        
    GS.clock_1 = 0
    GS.clock_2 = 0
    GS.cloc_3 = 0
    GS.clock_4 = 0
  elif app.before_list_0to9[1] == 1 and 10 <= GS.clock_1 and skip == True and 60 <= app.prayer.energy and GS.kimewaza == True: # 超竹おろし
    GS.clock_1 = 0
    app.go_on_stage("おろし"+str(GS.num))
    app.character["おろし"+str(GS.num)].memori_1 = 0
    GS.num += 1
    app.prayer.energy -= 60
    GS.enrgy_flag = False
  elif app.before_list_0to9[2] == 1 and 2 <= GS.clock_2 and skip == True and 10 <= app.prayer.energy: # ミサイル
    GS.clock_2 = 0
    app.go_on_stage("クラスター"+str(GS.num))
    app.character["クラスター"+str(GS.num)].memori_1 = 0
    GS.num += 1    
    app.prayer.energy -= 10
    GS.enrgy_flag = False
  elif app.before_list_0to9[3] == 1 and 2 <= GS.clock_3 and skip == True and 10 <= app.prayer.energy: # ロケット
    GS.clock_3 = 0
    app.go_on_stage("ロケット"+str(GS.num))
    app.character["ロケット"+str(GS.num)].memori_1 = 0
    GS.num += 1
    app.prayer.energy -= 10
    GS.enrgy_flag = False
  elif app.before_list_0to9[4] == 1 and 5 <= GS.clock_4 and skip == True: # パンチ
    GS.clock_4 = 0
    app.go_on_stage("パンチ"+str(GS.num))
    app.character["パンチ"+str(GS.num)].memori_1 = 0
    GS.num += 1        
    GS.enrgy_flag = False
    
        

def masin_rimokon(app,GS,skip,under_tile,A_tile,D_tile,W_tile,S_tile):
  app.prayer.hyper_muteki = True
  
  be_x = app.prayer.Prayer_conmaas_x
  be_y = app.prayer.Prayer_conmaas_y
  
  if skip == True:
    control(app,GS,5,skip)
    
  if app.prayer.Prayer_conmaas_x != be_x or app.prayer.Prayer_conmaas_y != be_y:
    app.SE_play("飛行音")  
    
  # スキル         
  if app.before_list_0to9[1] == 1 and skip == True:
    pp = random.randint(0,2)
    if pp == 0:
        app.SE_play("エンペラー_合体_1")
    elif pp == 1:
        app.SE_play("エンペラー_合体_2")
    else:
        app.SE_play("エンペラー_合体_3")
        
    app.prayer.role = "エンペラー"
    app.prayer.memori_3 = "オウエンペラー"
    app.prayer.memori_4 = "合体"
    if GS.Peeled == 0:
      app.prayer.prayer_img = app.prayer.memori_3 + "_A"
    elif GS.Peeled == 1:
      app.prayer.prayer_img = app.prayer.memori_3 + "_D" 
    elif GS.Peeled == 2:
      app.prayer.prayer_img = app.prayer.memori_3 + "_W" 
    elif GS.Peeled == 3:
      app.prayer.prayer_img = app.prayer.memori_3 + "_S"  
    app.prayer.hyper_muteki = False

  elif app.before_list_0to9[2] == 1 and skip == True:
    pp = random.randint(0,2)
    if pp == 0:
        app.SE_play("カイザー_合体_1")
    elif pp == 1:
        app.SE_play("カイザー_合体_2")
    else:
        app.SE_play("カイザー_合体_3")
    app.prayer.role = "カイザー"
    app.prayer.memori_3 = "オウカイザー"
    app.prayer.memori_4 = "合体"
    if GS.Peeled == 0:
      app.prayer.prayer_img = app.prayer.memori_3 + "_A"
    elif GS.Peeled == 1:
      app.prayer.prayer_img = app.prayer.memori_3 + "_D" 
    elif GS.Peeled == 2:
      app.prayer.prayer_img = app.prayer.memori_3 + "_W" 
    elif GS.Peeled == 3:
      app.prayer.prayer_img = app.prayer.memori_3 + "_S"   
    app.prayer.hyper_muteki = False  
    
  elif app.before_list_0to9[3] == 1 and skip == True:
    pp = random.randint(0,2)
    if pp == 0:
        app.SE_play("ミカド_合体_1")
    elif pp == 1:
        app.SE_play("ミカド_合体_2")
    else:
        app.SE_play("ミカド_合体_3")
    app.prayer.role = "ミカド"
    app.prayer.memori_3 = "オウミカド"
    app.prayer.memori_4 = "合体"
    if GS.Peeled == 0:
      app.prayer.prayer_img = app.prayer.memori_3 + "_A"
    elif GS.Peeled == 1:
      app.prayer.prayer_img = app.prayer.memori_3 + "_D" 
    elif GS.Peeled == 2:
      app.prayer.prayer_img = app.prayer.memori_3 + "_W" 
    elif GS.Peeled == 3:
      app.prayer.prayer_img = app.prayer.memori_3 + "_S"  
    app.prayer.hyper_muteki = False      