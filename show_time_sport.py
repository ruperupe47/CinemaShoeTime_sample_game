from collections import deque

# new_projection_frameに追加する仕組み
def Reservation(obj,name,parameter,list_parameter):
  new_projection_frame = deque()
    
  # for frame in obj.projection_frame:
  for i,frame in  enumerate(obj.projection_frame):
    # もし現在のコマが "sleep_time" だった場合
    if frame[0] == "sleep_time":
      # 背景更新用のコマンドを先に差し込む
      # 形式: [命令名, パラメータ, オブジェクト参照]
      new_projection_frame.append([name,parameter,list_parameter])
        
    # 本来のコマを追加
    new_projection_frame.append(frame)
    
  # 最後に中身を入れ替える
  obj.projection_frame = new_projection_frame
  # print(obj.projection_frame)





# 予約用のコマンド一覧
def background_Reservation(obj,parameter):
  Reservation(obj,"background_order",parameter,[obj])
  
  
def set_color_Reservation(obj,parameter):
  Reservation(obj,"set_color_order",parameter,[obj])
  
  
def rect_Reservation(obj,parameter):
  Reservation(obj,"rect_order",parameter,[obj])
  
  
def set_stroke_color_Reservation(obj,parameter):
  Reservation(obj,"set_stroke_color_order",parameter,[obj])
  
  
def noStroke_Reservation(obj,parameter):
  Reservation(obj,"noStroke_order",parameter,[obj])
  
  
def noFill_Reservation(obj,parameter):
  Reservation(obj,"noFill_order",parameter,[obj])
  
  
def set_fps_Reservation(obj,parameter):
  obj.stage_directions.append(["set_fps_order",parameter,[obj]])
  
def set_tps_Reservation(obj,parameter):
  obj.stage_directions.append(["set_tps_order",parameter,[obj]])

def rect_free_Reservation(obj,parameter):
  Reservation(obj,"rect_free_order",parameter,[obj])
  
def rect_animation_Reservation(obj,parameter):
  new_projection_frame = deque()
  
  wight_grid_coordinates_1 = parameter[0]
  height_grid_coordinates_1 = parameter[1]
  wight_grid_coordinates_2 = parameter[2]
  height_grid_coordinates_2 = parameter[3]
  Square_used = parameter[4]
  
  fps_count = 0 # 現在のfps量を測る
  amount_of_movement_wight = ((wight_grid_coordinates_2 - wight_grid_coordinates_1) * obj.math_size) / obj.fps # 1fps内での移動量(横)
  amount_of_movement_height = ((height_grid_coordinates_2 - height_grid_coordinates_1) * obj.math_size) / obj.fps # 1fps内での移動量(縦)
  
  
  for i,frame in  enumerate(obj.projection_frame):
    if frame[0] == "sleep_time":
      fps_count = fps_count + 1
      coordinate_wight = (wight_grid_coordinates_1 * obj.math_size) + (amount_of_movement_wight *  fps_count)
      # print(coordinate_wight)
      coordinate_height = (height_grid_coordinates_1 * obj.math_size) + (amount_of_movement_height *  fps_count)
      
      parameter_list = [coordinate_wight,coordinate_height,Square_used]
      # print(parameter_list)
      new_projection_frame.append(["rect_animation_order",parameter_list,[obj]])
        
    # 本来のコマを追加
    new_projection_frame.append(frame)
    
  # 最後に中身を入れ替える
  obj.projection_frame = new_projection_frame
  
  
def key_output_Reservation(obj,parameter):
  obj.stage_directions.append(["key_output_order",parameter,[obj]])
  

def Font_settings_Reservation(obj,parameter):
  obj.stage_directions.append(["Font_settings_order",parameter,[obj]]) 

def text_box_Reservation(obj,parameter):
  Reservation(obj,"text_box_order",parameter,[obj])
  
def text_box_free_Reservation(obj,parameter):
  Reservation(obj,"text_box_free_order",parameter,[obj])
  
  
def text_box_animation_Reservation(obj,parameter):
  new_projection_frame = deque()
  # print(parameter)
  output_text = parameter[0]
  font_obj_name = parameter[1]
  x_mas_con_1 = parameter[2]
  y_mas_con_1 = parameter[3]
  x_mas_con_2 = parameter[4]
  y_mas_con_2 = parameter[5]
    
  fps_count = 0 # 現在のfps量を測る
  amount_of_movement_wight = ((x_mas_con_2 - x_mas_con_1) * obj.math_size) / obj.fps # 1fps内での移動量(横)
  amount_of_movement_height = ((y_mas_con_2 - y_mas_con_1) * obj.math_size) / obj.fps # 1fps内での移動量(縦)
  
  
  for i,frame in  enumerate(obj.projection_frame):
    if frame[0] == "sleep_time":
      fps_count = fps_count + 1
      coordinate_wight = (x_mas_con_1 * obj.math_size) + (amount_of_movement_wight *  fps_count)
      # print(coordinate_wight)
      coordinate_height = (y_mas_con_1 * obj.math_size) + (amount_of_movement_height *  fps_count)
      # print(coordinate_wight)
      parameter_list = [output_text,font_obj_name,coordinate_wight,coordinate_height]
      new_projection_frame.append(["text_box_animation_order",parameter_list,[obj]])
    # 本来のコマを追加
    new_projection_frame.append(frame)
    
  # 最後に中身を入れ替える
  obj.projection_frame = new_projection_frame
  
  
  
def set_Border_size_Reservation(obj,parameter):
  Reservation(obj,"set_Border_size_order",parameter,[obj])
  
def image_create_Reservation(obj,parameter):
  obj.stage_directions.append(["image_create_order",parameter,[obj]]) 
  
def image_rect_Reservation(obj,parameter):
  Reservation(obj,"image_rect_order",parameter,[obj])
  
def image_cut_create_Reservation(obj,parameter):
  obj.stage_directions.append(["image_cut_create_order",parameter,[obj]]) 
  
  
def image_rect_animation_Reservation(obj,parameter):
  new_projection_frame = deque()
  # print(parameter)
  # image_name,x_mas_con_1,y_mas_con_1,x_mas_con_2,y_mas_con_2,math_size = 1
  image_name = parameter[0]
  x_mas_con_1 = parameter[1]
  y_mas_con_1 = parameter[2]
  x_mas_con_2 = parameter[3]
  y_mas_con_2 = parameter[4]
    
  fps_count = 0 # 現在のfps量を測る
  amount_of_movement_wight = ((x_mas_con_2 - x_mas_con_1) * obj.math_size) / obj.fps # 1fps内での移動量(横)
  amount_of_movement_height = ((y_mas_con_2 - y_mas_con_1) * obj.math_size) / obj.fps # 1fps内での移動量(縦)
  
  
  for i,frame in  enumerate(obj.projection_frame):
    if frame[0] == "sleep_time":
      fps_count = fps_count + 1
      coordinate_wight = (x_mas_con_1 * obj.math_size) + (amount_of_movement_wight *  fps_count)
      # print(coordinate_wight)
      coordinate_height = (y_mas_con_1 * obj.math_size) + (amount_of_movement_height *  fps_count)
      # print(coordinate_wight)
      parameter_list = [image_name,coordinate_wight,coordinate_height]
      new_projection_frame.append(["image_rect_animation_order",parameter_list,[obj]])
    # 本来のコマを追加
    new_projection_frame.append(frame)
    
  # 最後に中身を入れ替える
  obj.projection_frame = new_projection_frame


def line_display_Reservation(obj,parameter):
  Reservation(obj,"line_display_order",parameter,[obj])
  

def BGM_create_Reservation(obj,parameter):
  obj.stage_directions.append(["BGM_create_order",parameter,[obj]]) 
  
def BGM_play_Reservation(obj,parameter):
  obj.stage_directions.append(["BGM_play_order",parameter,[obj]]) 
  
def SE_play_Reservation(obj,parameter):
  obj.stage_directions.append(["SE_play_order",parameter,[obj]]) 

# def BGM_loop_play_Reservation(obj,parameter):
#   obj.stage_directions.append(["BGM_loop_play_order",parameter,[obj]]) 
  
def BGM_volume_Reservation(obj,parameter):
  obj.stage_directions.append(["BGM_volume_order",parameter,[obj]]) 
  
def BGM_flag_reset_Reservation(obj,parameter):
  for i,frame in  enumerate(obj.projection_frame):
    if frame[0] == "sleep_time":
      # 形式: [命令名, パラメータ, オブジェクト参照]
      obj.projection_frame.insert(i-1,["BGM_flag_reset_order",parameter,[obj]])
      return 0

def BGM_stop_Reservation(obj,parameter):
  obj.stage_directions.append(["BGM_stop_order",parameter,[obj]]) 
  
def BGM_memory_delete_Reservation(obj,parameter):
  obj.stage_directions.append(["BGM_play_order",parameter,[obj]]) 
  obj.stage_directions.append(["BGM_memory_delete_order",parameter,[obj]]) 
  
  
def grid_lines_Reservation(obj,parameter):
  Reservation(obj,"grid_lines_order",parameter,[obj])
  
  
def map_display_Reservation(obj,parameter):
  Reservation(obj,"map_display_order",parameter,[obj])
  
  
def map_display_animation_Reservation(obj,parameter):
  new_projection_frame = deque()
  
  map = parameter[0]
  wight_grid_coordinates_1 = parameter[1]
  height_grid_coordinates_1 = parameter[2]
  wight_grid_coordinates_2 = parameter[3]
  height_grid_coordinates_2 = parameter[4]
  
  fps_count = 0 # 現在のfps量を測る
  amount_of_movement_wight = ((wight_grid_coordinates_2 - wight_grid_coordinates_1) * obj.math_size) / obj.fps # 1fps内での移動量(横)
  amount_of_movement_height = ((height_grid_coordinates_2 - height_grid_coordinates_1) * obj.math_size) / obj.fps # 1fps内での移動量(縦)
  
  
  for i,frame in  enumerate(obj.projection_frame):
    if frame[0] == "sleep_time":
      fps_count = fps_count + 1
      coordinate_wight = (wight_grid_coordinates_1 * obj.math_size) + (amount_of_movement_wight *  fps_count)
      coordinate_height = (height_grid_coordinates_1 * obj.math_size) + (amount_of_movement_height *  fps_count)
      
      parameter_list = [map,coordinate_wight,coordinate_height]
      new_projection_frame.append(["map_display_animation_order",parameter_list,[obj]])
        
    # 本来のコマを追加
    new_projection_frame.append(frame)
    
  # 最後に中身を入れ替える
  obj.projection_frame = new_projection_frame


def texts_free_Reservation(obj,parameter):
  Reservation(obj,"texts_free_order",parameter,[obj])
  
def limit_map_display_Reservation(obj,parameter):
  Reservation(obj,"limit_map_display_order",parameter,[obj])
  
  
def raw_image_create_Reservation(obj,parameter):
  obj.stage_directions.append(["raw_image_create_order",parameter,[obj]]) 
  

def limit_map_display_animation_Reservation(obj,parameter):
  new_projection_frame = deque()
  # print(parameter)
  map = parameter[0]
  con_x = parameter[1]* obj.math_size
  con_y = parameter[2]* obj.math_size
  start_map_x = parameter[3]
  start_map_y= parameter[4]
  final_map_x = parameter[5]
  final_map_y = parameter[6]
  move_x = parameter[7]
  move_y= parameter[8]  
    
  
    
  fps_count = obj.fps # 現在のfps量を測る
  amount_of_movement_wight = (move_x * obj.math_size) / obj.fps # 1fps内での移動量(横)
  amount_of_movement_height = (move_y * obj.math_size) / obj.fps # 1fps内での移動量(縦)
  
  for i,frame in  enumerate(obj.projection_frame):
    if frame[0] == "sleep_time":
      fps_count = fps_count - 1
      coordinate_wight = con_x - (amount_of_movement_wight * fps_count)
      coordinate_height = con_y - (amount_of_movement_height * fps_count)
      
      # map,coordinate_wightt,coordinate_height,start_map_xf_map_x,start_map_y+f_map_y,final_map_xf_map_x,fainal_map_y+f_map_y 
      parameter_list = [map, coordinate_wight, coordinate_height, start_map_x, start_map_y, final_map_x, final_map_y]
      new_projection_frame.append(["limit_map_display_animation_order",parameter_list,[obj]])
    new_projection_frame.append(frame)
  obj.projection_frame = new_projection_frame
    
    
def Prayer_action_Reservation(obj,parameter):
  obj.stage_directions.append(["Prayer_action_order",parameter,[obj]]) 
  

def Character_action_Reservation(obj,parameter):
  obj.stage_directions.append(["Character_action_order",parameter,[obj]]) 
  





def rect_animation_fps_setting_Reservation(obj, parameter):
    new_projection_frame = deque()
    
    x1, y1, x2, y2 = parameter[0], parameter[1], parameter[2], parameter[3]
    start_fps, final_fps, Square_used = parameter[4], parameter[5], parameter[6]
    
    duration = final_fps - start_fps
    if duration <= 0: 
      duration = 1 

    amount_w = ((x2 - x1) * obj.math_size) / duration
    amount_h = ((y2 - y1) * obj.math_size) / duration
    
    move_count = 0 
    sllep_count = 0
    for i, frame in enumerate(obj.projection_frame):
        sllep_count = 0
        if sllep_count < start_fps:
            if frame[0] == "sleep_time":
                now_x, now_y = x1 * obj.math_size, y1 * obj.math_size
                new_projection_frame.append(["rect_animation_order", [now_x, now_y, Square_used], [obj]])
        elif start_fps <= sllep_count < final_fps:
            if frame[0] == "sleep_time":
                move_count += 1
                now_x = (x1 * obj.math_size) + (amount_w * move_count)
                now_y = (y1 * obj.math_size) + (amount_h * move_count)
                new_projection_frame.append(["rect_animation_order", [now_x, now_y, Square_used], [obj]])
        else:
            if frame[0] == "sleep_time":
                now_x, now_y = x2 * obj.math_size, y2 * obj.math_size
                new_projection_frame.append(["rect_animation_order", [now_x, now_y, Square_used], [obj]])
        new_projection_frame.append(frame)
    obj.projection_frame = new_projection_frame
    
    
# def rect_animation_fps_setting_free_size_Reservation(obj, parameter):
#     new_projection_frame = deque()
    
#     x1, y1, x2, y2 = parameter[0], parameter[1], parameter[2], parameter[3]
#     start_fps, final_fps= parameter[4], parameter[5]
#     math_size_w,math_size_h = parameter[6], parameter[7]
    
#     duration = final_fps - start_fps
#     if duration <= 0: 
#       duration = 1 

#     amount_w = ((x2 - x1) * obj.math_size) / duration
#     amount_h = ((y2 - y1) * obj.math_size) / duration
    
#     move_count = 0 
#     sllep_count = 0
#     for i, frame in enumerate(obj.projection_frame):
#         if sllep_count < start_fps:
#             if frame[0] == "sleep_time":
#                 sllep_count += 1
#                 now_x, now_y = x1 * obj.math_size, y1 * obj.math_size
#                 new_projection_frame.append(["rect_animation_fps_setting_free_size_order", [now_x, now_y, math_size_w,math_size_h], [obj]])
#         elif start_fps <= sllep_count < final_fps:
#             if frame[0] == "sleep_time":
#                 sllep_count += 1
#                 move_count += 1
#                 now_x = (x1 * obj.math_size) + (amount_w * move_count)
#                 now_y = (y1 * obj.math_size) + (amount_h * move_count)
#                 new_projection_frame.append(["rect_animation_fps_setting_free_size_order", [now_x, now_y, math_size_w,math_size_h], [obj]])
#         else:
#             if frame[0] == "sleep_time":
#                 sllep_count += 1
#                 now_x, now_y = x2 * obj.math_size, y2 * obj.math_size
#                 new_projection_frame.append(["rect_animation_fps_setting_free_size_order", [now_x, now_y, math_size_w,math_size_h], [obj]])
#         new_projection_frame.append(frame)
#     obj.projection_frame = new_projection_frame    
    
    
from collections import deque

def rect_animation_fps_setting_free_size_Reservation(obj, parameter):

    new_projection_frame = deque()

    x1, y1, x2, y2 = parameter[0], parameter[1], parameter[2], parameter[3]
    start_fps, final_fps = parameter[4], parameter[5]
    math_size_w, math_size_h = parameter[6], parameter[7]

    duration = final_fps - start_fps

    if duration <= 0:
        duration = 1

    amount_w = ((x2 - x1) * obj.math_size) / duration
    amount_h = ((y2 - y1) * obj.math_size) / duration

    move_count = 0
    sleep_count = 0
    for frame in obj.projection_frame:
        if frame[0] == "sleep_time":
            # 開始前
            if sleep_count < start_fps:
                now_x = x1 * obj.math_size
                now_y = y1 * obj.math_size
            # 移動中
            elif start_fps <= sleep_count < final_fps:
                progress = move_count / duration
                now_x = (x1 * obj.math_size) + ((x2 - x1) * obj.math_size * progress)
                now_y = (y1 * obj.math_size) + ((y2 - y1) * obj.math_size * progress)
                move_count += 1
            # 終了後
            else:
                now_x = x2 * obj.math_size
                now_y = y2 * obj.math_size
                
            new_projection_frame.append([
                "rect_animation_fps_setting_free_size_order",
                [now_x, now_y, math_size_w, math_size_h],
                [obj]
            ])
            sleep_count += 1
        new_projection_frame.append(frame)
    obj.projection_frame = new_projection_frame
    
    
        
def limit_map_display_animation_fps_setting_Reservation(obj, parameter):
    new_projection_frame = deque()
    
    maze_data, base_x_raw, base_y_raw = parameter[0], parameter[1], parameter[2]
    s_map_x, s_map_y, f_map_x, f_map_y = parameter[3], parameter[4], parameter[5], parameter[6]
    move_x, move_y = parameter[7], parameter[8]
    start_fps, final_fps, bools = parameter[9], parameter[10], parameter[11]

    base_x = base_x_raw * obj.math_size
    base_y = base_y_raw * obj.math_size

    duration = final_fps - start_fps
    if duration <= 0: 
      duration = 1

    step_x = (move_x * obj.math_size) / duration
    step_y = (move_y * obj.math_size) / duration

    # move_count = obj.fps
    move_count  = 0
    sllep_count = 0
    for i, frame in enumerate(obj.projection_frame):
        if frame[0] == "sleep_time":
            sllep_count += 1
            draw_x, draw_y = None, None

            if sllep_count  < start_fps:
                if bools:
                    draw_x, draw_y = base_x, base_y

            elif start_fps <= sllep_count  < final_fps:
                # move_count -= 1
                move_count += 1
                draw_x = base_x + (step_x * move_count)
                draw_y = base_y + (step_y * move_count)
                # print(f"step_x:{step_x},{move_count}:move_count,{step_x * move_count}")
            else:
                if bools:
                    draw_x = base_x + (move_x * obj.math_size)
                    draw_y = base_y + (move_y * obj.math_size)
                    # draw_x = base_x
                    # draw_y = base_y
                    
            if draw_x is not None:
                p_list = [maze_data, draw_x, draw_y, s_map_x, s_map_y, f_map_x, f_map_y]
                new_projection_frame.append(["limit_map_display_animation_order", p_list, [obj]])

        new_projection_frame.append(frame)

    obj.projection_frame = new_projection_frame
    
    
def image_create_rotate_Reservation(obj,parameter):
  obj.stage_directions.append(["image_create_rotate_order",parameter,[obj]]) 
  
  
  

def image_rect_animation_fps_setting_free_size_Reservation(obj, parameter):
    new_projection_frame = deque()

    image_name = parameter[0]
    x1, y1, x2, y2 = parameter[1], parameter[2], parameter[3], parameter[4]
    start_fps, final_fps = parameter[5], parameter[6]

    duration = final_fps - start_fps

    if duration <= 0:
        duration = 1

    amount_w = ((x2 - x1) * obj.math_size) / duration
    amount_h = ((y2 - y1) * obj.math_size) / duration

    move_count = 0
    sleep_count = 0
    for frame in obj.projection_frame:
        if frame[0] == "sleep_time":
            # 開始前
            if sleep_count < start_fps:
                now_x = x1 * obj.math_size
                now_y = y1 * obj.math_size
            # 移動中
            elif start_fps <= sleep_count < final_fps:
                progress = move_count / duration
                now_x = (x1 * obj.math_size) + ((x2 - x1) * obj.math_size * progress)
                now_y = (y1 * obj.math_size) + ((y2 - y1) * obj.math_size * progress)
                move_count += 1
            # 終了後
            else:
                now_x = x2 * obj.math_size
                now_y = y2 * obj.math_size
                
            new_projection_frame.append([
                "image_rect_animation_order",
                [image_name,now_x,now_y],
                [obj]
            ])
            sleep_count += 1
        new_projection_frame.append(frame)
    obj.projection_frame = new_projection_frame
    
    

  