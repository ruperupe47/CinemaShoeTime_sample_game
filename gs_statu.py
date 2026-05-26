import efect_dis
import random
import mob

# タイトル
## 用意するもの(BGM,タイトル画像,背景画像)
def statu_title(app,GS):
  GS.rogic_clock += 1
  # タイトル ((25*20)*(5*20))
  wx = 15
  app.set_color(255)
  app.rect_free((22-wx)*app.math_size+app.math_size,5*app.math_size,(2*wx)*app.math_size-app.math_size,5*app.math_size)
  app.set_color(0)
  app.texts_free("シチューにカツを見出す","60_font",(22-14+2)*app.math_size,5*app.math_size)  
  
  
  # クリックしてください表示
  # wx = 10
  # app.set_color(255)
  # app.rect_free((22-wx)*app.math_size,23*app.math_size,(2*wx)*app.math_size,3*app.math_size)  
  app.set_color(0)
  app.texts_free("click the screen to start","60_font",(22-14)*app.math_size,22*app.math_size)
  
  if 2 <= GS.rogic_clock and app.click_now_bool == False:
    GS.rogic_clock = 0
    GS.status = "blick"
    GS.begore_status = "タイトル"
    app.SE_play("タイトルクリック") 
  
  if GS.debag == True:
    app.set_color(255)
    app.rect_free(0*app.math_size,0*app.math_size,22*app.math_size,1*app.math_size)
    app.set_color(0)
    app.rect_free(22*app.math_size,0*app.math_size,22*app.math_size,1*app.math_size) 
    
    

# 説明画面の共通化
## 用意するもの(BGM,タイトル画像のぼかし,案内画像の増やし)
def explanation_parts(app,GS,part):
  GS.new_part = part # テスト用

  if GS.new_part != None:
    move_wh = GS.new_part - GS.part
    # print(GS.new_part)
  else:
    move_wh = 0
    GS.part = 0
    GS.new_part = 0

  # 画像1
  part = 0
  for i in range(7):
    # 説明写真
    app.set_color(255)
    # app.rect_animation_fps_setting_free_size(4+(40*part)+(40*GS.part),1,4+(40*part)+(40*move_wh)+(40*GS.part),1,0,app.fps,36,22)
    img = "スライド" + str(i+1)
    # app.image_rect_animation_fps_setting_free_size(img,4+(40*part)+(40*GS.part),1,4+(40*part)-(40*move_wh)+(40*GS.part),1,0,app.fps)  
    # app.image_rect_animation_fps_setting_free_size(img,4+(40*part)+(40*GS.part),1,4+(40*part)+(40*GS.new_part),1,0,app.fps)  
    app.image_rect_animation_fps_setting_free_size(img,4+(40*part)-(40*GS.part),1,4+(40*part)-(40*GS.part)-(40*move_wh),1,0,app.fps)  
    part += 1
  
  GS.part = GS.new_part

  
    

# 説明画面 
def statu_explanation(app,GS):
  # GS.part = 0
  
  # print(GS.part)
  GS.rogic_clock += 1
  if (app.before_Arrow_keys[0] == 1 or app.before_atoz_list[0] == 1) and 2 <= GS.rogic_clock:
    GS.new_part -= 1
    GS.rogic_clock = 0
  if (app.before_Arrow_keys[1] == 1 or app.before_atoz_list[3] == 1) and 2 <= GS.rogic_clock:
    GS.new_part += 1
    GS.rogic_clock = 0
    
  if GS.new_part <= 0:
    GS.new_part = 0
  elif 7 <= GS.new_part:
    GS.new_part = 6
    
  explanation_parts(app,GS,GS.new_part)
  
  if GS.debag == True:
    app.set_color(255)
    app.rect_free(0*app.math_size,0*app.math_size,22*app.math_size,1*app.math_size)
    app.set_color(0)
    app.rect_free(22*app.math_size,0*app.math_size,22*app.math_size,1*app.math_size) 
    
  WH = 8
  
  if GS.part == 6:
    print(app.Tracking_mouse_pos[0])
    print(GS.new_part)
    if 13 <= (app.Tracking_mouse_pos[0]//app.math_size) and (app.Tracking_mouse_pos[0]//app.math_size) <= 28 and 26 <= (app.Tracking_mouse_pos[1]//app.math_size) and (app.Tracking_mouse_pos[1]//app.math_size) <= 28 and GS.new_part == 6:
      app.set_color(240,131,0)
      if app.click_now_bool == False:
        GS.status = "blick"
        GS.begore_status = "説明"
    else:
      app.set_color(0)
    app.rect_free((21-WH)*app.math_size,26*app.math_size,(WH*2)*app.math_size,3*app.math_size)
    app.set_color(255)
    app.rect_free((21-WH)*app.math_size+5,26*app.math_size+5,(WH*2)*app.math_size-10,3*app.math_size-10)
  
    app.set_color(0)
    app.texts_free("click to start","60_font",(14)*app.math_size,26*app.math_size-5)
    
    
    

# ポーズ画面
def statu_pose(app,GS):
  # GS.part = 0
  GS.rogic_clock += 1
  # print(GS.part)
  if (app.before_Arrow_keys[0] == 1 or app.before_atoz_list[0] == 1) and 2 <= GS.rogic_clock:
    GS.new_part -= 1
    GS.rogic_clock = 0
  if (app.before_Arrow_keys[1] == 1 or app.before_atoz_list[3] == 1) and 2 <= GS.rogic_clock:
    GS.new_part += 1
    GS.rogic_clock = 0
    
    
  if GS.new_part <= 0:
    GS.new_part = 0
  elif 7 <= GS.new_part:
    GS.new_part = 6
    
  explanation_parts(app,GS,GS.new_part)
  

  print(app.Tracking_mouse_pos[0])
  print(GS.new_part)
  if 4 <= (app.Tracking_mouse_pos[0]//app.math_size) and (app.Tracking_mouse_pos[0]//app.math_size) <= 19 and 26 <= (app.Tracking_mouse_pos[1]//app.math_size) and (app.Tracking_mouse_pos[1]//app.math_size) <= 28:
      app.set_color(240,131,0)
      if app.click_now_bool == False:
        GS.status = "ポーズ_0"
        GS.begore_status = "ポーズ_1"
        GS.rogic_clock = 0
  else:
      app.set_color(0)
      
  app.rect_free((4)*app.math_size,26*app.math_size,(16)*app.math_size,3*app.math_size)
  app.set_color(255)
  app.rect_free((4)*app.math_size+5,26*app.math_size+5,(16)*app.math_size-10,3*app.math_size-10)
  
  app.set_color(0)
  app.texts_free("ゲームに戻る","60_font",(5)*app.math_size,26*app.math_size-5)
    
  if 23 <= (app.Tracking_mouse_pos[0]//app.math_size) and (app.Tracking_mouse_pos[0]//app.math_size) <= 38 and 26 <= (app.Tracking_mouse_pos[1]//app.math_size) and (app.Tracking_mouse_pos[1]//app.math_size) <= 28:
      app.set_color(240,131,0)
      if app.click_now_bool == False:
        GS.status = "ポーズ_1"
        GS.begore_status = "ポーズ_1"
        GS.rogic_clock = 0
        for name,obj in app.character.items():
          app.Crank_up_Character(name)
          app.Crank_up()
  else:
      app.set_color(0)
      
  app.rect_free((23)*app.math_size,26*app.math_size,(16)*app.math_size,3*app.math_size)
  app.set_color(255)
  app.rect_free((23)*app.math_size+5,26*app.math_size+5,(16)*app.math_size-10,3*app.math_size-10)
  
  app.set_color(0)
  app.texts_free("タイトルへ","60_font",(24)*app.math_size,26*app.math_size-5)
  
        
  if GS.debag == True:
    app.set_color(255)
    app.rect_free(0*app.math_size,0*app.math_size,22*app.math_size,1*app.math_size)
    app.set_color(0)
    app.rect_free(22*app.math_size,0*app.math_size,22*app.math_size,1*app.math_size)
    
    
# エンドのスコア画面
## 用意するもの(BGM,タイトル画像のぼかし)
def statu_end_scorea(app,GS):
  # スコア画面(36*25)*(22*25)
  wx = 18
  app.set_color(255)
  app.rect_free((22-wx)*app.math_size,4*app.math_size,(2*wx)*app.math_size,22*app.math_size)   
  app.image_rect_animation_fps_setting_free_size("エンドスコア",4,5,4,5,0,app.fps) 
  
  app.noStroke()
  app.set_color(125)
  app.rect_free((4)*app.math_size,26*app.math_size,(50)*app.math_size,50*app.math_size)   
  app.set_stroke_color(0) 
  
  app.set_color(0)
  app.texts_free(str(GS.death_mob),"60_font",(21)*app.math_size,7*app.math_size-5)  
  
  app.set_color(0)
  app.texts_free(str(GS.kara_count),"30_font",(12)*app.math_size+10,13*app.math_size-5)  
  app.set_color(0)
  app.texts_free(str(GS.oni_1_count),"30_font",(12)*app.math_size+10,16*app.math_size-5)    
  app.set_color(0)
  app.texts_free(str(GS.oni_2_count),"30_font",(12)*app.math_size+10,20*app.math_size-5)    
  app.set_color(0)
  app.texts_free(str(GS.oni_3_count),"30_font",(12)*app.math_size+10,23*app.math_size-5)      
  
  app.set_color(0)
  app.texts_free(str(GS.kumo_count),"30_font",(12+11)*app.math_size+10,13*app.math_size-5)  
  app.set_color(0)
  app.texts_free(str(GS.kitune_count),"30_font",(12+11)*app.math_size+10,16*app.math_size-5)    
  app.set_color(0)
  app.texts_free(str(GS.oogao_count),"30_font",(12+11)*app.math_size+10,20*app.math_size-5)    
  app.set_color(0)
  app.texts_free(str(GS.tuki_1_count),"30_font",(12+11)*app.math_size+10,23*app.math_size-5)      
 
  app.set_color(0)
  app.texts_free(str(GS.tuki_2_count),"30_font",(12+12+12)*app.math_size+10,13*app.math_size-5)  
  app.set_color(0)
  app.texts_free(str(GS.tuki_3_count),"30_font",(12+12+12)*app.math_size+10,16*app.math_size-5)    
  app.set_color(0)
  app.texts_free(str(GS.tuki_4_count),"30_font",(12+12+12)*app.math_size+10,20*app.math_size-5)    

          
  # 額縁
  app.noStroke()
  app.set_color(152,97,63)
  app.rect_free((22-wx)*app.math_size,4*app.math_size,(2*wx)*app.math_size,1*app.math_size) 
  app.rect_free((22-wx)*app.math_size,25*app.math_size,(2*wx)*app.math_size,1*app.math_size) 
  app.rect_free((22-wx)*app.math_size,4*app.math_size,1*app.math_size,22*app.math_size) 
  app.rect_free((22+wx-1)*app.math_size,4*app.math_size,1*app.math_size,22*app.math_size) 
  app.set_stroke_color(0) 
  app.line_display((22-wx)*app.math_size,4*app.math_size,40*app.math_size,4*app.math_size)
  app.line_display((22-wx)*app.math_size,4*app.math_size,(22-wx)*app.math_size,26*app.math_size)
  app.line_display((22-wx)*app.math_size,26*app.math_size,40*app.math_size,26*app.math_size)
  app.line_display(40*app.math_size,4*app.math_size,40*app.math_size,26*app.math_size)
  
  WH = 8
  if True:
    print(app.Tracking_mouse_pos[0])
    print(GS.new_part)
    if 13 <= (app.Tracking_mouse_pos[0]//app.math_size) and (app.Tracking_mouse_pos[0]//app.math_size) <= 28 and 26 <= (app.Tracking_mouse_pos[1]//app.math_size) and (app.Tracking_mouse_pos[1]//app.math_size) <= 28:
      app.set_color(240,131,0)
      if app.click_now_bool == False:
        GS.status = "blick"
        GS.begore_status = "黒"
    else:
      app.set_color(0)
    app.rect_free((21-WH)*app.math_size,26*app.math_size,(WH*2)*app.math_size,3*app.math_size)
    app.set_color(255)
    app.rect_free((21-WH)*app.math_size+5,26*app.math_size+5,(WH*2)*app.math_size-10,3*app.math_size-10)
  
    app.set_color(0)
    app.texts_free("タイトルへ","60_font",(14)*app.math_size,26*app.math_size-5)
  
  if GS.debag == True:
    app.set_color(255)
    app.rect_free(0*app.math_size,0*app.math_size,22*app.math_size,1*app.math_size)
    app.set_color(0)
    app.rect_free(22*app.math_size,0*app.math_size,22*app.math_size,1*app.math_size)
    
  

  
def battle_action(app, GS):
  bool = True

  mp = app.prayer.memori_1
  if app.prayer.memori_1 <= -1:
  #  x = -1
    x = app.prayer.memori_1
  elif app.prayer.memori_1 == 0:
    x = 0
  elif 1 <=  app.prayer.memori_1:
    x = 1
    x = app.prayer.memori_1
  
  cou = 0
  while bool:
    if app.prayer.Prayer_conmaas_x <= 16:
      dis_x = app.prayer.Prayer_conmaas_x - mp
      dis_map_x = 0
      move_ply_x = x
      move_map_x = 0
      
    elif app.prayer.Prayer_conmaas_x <= 17:
      if app.prayer.memori_1 <= -1:
        dis_x = 17
        dis_map_x = app.prayer.Prayer_conmaas_x - 17 - mp
        move_ply_x = 0
        move_map_x = -x        
      elif app.prayer.memori_1 == 0:
        dis_x = app.prayer.Prayer_conmaas_x - mp
        dis_map_x = 0
        move_ply_x = x
        move_map_x = 0      
      elif 1 <=  app.prayer.memori_1:
        dis_x = app.prayer.Prayer_conmaas_x - mp
        dis_map_x = 0
        move_ply_x = x
        move_map_x = 0      
        
    elif app.prayer.Prayer_conmaas_x <= 189:
        dis_x = 17
        dis_map_x = app.prayer.Prayer_conmaas_x - 17 - mp
        move_ply_x = 0
        move_map_x = -x

    elif app.prayer.Prayer_conmaas_x <= 190:
      if app.prayer.memori_1 <= -1:
        dis_x = app.prayer.Prayer_conmaas_x - 173 - mp
        dis_map_x = 173
        move_ply_x = x
        move_map_x = 0        
      elif app.prayer.memori_1 == 0:
        dis_x = 17
        dis_map_x = app.prayer.Prayer_conmaas_x - 17 - mp
        move_ply_x = 0
        move_map_x = -x
      elif 1 <=  app.prayer.memori_1:
        dis_x = 17
        dis_map_x = app.prayer.Prayer_conmaas_x - 17 - mp
        move_ply_x = 0
        move_map_x = -x

    elif app.prayer.Prayer_conmaas_x <= 203:
        dis_x = app.prayer.Prayer_conmaas_x - 173 - mp
        dis_map_x = 173
        move_ply_x = x
        move_map_x = 0
        
    app.prayer.memori_1 -= 1
    cou += 1
    if app.prayer.memori_1 <= 0:
      bool = False
      app.prayer.memori_1 = 0               
               
               
  bool = True

  mp = app.prayer.memori_2
  if app.prayer.memori_2 <= -1:
  #  y = -1
   y = app.prayer.memori_2
  elif app.prayer.memori_2 == 0:
    y = 0
  elif 1 <=  app.prayer.memori_2:
    # y = 1
    y = app.prayer.memori_2
  
  cou = 0
  while bool:
    if app.prayer.Prayer_conmaas_y <= 10:
      dis_y = app.prayer.Prayer_conmaas_y - mp
      dis_map_y = 0
      move_ply_y = y
      move_map_y = 0
      
    elif app.prayer.Prayer_conmaas_y <= 11:
      if app.prayer.memori_2 <= -1:
        dis_y = 11
        dis_map_y = app.prayer.Prayer_conmaas_y - 11 - mp
        move_ply_y = 0
        move_map_y = -y      
      elif app.prayer.memori_2 == 0:
        dis_y = app.prayer.Prayer_conmaas_y - mp
        dis_map_y = 0
        move_ply_y = y
        move_map_y = 0      
      elif 1 <=  app.prayer.memori_2:
        dis_y = app.prayer.Prayer_conmaas_y - mp
        dis_map_y = 0
        move_ply_y = y
        move_map_y = 0      
              
    elif app.prayer.Prayer_conmaas_y <= 290:
        dis_y = 11
        dis_map_y = app.prayer.Prayer_conmaas_y - 11 - mp
        move_ply_y = 0
        move_map_y = -y

    elif app.prayer.Prayer_conmaas_y <= 291:
      if app.prayer.memori_2 <= -1:
        dis_y = app.prayer.Prayer_conmaas_y - 280 - mp
        dis_map_y = 280
        move_ply_y = y
        move_map_y = 0        
      elif app.prayer.memori_2 == 0:
        dis_y = 11
        dis_map_y = app.prayer.Prayer_conmaas_y - 11 - mp
        move_ply_y = 0
        move_map_y = -y
      elif 1 <=  app.prayer.memori_2:
        dis_y= 11
        dis_map_y = app.prayer.Prayer_conmaas_y - 11 - mp
        move_ply_y = 0
        move_map_y = -y
        
    elif app.prayer.Prayer_conmaas_y <= 300:
        dis_y = app.prayer.Prayer_conmaas_y - 280 - mp
        dis_map_y = 280
        move_ply_y = y
        move_map_y = 0        
        
    app.prayer.memori_2 -= 1
    cou += 1
    if app.prayer.memori_2 <= 0:
      bool = False
      app.prayer.memori_2 = 0         
               
  # print(app.prayer.Prayer_conmaas_x,app.prayer.Prayer_conmaas_y)
  # print(dis_map_x,dis_map_y)
  app.limit_map_display_animationn_fps_setting(GS.map_data, 5,0, 0+dis_map_x,0+dis_map_y ,32+dis_map_x,22+dis_map_y, move_map_x,move_map_y ,0,23,1)
  # app.rect_animation_fps_setting(5+dis_x,0+dis_y, 5+dis_x+move_ply_x,0+dis_y+move_ply_y ,0,23 , 1)  
  
  efect_dis.under_efect_display(app,GS,move_map_x,move_map_y)
  
  if app.prayer.memori_4 == "合体":
    app.prayer.memori_4 = ""
    bools = True
    while bools == True:
        num_1 = random.randint(0,3)
        
        if num_1 == 0:# A
          if app.prayer.Prayer_conmaas_x <= 50:
            continue
          p_1 = "_A"
          move_ply_x_1 = -20
          move_ply_y_1 = 0
          
        if num_1 == 1:# D 
          if len(GS.map_data[0])-1 <= app.prayer.Prayer_conmaas_x + 50:
            continue
          p_1 = "_D"
          move_ply_x_1 = 20
          move_ply_y_1 = 0
                  
        if num_1 == 2:# W
          if app.prayer.Prayer_conmaas_y <= 50:
            continue
          p_1 = "_W"
          move_ply_x_1 = 0
          move_ply_y_1 = -20

        if num_1 == 3:# S
          if len(GS.map_data)-1 <= app.prayer.Prayer_conmaas_y + 50:
            continue    
          p_1 = "_S"
          move_ply_x_1 = 0
          move_ply_y_1 = 20
          
        num_2 = random.randint(0,3)
        
        if num_1 == num_2:
          continue
        
        if num_2 == 0:# A
          if app.prayer.Prayer_conmaas_x <= 50:
            continue
          p_2 = "_A"
          move_ply_x_2 = -20
          move_ply_y_2 = 0

        if num_2 == 1:# D 
          if len(GS.map_data[0])-1 <= app.prayer.Prayer_conmaas_x + 50:
            continue
          p_2 = "_D"
          move_ply_x_2 = 20
          move_ply_y_2 = 0
        
        if num_2 == 2:# W
          if app.prayer.Prayer_conmaas_y <= 50:
            continue
          p_2 = "_W"
          move_ply_x_2 = 0
          move_ply_y_2 = -20

        if num_2 == 3:# S
          if len(GS.map_data)-1 <= app.prayer.Prayer_conmaas_y + 50:
            continue  
          p_2 = "_S" 
          move_ply_x_2 = 0
          move_ply_y_2 = 20
        bools = False
    
    if app.prayer.memori_3 == "オウエンペラー":
      # app.image_rect_animation_fps_setting_free_size("カイザー号"+p_1,5+dis_x,0+dis_y, 5+dis_x+move_ply_x_1,0+dis_y+move_ply_y_1 ,0,23)  
      # app.image_rect_animation_fps_setting_free_size("ミカド号"+p_2,5+dis_x,0+dis_y, 5+dis_x+move_ply_x_2,0+dis_y+move_ply_y_2 ,0,23)  
      app.image_rect_animation_fps_setting_free_size("カイザー号"+p_1,5+dis_x+move_ply_x_1,0+dis_y+move_ply_y_1, 5+dis_x,0+dis_y ,0,23)  
      app.image_rect_animation_fps_setting_free_size("ミカド号"+p_2,5+dis_x+move_ply_x_2,0+dis_y+move_ply_y_2, 5+dis_x,0+dis_y ,0,23)  
    elif app.prayer.memori_3 == "オウカイザー":
      app.image_rect_animation_fps_setting_free_size("エンペラー号"+p_1,5+dis_x+move_ply_x_1,0+dis_y+move_ply_y_1, 5+dis_x,0+dis_y ,0,23)  
      app.image_rect_animation_fps_setting_free_size("ミカド号"+p_2,5+dis_x+move_ply_x_2,0+dis_y+move_ply_y_2, 5+dis_x,0+dis_y ,0,23)  
    elif app.prayer.memori_3 == "オウミカド":
      app.image_rect_animation_fps_setting_free_size("カイザー号"+p_1,5+dis_x+move_ply_x_1,0+dis_y+move_ply_y_1, 5+dis_x,0+dis_y ,0,23)  
      app.image_rect_animation_fps_setting_free_size("エンペラー号"+p_2,5+dis_x+move_ply_x_2,0+dis_y+move_ply_y_2, 5+dis_x,0+dis_y ,0,23)  
    app.SE_play("飛行音") 
    app.SE_play("飛行音") 

  elif app.prayer.memori_4 == "分離":
    app.prayer.memori_4 = ""
    bools = True
    while bools == True:
        num_1 = random.randint(0,3)
        
        if num_1 == 0:# A
          if app.prayer.Prayer_conmaas_x <= 50:
            continue
          p_1 = "_A"
          move_ply_x_1 = -20
          move_ply_y_1 = 0
          
        if num_1 == 1:# D 
          if len(GS.map_data[0])-1 <= app.prayer.Prayer_conmaas_x + 50:
            continue
          p_1 = "_D"
          move_ply_x_1 = 20
          move_ply_y_1 = 0
                  
        if num_1 == 2:# W
          if app.prayer.Prayer_conmaas_y <= 50:
            continue
          p_1 = "_W"
          move_ply_x_1 = 0
          move_ply_y_1 = -20

        if num_1 == 3:# S
          if len(GS.map_data)-1 <= app.prayer.Prayer_conmaas_y + 50:
            continue    
          p_1 = "_S"
          move_ply_x_1 = 0
          move_ply_y_1 = 20
          
        num_2 = random.randint(0,3)
        
        if num_1 == num_2:
          continue
        
        if num_2 == 0:# A
          if app.prayer.Prayer_conmaas_x <= 50:
            continue
          p_2 = "_A"
          move_ply_x_2 = -20
          move_ply_y_2 = 0

        if num_2 == 1:# D 
          if len(GS.map_data[0])-1 <= app.prayer.Prayer_conmaas_x + 50:
            continue
          p_2 = "_D"
          move_ply_x_2 = 20
          move_ply_y_2 = 0
        
        if num_2 == 2:# W
          if app.prayer.Prayer_conmaas_y <= 50:
            continue
          p_2 = "_W"
          move_ply_x_2 = 0
          move_ply_y_2 = -20

        if num_2 == 3:# S
          if len(GS.map_data)-1 <= app.prayer.Prayer_conmaas_y + 50:
            continue  
          p_2 = "_S" 
          move_ply_x_2 = 0
          move_ply_y_2 = 20
        bools = False
    
    if app.prayer.memori_3 == "エンペラー号":
      app.image_rect_animation_fps_setting_free_size("カイザー号"+p_1,5+dis_x,0+dis_y, 5+dis_x+move_ply_x_1,0+dis_y+move_ply_y_1 ,0,23)  
      app.image_rect_animation_fps_setting_free_size("ミカド号"+p_2,5+dis_x,0+dis_y, 5+dis_x+move_ply_x_2,0+dis_y+move_ply_y_2 ,0,23)  
    elif app.prayer.memori_3 == "カイザー号":
      app.image_rect_animation_fps_setting_free_size("エンペラー号"+p_1,5+dis_x,0+dis_y, 5+dis_x+move_ply_x_1,0+dis_y+move_ply_y_1 ,0,23)  
      app.image_rect_animation_fps_setting_free_size("ミカド号"+p_2,5+dis_x,0+dis_y, 5+dis_x+move_ply_x_2,0+dis_y+move_ply_y_2 ,0,23)  
    elif app.prayer.memori_3 == "ミカド号":
      app.image_rect_animation_fps_setting_free_size("カイザー号"+p_1,5+dis_x,0+dis_y, 5+dis_x+move_ply_x_1,0+dis_y+move_ply_y_1 ,0,23)  
      app.image_rect_animation_fps_setting_free_size("エンペラー号"+p_2,5+dis_x,0+dis_y, 5+dis_x+move_ply_x_2,0+dis_y+move_ply_y_2 ,0,23)  
    app.SE_play("飛行音") 
    app.SE_play("飛行音") 
  
  
  app.image_rect_animation_fps_setting_free_size(app.prayer.prayer_img,5+dis_x,0+dis_y, 5+dis_x+move_ply_x,0+dis_y+move_ply_y ,0,23)  




  mob.mob_display(app,GS,move_map_x,move_map_y)
  efect_dis.efect_display(app,GS,move_map_x,move_map_y) 
  
  
  
  
  for _ in range(5):
    if GS.mob_count <= 50:
    # if GS.mob_count <= 100:
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
      
      ### さぶロール追加
      if GS.efficiency_meter <=30:
        x = random.randint(0, 5)
        if x <= 4:
          app.character[name].role = "雑魚敵"
          sub = random.randint(0, 1)
          if sub == 0:
            app.character[name].sub_role = "鬼_1"
          elif sub == 1:
            app.character[name].sub_role = "唐傘"
        else:
          app.character[name].role = "小敵"
          sub = random.randint(0, 2)
          if sub == 0:
            app.character[name].sub_role = "鬼_2"
          elif sub == 1:
            app.character[name].sub_role = "大顔"
          else:
            app.character[name].sub_role = "月人_1"
            
      elif GS.efficiency_meter <=50:
        x = random.randint(0, 10)
        if x <= 5:
          app.character[name].role = "小敵"
          sub = random.randint(0, 2)
          if sub == 0:
            app.character[name].sub_role = "鬼_2"
          elif sub == 1:
            app.character[name].sub_role = "大顔"
          else:
            app.character[name].sub_role = "月人_1"
        elif x<= 8:
          app.character[name].role = "中敵"
          sub = random.randint(0, 2)
          if sub == 0:
            app.character[name].sub_role = "九尾"
          elif sub == 1:
            app.character[name].sub_role = "クモ"
          else:
            app.character[name].sub_role = "月人_2"
        else:
          app.character[name].role = "大敵"
          sub = random.randint(0, 1)
          if sub == 0:
            app.character[name].sub_role = "月人_3"
          elif sub == 1:
            app.character[name].sub_role = "月人_4"
      else:
        x = random.randint(0, 10)
        if x<= 7:
          app.character[name].role = "中敵"
          sub = random.randint(0, 2)
          if sub == 0:
            app.character[name].sub_role = "九尾"
          elif sub == 1:
            app.character[name].sub_role = "クモ"
          else:
            app.character[name].sub_role = "月人_2"
        else:
          app.character[name].role = "大敵"
          sub = random.randint(0, 1)
          if sub == 0:
            app.character[name].sub_role = "月人_3"
          elif sub == 1:
            app.character[name].sub_role = "月人_4"
    else:
      bools = False
      break
   
   
  
# ゲーム画面
def statu_game(app,GS):
  # 実動作
  battle_action(app,GS)
  
  # ウインドウ下地
  app.noStroke()
  app.set_color(125)
  app.rect_free(0*app.math_size,0*app.math_size,44*app.math_size,1*app.math_size)
  app.rect_free(0*app.math_size,0*app.math_size,6*app.math_size,30*app.math_size)
  app.rect_free(38*app.math_size,0*app.math_size,6*app.math_size,30*app.math_size)
  app.rect_free(0*app.math_size,23*app.math_size,44*app.math_size,7*app.math_size)
  
  # ウインドウ枠
  app.set_color(152,97,63)
  app.rect_free(6*app.math_size,1*app.math_size,32*app.math_size,1*app.math_size) 
  app.rect_free(6*app.math_size,22*app.math_size,32*app.math_size,1*app.math_size)
  app.rect_free(6*app.math_size,1*app.math_size,1*app.math_size,22*app.math_size)
  app.rect_free(37*app.math_size,1*app.math_size,1*app.math_size,22*app.math_size)
  app.set_stroke_color(0) 
  app.line_display(6*app.math_size,1*app.math_size,38*app.math_size,1*app.math_size)
  app.line_display(6*app.math_size,1*app.math_size,6*app.math_size,23*app.math_size)
  app.line_display(6*app.math_size,23*app.math_size,38*app.math_size,23*app.math_size)
  app.line_display(38*app.math_size,1*app.math_size,38*app.math_size,23*app.math_size) 

  # パラメータータイル
  app.set_color(105,190,120)
  app.rect_free(0*app.math_size,2*app.math_size,5*app.math_size,20*app.math_size)  
  app.rect_free(39*app.math_size,2*app.math_size,5*app.math_size,20*app.math_size)
  app.rect_free(6*app.math_size,24*app.math_size,32*app.math_size,5*app.math_size)  
  
  # パラメーター
  ## HP
  app.set_color(0)
  app.texts_free("HP","default_font",0*app.math_size+10,3*app.math_size-10)
  app.rect_free(0*app.math_size,4*app.math_size,5*app.math_size,2*app.math_size)
  # HPメーター
  if app.prayer.HP <= 5*app.math_size:
    HPs = app.prayer.HP
    app.set_color(255,90,90)
  else:
    HPs = 5*app.math_size
    app.set_color(230,180,90)
  app.rect_free(0*app.math_size,4*app.math_size+1,HPs,2*app.math_size-2)

  ## エネルギー
  app.set_color(0)
  app.texts_free("エネルギーメーター","13_font",0*app.math_size+5,7*app.math_size-5)
  app.rect_free(0*app.math_size,8*app.math_size,5*app.math_size,2*app.math_size)
  ## エネルギーメーター
  app.set_color(0,255,50)
  if app.prayer.energy <= 5*app.math_size:
    energy  = app.prayer.energy 
    app.set_color(34 ,230 ,164)
  else:
    energy  = 5*app.math_size
    app.set_color(0,255,50)
  app.rect_free(0*app.math_size,8*app.math_size+1,energy,2*app.math_size-2)
  
  ## 出力効率
  app.set_color(0)
  app.texts_free("出力効率","default_font",0*app.math_size+5,11*app.math_size-10)
  app.rect_free(0*app.math_size,12*app.math_size,5*app.math_size,2*app.math_size)
  app.set_color(240)
  app.rect_free(0*app.math_size,12*app.math_size+1,5*app.math_size,2*app.math_size-2)
  ## 出力効率メーター
  app.set_color(0)
  app.texts_free(str(GS.efficiency_meter),"40_font",0*app.math_size+5,12*app.math_size-10)
  app.texts_free("%","40_font",3*app.math_size+5,12*app.math_size-10)
  
  ## エンタキーフラグ
  app.set_color(0)
  app.texts_free("エンタキーフラグ","13_font",0*app.math_size+5,15*app.math_size-10)
  app.set_color(255)
  app.rect_free(2*app.math_size,16*app.math_size,2*app.math_size,2*app.math_size)
  if GS.enter_parameter == True:
    app.set_color(238,120,0)
  else:
    app.set_color(255)
  app.rect_free(2*app.math_size+5,16*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
  
  ## ポーズキー
  app.set_color(0)
  app.texts_free("ポーズキーはPキー","13_font",0*app.math_size+5,19*app.math_size-10)
  
  
  # 値パラメータ
  ## HP
  app.set_color(255)
  app.rect_free(39*app.math_size,4*app.math_size,5*app.math_size,2*app.math_size)
  # HPメーター
  app.set_color(0)
  app.texts_free("HP","default_font",39*app.math_size+10,3*app.math_size-10)
  app.texts_free(str(app.prayer.HP),"40_font",39*app.math_size+5,4*app.math_size-10)
  

  ## エネルギー量
  app.set_color(255)
  app.rect_free(39*app.math_size,8*app.math_size,5*app.math_size,2*app.math_size)
  # エネルギー量
  app.set_color(0)
  app.texts_free("エネルギー量","default_font",39*app.math_size+2,7*app.math_size-10)
  app.texts_free(str(app.prayer.energy ),"40_font",39*app.math_size+2,8*app.math_size-10)
  
  ## 攻撃力
  if app.prayer.role == "エンペラー":
    da = 20 + GS.plus_damage
  elif app.prayer.role == "カイザー":
    da = 10 + GS.plus_damage
  elif app.prayer.role == "ミカド":
    da = 10 + GS.plus_damage
  else:
    da = 0
    
  app.set_color(255)
  app.rect_free(39*app.math_size,12*app.math_size,5*app.math_size,2*app.math_size)
  # 攻撃力メーター
  app.set_color(0)
  app.texts_free("攻撃力","default_font",39*app.math_size+10,11*app.math_size-10)
  app.texts_free(str(da),"40_font",39*app.math_size+5,12*app.math_size-10)
  

  ## 防御力
  app.set_color(255)
  app.rect_free(39*app.math_size,16*app.math_size,5*app.math_size,2*app.math_size)
  # 防御力
  app.set_color(0)
  app.texts_free("防御力","default_font",39*app.math_size+10,15*app.math_size-10)
  app.texts_free(str(app.prayer.defence),"40_font",39*app.math_size+5,16*app.math_size-10)
  
  # スキルボックス
  # if 2 <= GS.clock:
  #   skip = True
  # else:
  #   skip = False
    
    
  if GS.lock == True:
    skip = False
  else:
    skip = True
    
  app.set_color(0)
  app.texts_free("キーナンバー","13_font",6*app.math_size+5,27*app.math_size)
  app.texts_free("技名","13_font",6*app.math_size+5,28*app.math_size)
      
  if app.prayer.role == "エンペラー":
    app.set_color(0)
    app.texts_free("0","13_font",11*app.math_size+5,27*app.math_size)
    app.texts_free("分離","13_font",11*app.math_size+5,28*app.math_size)
    
    app.texts_free("1","13_font",15*app.math_size+5,27*app.math_size)
    app.texts_free("オウビーム","13_font",15*app.math_size+5,28*app.math_size)
  
    app.texts_free("2","13_font",19*app.math_size+5,27*app.math_size)
    app.texts_free("オウブーメラン","13_font",19*app.math_size+5,28*app.math_size)  
  
    app.texts_free("3","13_font",24*app.math_size+5,27*app.math_size)
    app.texts_free("エンペラーカッター","13_font",24*app.math_size+5,28*app.math_size)  
  
    app.texts_free("4","13_font",30*app.math_size+5,27*app.math_size)
    app.texts_free("ブーメラン斬り","13_font",30*app.math_size+5,28*app.math_size)  
    
    app.set_stroke_color(0)
    app.set_color(255)
    app.rect_free(11*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(15*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(19*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(24*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(30*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    
    if skip == True: # 分離
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(11*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if 5 <= GS.clock_1 and skip == True and 100 <= app.prayer.energy and GS.kimewaza == True: # オウビーム
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(15*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if 10 <= GS.clock_2 and skip == True: # オウブーメラン
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(19*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if 10 <= GS.clock_3 and skip == True: # エンペラーカッター
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(24*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if 5 <= GS.clock_4 and skip == True: # ブーメラン斬り
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(30*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)

  elif app.prayer.role == "カイザー":
    app.set_color(0)
    app.texts_free("0","13_font",11*app.math_size+5,27*app.math_size)
    app.texts_free("分離","13_font",11*app.math_size+5,28*app.math_size)
    
    app.texts_free("1","13_font",15*app.math_size+5,27*app.math_size)
    app.texts_free("オウドリルミサイル","13_font",15*app.math_size+5,28*app.math_size)
  
    app.texts_free("2","13_font",22*app.math_size+5,27*app.math_size)
    app.texts_free("オウハリケーン","13_font",22*app.math_size+5,28*app.math_size)  
  
    app.texts_free("3","13_font",27*app.math_size+5,27*app.math_size)
    app.texts_free("カイザートルネード","13_font",27*app.math_size+5,28*app.math_size)  
  
    app.texts_free("4","13_font",33*app.math_size+5,27*app.math_size)
    app.texts_free("オーバードライブ","13_font",33*app.math_size+5,28*app.math_size)  
    
    app.set_stroke_color(0)
    app.set_color(255)
    app.rect_free(11*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(15*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(22*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(27*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(33*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)    
    
    if skip == True: # 分離
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(11*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if 10<= GS.clock_1 and skip == True and 30 <= app.prayer.energy and GS.kimewaza == True: # オウドリルミサイル
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(15*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if 10 <= GS.clock_2 and skip == True and 20 <= app.prayer.energy: # オウハリケーン
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(22*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if 10 <= GS.clock_3 and skip == True and 30 <= app.prayer.energy: # カイザートルネード
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(27*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if 5 <= GS.clock_4 and skip == True: # オーバードライブ
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(33*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)    
    
    
  elif app.prayer.role == "ミカド":
    app.set_color(0)
    app.texts_free("0","13_font",11*app.math_size+5,27*app.math_size)
    app.texts_free("分離","13_font",11*app.math_size+5,28*app.math_size)
    
    app.texts_free("1","13_font",15*app.math_size+5,27*app.math_size)
    app.texts_free("超竹おろし","13_font",15*app.math_size+5,28*app.math_size)
  
    app.texts_free("2","13_font",19*app.math_size+5,27*app.math_size)
    app.texts_free("オウミサイル","13_font",19*app.math_size+5,28*app.math_size)  
  
    app.texts_free("3","13_font",23*app.math_size+5,27*app.math_size)
    app.texts_free("タケノコロケット","13_font",23*app.math_size+5,28*app.math_size)  
  
    app.texts_free("4","13_font",27*app.math_size+5,27*app.math_size)
    app.texts_free("ミカドパンチ","13_font",27*app.math_size+5,28*app.math_size)  
    
    app.set_stroke_color(0)
    app.set_color(255)
    app.rect_free(11*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(15*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(19*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(23*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(27*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)    
    
    if skip == True: # 分離
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(11*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if 10 <= GS.clock_1 and skip == True and 60 <= app.prayer.energy and GS.kimewaza == True: # 超竹おろし
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(15*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if 2 <= GS.clock_2 and skip == True and  120 <= app.prayer.energy: # オウミサイル
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(19*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if 2 <= GS.clock_3 and skip == True and 10 <= app.prayer.energy:# タケノコロケット
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(23*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if 2 <= GS.clock_4 and skip == True: # ミカドパンチ
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(27*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)    
  
  elif app.prayer.role == "マシン":
    app.set_color(0)
    app.texts_free("1","13_font",11*app.math_size+5,27*app.math_size)
    app.texts_free("オウエンペラー","13_font",11*app.math_size+5,28*app.math_size)
    
    app.texts_free("2","13_font",15*app.math_size+5,27*app.math_size)
    app.texts_free("オウカイザー","13_font",15*app.math_size+5,28*app.math_size)
  
    app.texts_free("3","13_font",19*app.math_size+5,27*app.math_size)
    app.texts_free("オウミカド","13_font",19*app.math_size+5,28*app.math_size)  

    
    app.set_stroke_color(0)
    app.set_color(255)
    app.rect_free(11*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(15*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    app.rect_free(19*app.math_size,25*app.math_size,2*app.math_size,2*app.math_size)
    
    if skip == True:
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(11*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if skip == True:
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(15*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)
    
    if skip == True:
      app.set_color(0,255,50)
    else:
      app.set_color(169)
    app.rect_free(19*app.math_size+5,25*app.math_size+5,2*app.math_size-10,2*app.math_size-10)   
       
  app.noStroke()     
  if GS.debag == True:
    app.set_color(255)
    app.rect_free(0*app.math_size,0*app.math_size,22*app.math_size,1*app.math_size)
    app.set_color(0)
    app.rect_free(22*app.math_size,0*app.math_size,22*app.math_size,1*app.math_size)  