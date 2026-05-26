import random
import enmy_efect_dis

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
  
  

from collections import deque
# AIを活用
def bot_input_generator(maze_map, start_pos, target_pos, max_steps= 5):
    """
    maze_map: GS.map_data と同じ二次元リスト
    start_pos: (x, y) 現在地
    target_pos: (x, y) 目的地
    max_steps: 一度に作成するキューの最大数
    """
    start_x, start_y = int(start_pos[0]), int(start_pos[1])
    target_x, target_y = int(target_pos[0]), int(target_pos[1])
    
    # 既に目的地にいる場合は即座に空のキューを返す
    if (start_x, start_y) == (target_x, target_y):
        return []
        
    # 🛑 【追加】通れない障害物タイルの完全リスト
    ignore_tiles = [
        [1, [(175, 223, 228)]],
        [2, ['レンガ']],
        [2, ['シルバーレンガ']],
        [2, ['岩']]
    ]
          
    # 探索用キュー: (現在の座標)
    queue = deque([(start_x, start_y)])
    # 経路復元用の辞書: { 移動先の座標 : (移動元の座標, 移動した方向インデックス) }
    came_from = {(start_x, start_y): None}
    
    # 方向の定義 [0:a(左), 1:d(右), 2:w(上), 3:s(下)]
    dirs = [
        (-1, 0), # 0: a (左)
        (1, 0),  # 1: d (右)
        (0, -1), # 2: w (上)
        (0, 1)   # 3: s (下)
    ]
    
    found = False
    
    while queue:
        cx, cy = queue.popleft()
        
        # 目的地に到達
        if (cx, cy) == (target_x, target_y):
            found = True
            break
            
        for i, (dx, dy) in enumerate(dirs):
            nx, ny = cx + dx, cy + dy
            
            # マップの範囲内かチェック
            if 0 <= ny < len(maze_map) and 0 <= nx < len(maze_map[0]):
                
                # 進む先のタイルデータを取得
                target_tile = maze_map[ny][nx]
                
                # ⭕ 修正：進む先が障害物リストに含まれて「おらず」、まだ未訪問のマスなら進む
                if (target_tile not in ignore_tiles) and ((nx, ny) not in came_from):
                    came_from[(nx, ny)] = ((cx, cy), i)
                    queue.append((nx, ny))

    # --- 目的地から逆算して経路（方向インデックスのリスト）を復元 ---
    found_path_indices = []
    if found:
        curr = (target_x, target_y)
        while curr != (start_x, start_y):
            prev, direction_idx = came_from[curr]
            found_path_indices.append(direction_idx)
            curr = prev
        # 逆順をスタート→目的地順に反転
        found_path_indices.reverse()

    # --- 数値リスト [[a,d,w,s], ...] に変換 ---
    action_queue = []
    for step in range(min(len(found_path_indices), max_steps)):
        direction_idx = found_path_indices[step]
        
        input_bit = [0, 0, 0, 0]
        input_bit[direction_idx] = 1
        action_queue.append(input_bit)
        
    return action_queue
  
  
  
def mob_display(app,GS,move_map_x,move_map_y):
  gen_x,gen_y = origin(app,GS)
  # print(GS.before_mob)
  for i in range(len(GS.before_mob)):  
    name = GS.before_mob[i][0]
    
    dis_x = app.character[name].Character_conmaas_x - gen_x
    dis_y = app.character[name].Character_conmaas_y - gen_y
    # if i == 1:
    #   print(dis_x,dis_y)
    
    if app.character[name].before_key == None:
      app.character[name].before_key = ""
    
    
    if app.character[name].before_key == "":
      move_x = 0
      move_y = 0
    elif app.character[name].before_key == "A":
      move_x = 1
      move_y = 0
    elif app.character[name].before_key == "D":
      move_x = -1
      move_y = 0
    elif app.character[name].before_key == "W":
      move_x = 0
      move_y = 1
    elif app.character[name].before_key == "S":
      move_x = 0
      move_y = -1
    
        
    
    if app.character[name].memori_2 == 0:
      imag = app.character[name].sub_role + "_A"
    elif app.character[name].memori_2 == 1:
      imag = app.character[name].sub_role + "_D"
    elif app.character[name].memori_2 == 2:
      imag = app.character[name].sub_role + "_W"
    elif app.character[name].memori_2 == 3:
      imag = app.character[name].sub_role + "_S"
    app.image_rect_animation_fps_setting_free_size(imag, 5+dis_x-move_map_x+move_x,dis_y-move_map_y+move_y ,5+dis_x,dis_y, 0,23)
    
    
    
# 雑魚敵    
def weak_enemies(app,GS,name):
  if app.character[name].Initialization == True:
    app.character[name].Initialization = False
    app.character[name].memori_1 = [[0,0,0,0],[0,0,0,0]] # 行動
    app.character[name].memori_2 = 0 # 向き
    app.character[name].memori_0 = 0
    
    app.character[name].HP = 30

  weak_enemies_action(app,GS,name)
  app.character[name].TPS_clock += 1

 
def weak_attack(app,GS,name):
  if 20 <= app.character[name].TPS_clock:
    app.prayer_damage(20)
    if app.character[name].sub_role == "鬼_1":
      app.SE_play("nc426264_打撃音4")
    if app.character[name].sub_role == "唐傘":
      app.SE_play("小化け物の威嚇")
    
    
    app.character[name].TPS_clock = 0
    
    
def weak_enemies_action(app,GS,name):
    
  x = app.character[name].Character_conmaas_x
  y = app.character[name].Character_conmaas_y
      
  view_left  = x - app.wight_mathpiece
  view_right = x + app.wight_mathpiece
  view_up    = y - app.height_mathpiece
  view_down  = y + app.height_mathpiece

  if (app.prayer.Prayer_conmaas_x < view_left) or (view_right < app.prayer.Prayer_conmaas_x) or (app.prayer.Prayer_conmaas_y < view_up) or (view_down < app.prayer.Prayer_conmaas_y):
    app.Crank_up_Character(name)
    GS.mob_count -= 1
    return


  if app.character[name].death_flag == True:
    GS.death_mob += 1
    GS.power_count += 1
    app.Crank_up_Character(name)
    GS.mob_count -= 1
    app.SE_play("神社の鈴") 
    if app.character[name].sub_role == "唐傘":
      GS.kara_count += 1
    elif app.character[name].sub_role == "鬼_1":
      GS.oni_1_count += 1
    return

  if len(app.character[name].memori_1) <= 1:
    app.character[name].memori_1 = bot_input_generator(GS.map_data, (x,y), (app.prayer.Prayer_conmaas_x,app.prayer.Prayer_conmaas_y))

  if not app.character[name].memori_1:
    app.character[name].before_key = ""
    return
    
  element = app.character[name].memori_1.pop(0)
  
  
  if (app.character[name].Character_conmaas_x - 1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x + 1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y + 1):
    weak_attack(app,GS,name) 
      
        
  # [a,d,w,s]
  if element[0] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x-1 and GS.bos[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 0
        app.character[name].Character_conmaas_x -= 1
      else:
        app.character[name].before_key = ""
  elif element[1] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x+1 and GS.bos[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 1
        app.character[name].Character_conmaas_x += 1  
      else:
        app.character[name].before_key = ""
  elif element[2] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x and GS.bos[n][1][1] == app.character[name].Character_conmaas_y-1:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 2
        app.character[name].Character_conmaas_y -= 1
      else:
        app.character[name].before_key = ""
  elif element[3] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x and GS.bos[n][1][1] == app.character[name].Character_conmaas_y+1:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 3
        app.character[name].Character_conmaas_y += 1    
      else:
        app.character[name].before_key = ""
  
  GS.mob.append([name,(app.character[name].Character_conmaas_x,app.character[name].Character_conmaas_y)])
    
    




  
# 小敵  
def Little_Enemy(app,GS,name):
  if app.character[name].Initialization == True:
    app.character[name].Initialization = False
    app.character[name].memori_1 = [[0,0,0,0],[0,0,0,0]] # 行動
    app.character[name].memori_2 = 0 # 向き
    app.character[name].memori_0 = 0
    
    app.character[name].HP = 100

  Little_Enemy_action(app,GS,name)
  app.character[name].TPS_clock += 1

 
def Little_Enemy_weak_attack(app,GS,name):
  if 10 <= app.character[name].TPS_clock:
    app.prayer_damage(50)  
    app.character[name].TPS_clock = 0
    if app.character[name].sub_role == "鬼_2":
      app.SE_play("刀で打ち合う音")
    if app.character[name].sub_role == "大顔":
      app.SE_play("悪魔の笑い声")
    if app.character[name].sub_role == "月人_1":
      app.SE_play("月人")      
      
    
def Little_Enemy_action(app,GS,name):
    
  x = app.character[name].Character_conmaas_x
  y = app.character[name].Character_conmaas_y
      
  view_left  = x - app.wight_mathpiece
  view_right = x + app.wight_mathpiece
  view_up    = y - app.height_mathpiece
  view_down  = y + app.height_mathpiece

  if (app.prayer.Prayer_conmaas_x < view_left) or (view_right < app.prayer.Prayer_conmaas_x) or (app.prayer.Prayer_conmaas_y < view_up) or (view_down < app.prayer.Prayer_conmaas_y):
    app.Crank_up_Character(name)
    GS.mob_count -= 1
    return


  if app.character[name].death_flag == True:
    GS.death_mob += 1
    GS.power_count += 1
    app.Crank_up_Character(name)
    GS.mob_count -= 1
    app.SE_play("神社の鈴") 
    if app.character[name].sub_role == "鬼_2":
      GS.oni_2_count += 1
    elif app.character[name].sub_role == "大顔":
      GS.oogao_count += 1
    elif app.character[name].sub_role == "月人_1":
      GS.tuki_1_count += 1
    return

  if len(app.character[name].memori_1) <= 1:
    app.character[name].memori_1 = bot_input_generator(GS.map_data, (x,y), (app.prayer.Prayer_conmaas_x,app.prayer.Prayer_conmaas_y))

  if not app.character[name].memori_1:
    app.character[name].before_key = ""
    return
    
  element = app.character[name].memori_1.pop(0)
  if (app.character[name].Character_conmaas_x - 1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x + 1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y + 1):
    Little_Enemy_weak_attack(app,GS,name) 
    
  # [a,d,w,s]
  if element[0] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x-1 and GS.bos[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 0
        app.character[name].Character_conmaas_x -= 1
      else:
        app.character[name].before_key = ""
  elif element[1] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
      Little_Enemy_weak_attack(app,GS,name)
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x+1 and GS.bos[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 1
        app.character[name].Character_conmaas_x += 1  
      else:
        app.character[name].before_key = ""
  elif element[2] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
      Little_Enemy_weak_attack(app,GS,name)
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x and GS.bos[n][1][1] == app.character[name].Character_conmaas_y-1:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 2
        app.character[name].Character_conmaas_y -= 1
      else:
        app.character[name].before_key = ""
  elif element[3] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
      Little_Enemy_weak_attack(app,GS,name)
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x and GS.bos[n][1][1] == app.character[name].Character_conmaas_y+1:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 3
        app.character[name].Character_conmaas_y += 1    
      else:
        app.character[name].before_key = ""
  
  GS.mob.append([name,(app.character[name].Character_conmaas_x,app.character[name].Character_conmaas_y)])
    
    


    
# 中敵  
def Middle_enemy(app,GS,name):
  if app.character[name].Initialization == True:
    app.character[name].Initialization = False
    app.character[name].memori_1 = [[0,0,0,0],[0,0,0,0]] # 行動
    app.character[name].memori_2 = 0 # 向き
    app.character[name].memori_0 = 0
    
    app.character[name].HP = 300

  Middle_enemy_action(app,GS,name)
  app.character[name].TPS_clock += 1

# def arch_enemy(app,GS,name):
#   if app.character[name].Initialization == True:
#     app.character[name].Initialization = False
#     app.character[name].memori_1 = [[0,0,0,0],[0,0,0,0]] # 行動
#     app.character[name].memori_2 = 0 # 向き
#     app.character[name].memori_0 = 0
    
#     app.character[name].HP = 300

#   arch_enemy_action(app,GS,name)
#   app.character[name].TPS_clock += 1

 
def crea_stone_iwa(app,GS,name):
  pass
    # be_x = app.prayer.Prayer_conmaas_x - (app.wight_mathpiece//3)-5
    # af_x = app.prayer.Prayer_conmaas_x + (app.wight_mathpiece//3)+5
    # be_y = app.prayer.Prayer_conmaas_y - (app.height_mathpiece//3)-5
    # af_y = app.prayer.Prayer_conmaas_y + (app.height_mathpiece//3)+5
    # app.SE_play("つるはし") 
    # bools = True 
    # for i in range(1):
    #   while bools == True :
    #     mob_x = random.randint(be_x, af_x)
    #     mob_y = random.randint(be_y, af_y)
    #     num = random.randint(0,3)
        
    #     if mob_x <= 4:
    #       continue
    #     elif len(GS.map_data[0])-4 <= mob_x:
    #       continue
    #     if mob_y <= 4:
    #       continue
    #     elif len(GS.map_data)-4 <= mob_y:
    #       continue  
        
    #     GS.map_data[mob_y][mob_x] = [2, ['岩']]
    #     bools = False
         
         
def Middle_enemy_weak_attack(app,GS,name):
  if 20 <= app.character[name].TPS_clock:
    app.prayer_damage(200)
    
    app.character[name].TPS_clock = 0
    if app.character[name].sub_role == "月人_2":
      app.SE_play("月人")      
    if app.character[name].sub_role == "クモ":
      app.SE_play("小化け物の威嚇")         
    if app.character[name].sub_role == "九尾":
      app.SE_play("獣の唸る声")       
    
    
    
    
def Middle_enemy_action(app,GS,name):
    
  x = app.character[name].Character_conmaas_x
  y = app.character[name].Character_conmaas_y
      
  view_left  = x - app.wight_mathpiece
  view_right = x + app.wight_mathpiece
  view_up    = y - app.height_mathpiece
  view_down  = y + app.height_mathpiece

  if (app.prayer.Prayer_conmaas_x < view_left) or (view_right < app.prayer.Prayer_conmaas_x) or (app.prayer.Prayer_conmaas_y < view_up) or (view_down < app.prayer.Prayer_conmaas_y):
    app.Crank_up_Character(name)
    GS.mob_count -= 1
    return


  if app.character[name].death_flag == True:
    GS.death_mob += 1
    GS.power_count += 1
    app.Crank_up_Character(name)
    GS.mob_count -= 1
    app.SE_play("神社の鈴") 
    if app.character[name].sub_role == "月人_2":
      GS.tuki_2_count += 1
    if app.character[name].sub_role == "クモ":
      GS.kumo_count += 1
    if app.character[name].sub_role == "九尾":
      GS.kitune_count += 1      
    return

  if len(app.character[name].memori_1) <= 1:
    app.character[name].memori_1 = bot_input_generator(GS.map_data, (x,y), (app.prayer.Prayer_conmaas_x,app.prayer.Prayer_conmaas_y))

  if not app.character[name].memori_1:
    app.character[name].before_key = ""
    return
    
  element = app.character[name].memori_1.pop(0)
  
  if (app.character[name].Character_conmaas_x - 1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x + 1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y + 1):
    Middle_enemy_weak_attack(app,GS,name) 
    
  probability = random.randint(0, 300)
  
  if 290 <= probability:
    crea_stone_iwa(app,GS,name)    
    
  # [a,d,w,s]
  if element[0] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x-1 and GS.bos[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 0
        app.character[name].Character_conmaas_x -= 1
      else:
        app.character[name].before_key = ""
  elif element[1] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x+1 and GS.bos[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 1
        app.character[name].Character_conmaas_x += 1  
      else:
        app.character[name].before_key = ""
  elif element[2] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x and GS.bos[n][1][1] == app.character[name].Character_conmaas_y-1:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 2
        app.character[name].Character_conmaas_y -= 1
      else:
        app.character[name].before_key = ""
  elif element[3] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x and GS.bos[n][1][1] == app.character[name].Character_conmaas_y+1:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 3
        app.character[name].Character_conmaas_y += 1    
      else:
        app.character[name].before_key = ""
  
  GS.mob.append([name,(app.character[name].Character_conmaas_x,app.character[name].Character_conmaas_y)])
    
    

    
    

# 大敵
def arch_enemy(app,GS,name):
  if app.character[name].Initialization == True:
    app.character[name].Initialization = False
    app.character[name].memori_1 = [[0,0,0,0],[0,0,0,0]] # 行動
    app.character[name].memori_2 = 0 # 向き
    app.character[name].memori_0 = 0
    
    app.character[name].HP = 500

  arch_enemy_action(app,GS,name)
  app.character[name].TPS_clock += 1

 
def crea_stone(app,GS,name):
  pass
    # be_x = app.prayer.Prayer_conmaas_x - (app.wight_mathpiece//3)-5
    # af_x = app.prayer.Prayer_conmaas_x + (app.wight_mathpiece//3)+5
    # be_y = app.prayer.Prayer_conmaas_y - (app.height_mathpiece//3)-5
    # af_y = app.prayer.Prayer_conmaas_y + (app.height_mathpiece//3)+5
    
    # bools = True 
    # app.SE_play("つるはし") 
    # app.SE_play("つるはし") 
    # app.SE_play("つるはし") 
    
    # for i in range(3):
    #   while bools == True :
    #     mob_x = random.randint(be_x, af_x)
    #     mob_y = random.randint(be_y, af_y)
    #     num = random.randint(0,3)
        
    #     if mob_x <= 4:
    #       continue
    #     elif len(GS.map_data[0])-4 <= mob_x:
    #       continue
    #     if mob_y <= 4:
    #       continue
    #     elif len(GS.map_data)-4 <= mob_y:
    #       continue  
        
    #     GS.map_data[mob_y][mob_x] = [2, ['レンガ']]
    #     bools = False
         
         
         
def arch_enemy_weak_attack(app,GS,name):
  if 10 <= app.character[name].TPS_clock:
      if 100 <= GS.efficiency_meter:
            app.prayer_damage(500)  
      elif GS.efficiency_meter <=100:
            app.prayer_damage(300)  
      elif GS.efficiency_meter <= 50:
            app.prayer_damage(200)     
      app.character[name].TPS_clock = 0
      if app.character[name].sub_role == "月人_3":
        app.SE_play("月人")     
      if app.character[name].sub_role == "月人_4":
        app.SE_play("月人")       

    
  
  
def arch_enemy_special_attack(app,GS,name):
  probability = random.randint(0, 200)
  
  if 190 <= probability:
    crea_stone(app,GS,name)
    
  probability = random.randint(0, 100)    
  if 99 <= probability:
    probability = random.randint(0, 2)
    
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
      
      
  
  
    
def arch_enemy_action(app,GS,name):
  
  x = app.character[name].Character_conmaas_x
  y = app.character[name].Character_conmaas_y
      
  view_left  = x - app.wight_mathpiece
  view_right = x + app.wight_mathpiece
  view_up    = y - app.height_mathpiece
  view_down  = y + app.height_mathpiece

  if (app.prayer.Prayer_conmaas_x < view_left) or (view_right < app.prayer.Prayer_conmaas_x) or (app.prayer.Prayer_conmaas_y < view_up) or (view_down < app.prayer.Prayer_conmaas_y):
    app.Crank_up_Character(name)
    GS.mob_count -= 1
    return


  if app.character[name].death_flag == True:
    GS.death_mob += 1
    GS.power_count += 1
    app.Crank_up_Character(name)
    GS.mob_count -= 1
    app.SE_play("神社の鈴") 
    if app.character[name].sub_role == "月人_3":
      GS.tuki_3_count += 3
    if app.character[name].sub_role == "月人_4":
      GS.tuki_4_count += 4
    return

  if len(app.character[name].memori_1) <= 1:
    app.character[name].memori_1 = bot_input_generator(GS.map_data, (x,y), (app.prayer.Prayer_conmaas_x,app.prayer.Prayer_conmaas_y))

  if not app.character[name].memori_1:
    app.character[name].before_key = ""
    return
    
  element = app.character[name].memori_1.pop(0)
  
  if (app.character[name].Character_conmaas_x - 1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x + 1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y + 1):
    arch_enemy_weak_attack(app,GS,name) 
    
  # [a,d,w,s]
  if element[0] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
      app.character[name].before_key = ""
    else:
      app.character[name].before_key = "A"
      arch_enemy_special_attack(app,GS,name)
      break_bool = False
      for n in range(len(GS.before_mob)):
        if GS.before_mob[n][1][0] == app.character[name].Character_conmaas_x-1 and GS.before_mob[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break
      for n in range(len(GS.mob)):
        if GS.mob[n][1][0] == app.character[name].Character_conmaas_x-1 and GS.mob[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x-1 and GS.bos[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 0
        app.character[name].Character_conmaas_x -= 1
      else:
        app.character[name].before_key = ""
  elif element[1] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
      app.character[name].before_key = ""
    else:
      app.character[name].before_key = "D"
      arch_enemy_special_attack(app,GS,name)
      break_bool = False
      for n in range(len(GS.before_mob)):
        if GS.before_mob[n][1][0] == app.character[name].Character_conmaas_x+1 and GS.before_mob[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break
      for n in range(len(GS.mob)):
        if GS.mob[n][1][0] == app.character[name].Character_conmaas_x+1 and GS.mob[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x+1 and GS.bos[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 1
        app.character[name].Character_conmaas_x += 1  
      else:
        app.character[name].before_key = ""
  elif element[2] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
      app.character[name].before_key = ""
    else:
      break_bool = False
      app.character[name].before_key = "W"
      arch_enemy_special_attack(app,GS,name)
      for n in range(len(GS.before_mob)):
        if GS.before_mob[n][1][0] == app.character[name].Character_conmaas_x and GS.before_mob[n][1][1] == app.character[name].Character_conmaas_y-1:
          break_bool = True
          break
      for n in range(len(GS.mob)):
        if GS.mob[n][1][0] == app.character[name].Character_conmaas_x and GS.mob[n][1][1] == app.character[name].Character_conmaas_y-1:
          break_bool = True
          break
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x and GS.bos[n][1][1] == app.character[name].Character_conmaas_y-1:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 2
        app.character[name].Character_conmaas_y -= 1
      else:
        app.character[name].before_key = ""
  elif element[3] == 1:
    if (app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y +1):
      app.character[name].before_key = ""
    else:
      app.character[name].before_key = "S"
      arch_enemy_special_attack(app,GS,name)
      break_bool = False
      for n in range(len(GS.before_mob)):
        if GS.before_mob[n][1][0] == app.character[name].Character_conmaas_x and GS.before_mob[n][1][1] == app.character[name].Character_conmaas_y+1:
          break_bool = True
          break
      for n in range(len(GS.mob)):
        if GS.mob[n][1][0] == app.character[name].Character_conmaas_x and GS.mob[n][1][1] == app.character[name].Character_conmaas_y+1:
          break_bool = True
          break
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x and GS.bos[n][1][1] == app.character[name].Character_conmaas_y+1:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 3
        app.character[name].Character_conmaas_y += 1    
      else:
        app.character[name].before_key = ""
  
  GS.mob.append([name,(app.character[name].Character_conmaas_x,app.character[name].Character_conmaas_y)])
    
    


# 守り手    
def dif_enemies(app,GS,name):
  if app.character[name].Initialization == True:
    app.character[name].Initialization = False
    app.character[name].memori_1 = [[0,0,0,0],[0,0,0,0]] # 行動
    app.character[name].memori_2 = 0 # 向き
    app.character[name].memori_0 = 0
    
    app.character[name].HP = 30

  dif_enemies_action(app,GS,name)
  
  app.character[name].TPS_clock += 1
  if (app.character[name].Character_conmaas_x - 1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x + 1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y - 1) or (app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y + 1):
    Middle_enemy_weak_attack(app,GS,name) 
    

 

    
    
def dif_enemies_action(app,GS,name):
    
  x = app.character[name].Character_conmaas_x
  y = app.character[name].Character_conmaas_y
      
  view_left  = x - app.wight_mathpiece
  view_right = x + app.wight_mathpiece
  view_up    = y - app.height_mathpiece
  view_down  = y + app.height_mathpiece

  if (app.prayer.Prayer_conmaas_x < view_left) or (view_right < app.prayer.Prayer_conmaas_x) or (app.prayer.Prayer_conmaas_y < view_up) or (view_down < app.prayer.Prayer_conmaas_y):
    app.Crank_up_Character(name)
    GS.mob_count -= 1
    return


  if 100 <= app.character[name].TPS_clock:
    app.character["セイメイ"].HP += 100
    app.character["セイメイ"].TPS_clock += 10
    app.character[name].TPS_clock = 0
    if app.character[name].sub_role == "鬼_3":
        app.SE_play("神社の鈴")  

  if app.character[name].death_flag == True:
    GS.death_mob += 1
    GS.power_count += 1
    app.Crank_up_Character(name)
    GS.mob_count -= 1
    app.SE_play("神社の鈴") 
    if app.character[name].sub_role == "鬼_3":
      GS.oni_3_count += 1
    return

  if len(app.character[name].memori_1) <= 1:
    app.character[name].memori_1 = bot_input_generator(GS.map_data, (x,y), (app.character["セイメイ"].Character_conmaas_x-1,app.character["セイメイ"].Character_conmaas_x-1))

  if not app.character[name].memori_1:
    app.character[name].before_key = ""
    return
    
  element = app.character[name].memori_1.pop(0)
  # [a,d,w,s]
  if element[0] == 1:
    if app.character[name].Character_conmaas_x-1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y:
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x-1 and GS.bos[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 0
        app.character[name].Character_conmaas_x -= 1
      else:
        app.character[name].before_key = ""
  elif element[1] == 1:
    if app.character[name].Character_conmaas_x+1 == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y == app.prayer.Prayer_conmaas_y:
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x+1 and GS.bos[n][1][1] == app.character[name].Character_conmaas_y:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 1
        app.character[name].Character_conmaas_x += 1  
      else:
        app.character[name].before_key = ""
  elif element[2] == 1:
    if app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y-1 == app.prayer.Prayer_conmaas_y:
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x and GS.bos[n][1][1] == app.character[name].Character_conmaas_y-1:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 2
        app.character[name].Character_conmaas_y -= 1
      else:
        app.character[name].before_key = ""
  elif element[3] == 1:
    if app.character[name].Character_conmaas_x == app.prayer.Prayer_conmaas_x and app.character[name].Character_conmaas_y+1 == app.prayer.Prayer_conmaas_y:
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
      for n in range(len(GS.bos)):
        if GS.bos[n][1][0] == app.character[name].Character_conmaas_x and GS.bos[n][1][1] == app.character[name].Character_conmaas_y+1:
          break_bool = True
          break     
      if break_bool == False:
        app.character[name].memori_2 = 3
        app.character[name].Character_conmaas_y += 1    
      else:
        app.character[name].before_key = ""
  
  GS.mob.append([name,(app.character[name].Character_conmaas_x,app.character[name].Character_conmaas_y)])
    
    

