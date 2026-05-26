import pygame
import time
import __main__


# ウインドウの横幅、ウインドウの縦幅、タイトル
def Stage_preparations(WIDTH, HEIGHT, Title):
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption(Title)
  return screen







# キーボードの入力を受け取る仕組み
def key_inputs(obj):
  KEY_MAP = {
    # 英字 (a-z)
    "a": pygame.K_a, "b": pygame.K_b, "c": pygame.K_c, "d": pygame.K_d,
    "e": pygame.K_e, "f": pygame.K_f, "g": pygame.K_g, "h": pygame.K_h,
    "i": pygame.K_i, "j": pygame.K_j, "k": pygame.K_k, "l": pygame.K_l,
    "m": pygame.K_m, "n": pygame.K_n, "o": pygame.K_o, "p": pygame.K_p,
    "q": pygame.K_q, "r": pygame.K_r, "s": pygame.K_s, "t": pygame.K_t,
    "u": pygame.K_u, "v": pygame.K_v, "w": pygame.K_w, "x": pygame.K_x,
    "y": pygame.K_y, "z": pygame.K_z,
    
    # 英字 (A-Z)
    "A": pygame.K_a, "B": pygame.K_b, "C": pygame.K_c, "D": pygame.K_d,
    "E": pygame.K_e, "F": pygame.K_f, "G": pygame.K_g, "H": pygame.K_h,
    "I": pygame.K_i, "J": pygame.K_j, "K": pygame.K_k, "L": pygame.K_l,
    "M": pygame.K_m, "N": pygame.K_n, "O": pygame.K_o, "P": pygame.K_p,
    "Q": pygame.K_q, "R": pygame.K_r, "S": pygame.K_s, "T": pygame.K_t,
    "U": pygame.K_u, "V": pygame.K_v, "W": pygame.K_w, "X": pygame.K_x,
    "Y": pygame.K_y, "Z": pygame.K_z,

    # 数字 (0-9)
    "0": pygame.K_0, "1": pygame.K_1, "2": pygame.K_2, "3": pygame.K_3,
    "4": pygame.K_4, "5": pygame.K_5, "6": pygame.K_6, "7": pygame.K_7,
    "8": pygame.K_8, "9": pygame.K_9,
  }
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      obj.running = False
    
  keys = pygame.key.get_pressed()
  
  # 小文字のキー入力をとる
  for i in range(97,122+1):
    key_code = KEY_MAP.get(chr(i))
    if keys[key_code] == 1:
      obj.atoz_list[i-97] = 1
  # print(obj.atoz_list)
  
  # 大文字のキー入力をとる
  for i in range(65,90+1):
    key_code = KEY_MAP.get(chr(i))
    if keys[key_code] == 1:
      obj.atoz_list[i-65] = 1
      
  # 1~0のキー入力をとる
  for i in range(48,57+1):
    key_code = KEY_MAP.get(chr(i))
    if keys[key_code] == 1:
      obj.list_0to9[i-48] = 1
  # print(obj.list_0to9)
  
  # 矢印キー入力をとる
  if keys[pygame.K_LEFT] == 1:
    obj.Arrow_keys[0] = 1
  if keys[pygame.K_RIGHT] == 1:
    obj.Arrow_keys[1] = 1
  if keys[pygame.K_UP] == 1:
    obj.Arrow_keys[2] = 1  
  if keys[pygame.K_DOWN] == 1:
    obj.Arrow_keys[3] = 1 
  # print(obj.Arrow_keys)  
  
  # コマンド記憶
  if keys[pygame.K_RETURN] == 1:
    obj.Enter_key = 1
    
  if keys[pygame.K_ESCAPE] == 1:
    obj.Escape = 1
    
  if keys[pygame.K_BACKSPACE] == 1:
    obj.Backspace = 1
    
  if keys[pygame.K_SPACE] == 1:
    obj.Space = 1
    
  if keys[pygame.K_LSHIFT] == 1:
    obj.Shift_left = 1
    
  if keys[pygame.K_RSHIFT] == 1:
    obj.Shift_right = 1
  
  # 現在の座標を取得
  mx, my = pygame.mouse.get_pos()
  obj.Tracking_mouse_pos = [mx, my]
  # print(obj.Tracking_mouse_pos)
  
  # クリックした時の座標を取得
  m_buttons = pygame.mouse.get_pressed()
  if m_buttons[0] == True and obj.click_now_bool == True:
    obj.click_now_bool = False
    mx, my = pygame.mouse.get_pos()
    obj.click_mouse_pos = [mx, my]
    # print(obj.click_mouse_pos)
    mx_mas = mx//obj.math_size
    my_mas = my//obj.math_size
    obj.click_mouse_grid_pos = [mx_mas,my_mas]
    # print(obj.click_mouse_grid_pos)
    
  if  m_buttons[0] == False:
    obj.click_now_bool = True
  
  
  # 画面の描写
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pass
  pygame.display.flip()
      
      
      

# フィルムとコマとコマの区切り目
def sleep_time(obj,parameter,obj_parameter):
  # print(f"休止:{obj.fps_sleep_time}")
  # time.sleep(obj.fps_sleep_time)
  time_rupe = True
  start_time = time.time()
  while time_rupe:
    now = time.time()
    if obj.fps_sleep_time <= now - start_time:
      time_rupe = False
    else:
      time.sleep(0.001)
      key_inputs(obj)


# 実動作
def background_order(obj,parameter,obj_parameter):
  obj_parameter[0].screen.fill(obj_parameter[0].color)
  
  
def set_color_order(obj,parameter,obj_parameter):
  obj.Shapes_bool = True
  R = int(parameter[0])
  G = int(parameter[1])
  B = int(parameter[2])
  obj.color = (R,G,B)
  # print(obj.color)
  
  
def rect_order(obj,parameter,obj_parameter):
  # print(parameter[0])
  # print(parameter[1])
  # print(parameter[2])
  
  width_coordinates = int(parameter[0] * obj.math_size)
  height_coordinates = int(parameter[1] * obj.math_size)
  
  if obj.Shapes_bool == True:
    pygame.draw.rect(obj.screen, obj.color, (width_coordinates, height_coordinates, obj.math_size* parameter[2], obj.math_size * parameter[2]))
  if obj.Border_bool == True:
    pygame.draw.rect(obj.screen, obj.stroke_color, (width_coordinates, height_coordinates, obj.math_size* parameter[2], obj.math_size * parameter[2]),obj.Border_size)
    

def set_stroke_color_order(obj,parameter,obj_parameter):
  R = int(parameter[0])
  G = int(parameter[1])
  B = int(parameter[2])
  obj.Border_bool = True
  obj.stroke_color = (R,G,B)
  # print(obj.color)
  

def noStroke_order(obj,parameter,obj_parameter):
  obj.Border_bool = False
  
def noFill_order(obj,parameter,obj_parameter):
  obj.Shapes_bool = False
  
  
def set_fps_order(obj,parameter,obj_parameter):
  obj.fps = int(parameter[0])
  
def set_tps_order(obj,parameter,obj_parameter):
  obj.tps = parameter[0]
  
  
def rect_free_order(obj,parameter,obj_parameter):  
  if obj.Shapes_bool == True:
    pygame.draw.rect(obj.screen, obj.color, (parameter[0], parameter[1], parameter[2], parameter[3]))
  if obj.Border_bool == True:
    pygame.draw.rect(obj.screen, obj.stroke_color, (parameter[0], parameter[1], parameter[2], parameter[3]),obj.Border_size)
    

def rect_animation_order(obj,parameter,obj_parameter):
  # print(parameter[0])
  # print(parameter[1])
  # print(parameter[2])
  
  width_coordinates = parameter[0]
  height_coordinates =parameter[1]
  if obj.Shapes_bool == True:
    pygame.draw.rect(obj.screen, obj.color, (width_coordinates, height_coordinates, obj.math_size* parameter[2], obj.math_size * parameter[2]))
  if obj.Border_bool == True:
    pygame.draw.rect(obj.screen, obj.stroke_color, (width_coordinates, height_coordinates, obj.math_size* parameter[2], obj.math_size * parameter[2]),obj.Border_size)
    

def key_output_order(obj,parameter,obj_parameter):
  print(f"小文字:{obj.before_atoz_list}")
  # print(f"大文字:{obj.before_AtoZ_list}")
  print(f"数字:{obj.before_list_0to9}")
  print(f"左右上下:{obj.before_Arrow_keys}")
  print(f"エンターキー:{obj.before_Enter_key}")
  print(f"エスケープキー:{obj.before_Escape}")
  print(f"バックスペースキー:{obj.before_Backspace}")
  print(f"スペースキー:{obj.before_Space}")
  print(f"左シフト:{obj.before_Shift_left}")
  print(f"右シフト:{obj.before_Shift_right}")
  print()
  
  
def Font_settings_order(obj,parameter,obj_parameter):
  # print(parameter)
  font_name = parameter[0]
  font_kind = parameter[1]
  font_size = parameter[2]
  
  if font_name in obj.font_box:
    print("同じものが登録されています:フォント")
  else:
    obj.font_box[font_name] = pygame.font.Font(font_kind, font_size)
    
  # print(obj.font_box)
  

def text_box_order(obj,parameter,obj_parameter):
  if parameter[1] in obj.font_box:
    font_obj = obj.font_box[parameter[1]]
    if obj.Shapes_bool == True:
      text_surface = font_obj.render(parameter[0], obj.Anti_aliasing, obj.color)
      obj.screen.blit(text_surface, (parameter[2]*obj.math_size, parameter[3]*obj.math_size))
  else:
    print("登録されていません")
    raise 0
  
def text_box_free_order(obj,parameter,obj_parameter):
  if parameter[1] in obj.font_box:
    font_obj = obj.font_box[parameter[1]]
    if obj.Shapes_bool == True:
      text_surface = font_obj.render(parameter[0], obj.Anti_aliasing, obj.color)
      obj.screen.blit(text_surface, (parameter[2], parameter[3]))
  else:
    print("登録されていません")
    raise 0
  
def text_box_animation_order(obj,parameter,obj_parameter):
  if parameter[1] in obj.font_box:
    font_obj = obj.font_box[parameter[1]]
    if obj.Shapes_bool == True:
      text_surface = font_obj.render(parameter[0], obj.Anti_aliasing, obj.color)
      # print(parameter[2])
      # print(parameter[3])
      obj.screen.blit(text_surface, (parameter[2], parameter[3]))
  else:
    print("登録されていません")
    raise 0
  
  
def set_Border_size_order(obj,parameter,obj_parameter):
  obj.Border_size = int(parameter[0])
  obj.Border_bool = True
  
  
def image_create_order(obj,parameter,obj_parameter):
  image_name = parameter[0]
  image_path = parameter[1]
  image_size = parameter[2] * obj.math_size
  
  if image_name in obj.image_box:
    # メモリ解放
    obj.image_box[image_name] = None
  
  original_img = pygame.image.load(image_path).convert_alpha()
  obj.image_box[image_name] = pygame.transform.scale(original_img, (image_size, image_size))
    
  # print(obj.image_box)


def image_rect_order(obj,parameter,obj_parameter):
  image_obj = obj.image_box[parameter[0]]
  width_coordinates = int(parameter[1] * obj.math_size)
  height_coordinates = int(parameter[2] * obj.math_size)
  
  obj.screen.blit(image_obj, (width_coordinates, height_coordinates))
  
  
def image_cut_create_order(obj,parameter,obj_parameter):
  # image_name,image_path,cut_x_coordinates,cut_y_coordinates,cut_size,image_size = 1
  image_name = parameter[0]
  image_path = parameter[1]
  cut_x_coordinates = parameter[2]
  cut_y_coordinates = parameter[3]
  cut_size = parameter[4]
  image_size = parameter[5] * obj.math_size
  
  if image_name in obj.image_box:
    # メモリ解放
    obj.image_box[image_name] = None
  
  original_img = pygame.image.load(image_path).convert_alpha()
  cropped_img = original_img.subsurface((cut_x_coordinates,cut_y_coordinates,cut_size,cut_size)).copy()
  obj.image_box[image_name] = pygame.transform.scale(cropped_img, (image_size, image_size))
  original_img = None
    
  # print(obj.image_box)
  

def image_rect_animation_order(obj,parameter,obj_parameter):
  image_obj = obj.image_box[parameter[0]]
  width_coordinates = parameter[1]
  height_coordinates = parameter[2]
  
  obj.screen.blit(image_obj, (width_coordinates, height_coordinates))
  

def line_display_order(obj,parameter,obj_parameter):
    if obj.Border_bool == True:
      pygame.draw.line(obj.screen,obj.stroke_color,(parameter[0], parameter[1]),(parameter[2], parameter[3]),obj.Border_size)
      

def BGM_create_order(obj,parameter,obj_parameter):
  BGM_name = parameter[0]
  BGM_path = parameter[1]
  
  if BGM_name in obj.BGM_box:
    print("同じものが登録されています:BGM")
  else:
    sound = pygame.mixer.Sound(BGM_path)
    obj.BGM_box[BGM_name] = sound
    obj.BGM_flag_box[BGM_name] = 0
    obj.BGM_volume_box[BGM_name] = 0.5
    obj.BGM_delete_box[BGM_name] = 0
       
       
def BGM_play_order(obj,parameter,obj_parameter):
  BGM_name = parameter[0]
  if BGM_name in obj.BGM_box:
    if obj.BGM_flag_box[BGM_name] == 0:
      obj.BGM_flag_box[BGM_name] = 1
      obj.BGM_box[BGM_name].set_volume(obj.BGM_volume_box[BGM_name])
      obj.BGM_box[BGM_name].play()
      obj.auto_scenario_script.append(["BGM_flag_reset_Reservation",[BGM_name],[obj]])
      # print(obj.auto_scenario_script)
    else:
      print("再生中")
  else:
    print("未登録のBGMです:play")
    
def SE_play_order(obj,parameter,obj_parameter):
  BGM_name = parameter[0]
  if BGM_name in obj.BGM_box:
      obj.BGM_box[BGM_name].set_volume(obj.BGM_volume_box[BGM_name])
      obj.BGM_box[BGM_name].play()
  else:
    print("未登録のBGMです:play")
    
  # print("play")
    
# def BGM_loop_play_order(obj,parameter,obj_parameter):
#   BGM_name = parameter[0]
#   if obj.BGM_flag_box[BGM_name] == 0:
#     obj.BGM_flag_box[BGM_name] = 0
#     obj.BGM_box[BGM_name].play(-1)
#   else:
#     print("再生中:ループ")

def BGM_volume_order(obj,parameter,obj_parameter):
  BGM_name = parameter[0]
  
  if BGM_name in obj.BGM_box:
    BGM_volume = parameter[1] / 100
  
  
    BGM_volume = max(BGM_volume, 0.0)
    BGM_volume = min(BGM_volume, 1.0)
  
    obj.BGM_volume_box[BGM_name] = BGM_volume
    obj.BGM_box[BGM_name].set_volume(obj.BGM_volume_box[BGM_name])
  else:
    print("未登録のBGMです:volum")
    
    
# BGMがなっているかの確認
def BGM_flag_reset_order(obj, parameter, obj_parameter):
    BGM_name = parameter[0]
  
    if BGM_name not in obj.BGM_box:
        obj.auto_scenario_script = [task for task in obj.auto_scenario_script if not (task[0] == "BGM_flag_reset_Reservation" and task[1][0] == BGM_name)]
        return

    if obj.BGM_box[BGM_name].get_num_channels() == 0:
        obj.BGM_flag_box[BGM_name] = 0
        obj.auto_scenario_script = [task for task in obj.auto_scenario_script if not (task[1][0] == BGM_name)]

    if obj.BGM_delete_box.get(BGM_name) == 1:
        obj.BGM_box.pop(BGM_name, None)
        obj.BGM_flag_box.pop(BGM_name, None)
        obj.BGM_volume_box.pop(BGM_name, None)
        obj.BGM_delete_box.pop(BGM_name, None)
        obj.auto_scenario_script = [task for task in obj.auto_scenario_script if not (task[1][0] == BGM_name)]


 
# BGMの停止
def BGM_stop_order(obj,parameter,obj_parameter):
  # print("stop")
  BGM_name = parameter[0]
  if BGM_name in obj.BGM_box:
    obj.BGM_box[BGM_name].stop()
  else:
    print("未登録のBGMです:stop")
    
    
def BGM_memory_delete_order(obj,parameter,obj_parameter):
  BGM_name = parameter[0]
  if BGM_name in obj.BGM_box:
    obj.BGM_delete_box[BGM_name] = 1
    obj.BGM_box[BGM_name].stop()
    print(f"BGMメモリー削除:{BGM_name}")
  else:
    print("未登録のBGMです:memory")
  

def grid_lines_order(obj,parameter,obj_parameter):
  x1 = parameter[0]
  y1 = parameter[1]
  x2 = parameter[2]
  y2 = parameter[3]
  
  if x2 <= x1:
    print("処理不可:x1がx2のマス目を超えている")
    raise 0
  if y2 <= y1:
    print("処理不可:y1がy2のマス目を超えている")  
    raise 0
  
  width_cells = x2 - x1  
  height_cells = y2 - y1
  for i in range(width_cells + 1):
    x_con_1 = parameter[0]*obj.math_size + i*obj.math_size
    y_con_1 = parameter[1]*obj.math_size
    x_con_2 = parameter[0]*obj.math_size + i*obj.math_size
    y_con_2 = parameter[3]*obj.math_size
    if obj.Border_bool == True:
      pygame.draw.line(obj.screen,obj.stroke_color,(x_con_1, y_con_1),(x_con_2, y_con_2),obj.Border_size)
      
  for i in range(height_cells + 1):
    x_con_1 = parameter[0]*obj.math_size
    y_con_1 = parameter[1]*obj.math_size + i*obj.math_size
    x_con_2 = parameter[2]*obj.math_size 
    y_con_2 = parameter[1]*obj.math_size + i*obj.math_size
    if obj.Border_bool == True:
      pygame.draw.line(obj.screen,obj.stroke_color,(x_con_1, y_con_1),(x_con_2, y_con_2),obj.Border_size)  
      

def map_display_order(obj,parameter,obj_parameter):
  # print(parameter)
  map = parameter[0]
  x_con = parameter[1][0] * obj.math_size
  y_con = parameter[1][1] * obj.math_size

  for y in range(len(map)):
    for x in range(len(map[0])):
      # pygame.draw.rect(obj.screen, (200,0,0), ((x*obj.math_size)+x_con,(y*obj.math_size)+y_con , obj.math_size, obj.math_size))
      # print(map[y][x])
      mas = map[y][x]
      if mas[0] == 1:
        pygame.draw.rect(obj.screen, mas[1][0], ((x*obj.math_size)+x_con,(y*obj.math_size)+y_con , obj.math_size, obj.math_size))
      
      elif mas[0] == 2:
        image_obj = obj.image_box[mas[1][0]]
        width_coordinates = (x*obj.math_size)+x_con
        height_coordinates = (y*obj.math_size)+y_con
        obj.screen.blit(image_obj, (width_coordinates, height_coordinates))
  
        
        
  #     map_display = [
  #   [[0,[]],[1,[(200,0,0)]]], #(0,0),(0,1)
  #   [[2,["テスト"]],[3,["テスト4"]]]
  # ]
  
  
  
  
def map_display_animation_order(obj,parameter,obj_parameter):
  # print(parameter)
  map = parameter[0]
  
  animation_x = parameter[1]
  animation_y = parameter[2]

  for y in range(len(map)):
    for x in range(len(map[0])):
      # pygame.draw.rect(obj.screen, (200,0,0), ((x*obj.math_size)+x_con,(y*obj.math_size)+y_con , obj.math_size, obj.math_size))
      # print(map[y][x])
      mas = map[y][x]
      if mas[0] == 1:
        x_rect = (x*obj.math_size) + animation_x
        y_rect = (y*obj.math_size) + animation_y
        pygame.draw.rect(obj.screen, mas[1][0], (x_rect,y_rect , obj.math_size, obj.math_size))
      
      elif mas[0] == 2:
        image_obj = obj.image_box[mas[1][0]]
        width_coordinates = (x*obj.math_size) + animation_x
        height_coordinates = (y*obj.math_size) + animation_y
        obj.screen.blit(image_obj, (width_coordinates, height_coordinates))
        

def texts_free_order(obj,parameter,obj_parameter):
  # print(parameter)
  if parameter[1] in obj.font_box:
    font_obj = obj.font_box[parameter[1]]
    if obj.Shapes_bool == True:
      text_surface = font_obj.render(parameter[0], obj.Anti_aliasing, obj.color)
      obj.screen.blit(text_surface, (parameter[2], parameter[3]))
  else:
    print("登録されていません")
    raise 0
  
  
def limit_map_display_order(obj,parameter,obj_parameter):
  # print(parameter)
  map = parameter[0]
  x_con = parameter[1] * obj.math_size
  y_con = parameter[2] * obj.math_size
  start_map_x = parameter[3]
  start_map_y = parameter[4]
  final_map_x = parameter[5]
  fainal_map_y = parameter[6]
  
  width_count = final_map_x - start_map_x
  height_count = fainal_map_y - start_map_y
  
  for y in range(height_count):
   for x in range(width_count):
      map_y = start_map_y + y
      map_x = start_map_x + x
      mas = map[map_y][map_x]
      if mas[0] == 1:
        pygame.draw.rect(obj.screen, mas[1][0], ((x*obj.math_size)+x_con,(y*obj.math_size)+y_con , obj.math_size, obj.math_size))
      elif mas[0] == 2:
        image_name = mas[1][0]
        if image_name in obj.image_box:
          image_obj = obj.image_box[image_name]
          width_coordinates = (x * obj.math_size) + x_con
          height_coordinates = (y * obj.math_size) + y_con
          # height_coordinates = (y * obj.math_size) + y_con
          obj.screen.blit(image_obj, (width_coordinates, height_coordinates))
        else:
          print("画像が存在しません")
          


def limit_map_display_animation_order(obj,parameter,obj_parameter):
  # print(parameter)
  # map, coordinate_wight, coordinate_height, start_map_x, start_map_y, final_map_x, final_map_y
  map = parameter[0]
  x_con = parameter[1]
  y_con = parameter[2]
  start_map_x = parameter[3]
  start_map_y = parameter[4]
  final_map_x = parameter[5]
  final_map_y = parameter[6]
  # x_con = 0
  # y_con = 0
  width_count = final_map_x - start_map_x + 1
  height_count = final_map_y - start_map_y +1
  # print(x_con)
  for y in range(height_count):
   for x in range(width_count):
      map_y = start_map_y + y
      map_x = start_map_x + x
      if 0 <= map_y < len(map) and 0 <= map_x < len(map[0]):
        mas = map[map_y][map_x]
      else:
        continue
        
      if mas[0] == 1:
        pygame.draw.rect(obj.screen, mas[1][0], ((x*obj.math_size)+x_con,(y*obj.math_size)+y_con , obj.math_size, obj.math_size))
      elif mas[0] == 2:
        image_name = mas[1][0]
        if image_name in obj.image_box:
          image_obj = obj.image_box[image_name]
          width_coordinates = (x * obj.math_size) + x_con
          height_coordinates = (y * obj.math_size) + y_con
          obj.screen.blit(image_obj, (width_coordinates, height_coordinates))
        else:
          print("画像が存在しません")
          
                          
      
def raw_image_create_order(obj,parameter,obj_parameter):
  image_name = parameter[0]
  image_path = parameter[1]
  image_size_height = parameter[2]
  image_size_wight = parameter[3]
  
  if image_name in obj.image_box:
    # メモリ解放
    obj.image_box[image_name] = None
  
  original_img = pygame.image.load(image_path).convert_alpha()
  obj.image_box[image_name] = pygame.transform.scale(original_img, (image_size_height, image_size_wight))
    
    
  # print(obj.image_box)
  
def rect_animation_fps_setting_free_size_order(obj,parameter,obj_parameter):
  # print(parameter[0])
  # print(parameter[1])
  # print(parameter[2])
  
  width_coordinates = parameter[0]
  height_coordinates =parameter[1]
  
  if obj.Shapes_bool == True:
    pygame.draw.rect(obj.screen, obj.color, (width_coordinates, height_coordinates, obj.math_size* parameter[2], obj.math_size * parameter[3]))
  if obj.Border_bool == True:
    pygame.draw.rect(obj.screen, obj.stroke_color, (width_coordinates, height_coordinates, obj.math_size* parameter[2], obj.math_size * parameter[3]),obj.Border_size)

  
def image_create_rotate_order(obj,parameter,obj_parameter):
  image_name = parameter[0]
  image_path = parameter[1]
  image_size = parameter[3] * obj.math_size
  rotate = parameter[2]
  
  # print(parameter)
  if rotate == 0:# 回転なし
    rotate = 0
  elif rotate == 1:# 左回転
    rotate = 90
  elif rotate == 2:# 右回転
    rotate = 180
  elif rotate == 3:# 上下反転
    rotate = -90    
      
  if image_name in obj.image_box:
    obj.image_box[image_name] = None
    
  original_img = pygame.image.load(image_path).convert_alpha()
  scaled_img = pygame.transform.scale(original_img, (image_size, image_size))
  rotated_img = pygame.transform.rotate(scaled_img, rotate)

  obj.image_box[image_name] = rotated_img
    
  # print(obj.image_box)
  
  
  
# プレイヤーオブジェクト
def Prayer_action_order(obj, parameter, obj_parameter):
    if obj.Dominus == False:
        print("プレイヤーをクランクアップ")
        obj.auto_scenario_script = [
            task for task in obj.auto_scenario_script 
            if task[0] != "Prayer_action_Reservation"
        ]
        obj.prayer = None # プレイヤーオブジェクトを空にする
        return
    else:
      if hasattr( __main__,'Prayer_action_rule'):
        __main__.Prayer_action_rule(obj)
        if obj.prayer.hyper_muteki == False:
          damage_box = obj.prayer.damage_box
          for i in range(len(damage_box)):
            damage = damage_box[i]
            damage = damage - obj.prayer.defence
            if damage <= 0:
              damage = 10
            obj.prayer.HP = obj.prayer.HP - damage
          obj.prayer.damage_box = []
          if obj.prayer.HP <= 0:
            obj.prayer.HP = 0
            obj.prayer.death_flag = True 
        else:
          obj.prayer.damage_box = []
       
       
          
# キャタクター
# キャラクターの実行命令
def Character_action_order(obj, parameter, obj_parameter):
    char_obj = parameter[0]  # Characterクラスのインスタンス
    name = char_obj.name

    if char_obj.Crank_up == True:
        print(f"【演出】{name}がクランクアップ（退場）しました")
        
        obj.auto_scenario_script = [
            task for task in obj.auto_scenario_script 
            if not (task[0] == "Character_action_Reservation" and task[1][1] == name)
        ]
        obj.character.pop(name)

        
    if char_obj.hyper_muteki == False:
      damage_box = char_obj.damage_box
      for i in range(len(damage_box)):
        damage = damage_box[i]
        char_obj.HP = char_obj.HP - damage
      char_obj.damage_box = []
      if char_obj.HP <= 0:
        char_obj.HP = 0
        char_obj.death_flag = True 
    else:
      char_obj.prayer.damage_box = []
      
    if hasattr(__main__, 'Character_action_rule') and char_obj.Crank_up == False:
        __main__.Character_action_rule(obj,name)