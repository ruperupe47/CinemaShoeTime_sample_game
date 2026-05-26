import __main__
from collections import deque
from py_system_syow import *
import show_time_sport as show_time_sport
import os

class Cinema_ShowTime: 
  def __init__(self,wight_mathpiece = 30,height_mathpiece = 20,math_size = 30,Window_title = ""):
    
    # 初期化
    self.wight_mathpiece = wight_mathpiece # 横のマス数
    self.height_mathpiece = height_mathpiece # 縦のマス数
    self.math_size = math_size # マスのサイズ
  
    self.Weight_windowSize = self.wight_mathpiece * self.math_size # ウインドサイズ(横)
    self.Height_windowSize = self.height_mathpiece * self.math_size # ウインドサイズ(縦)
    
    self.Window_title = Window_title # ウインドウタイトル
    
    self.tps = 1 # 処理にかける秒数
    self.fps = 24 # 1tps内に何回処理するか
    
    self.scenario_script = deque() # settingとad_lib内の命令を保存する
    self.auto_scenario_script = [] # 自動化したい処理を記録し続ける
    self.stage_directions = deque()# 音を鳴らすというような命令を記録する
    self.projection_frame = deque()# フィルムの1コマを記録する
      
    # 現在の入力
    self.atoz_list = [0 for i in range(26)] # a〜zの順番
    # self.AtoZ_list = [0 for i in range(26)] # A〜Zの順番
    self.list_0to9 = [0 for i in range(10)] # 0〜9の順番
    self.Arrow_keys = [0 for i in range(4)] # 左、右、上、下の順番
    self.Enter_key = 0 # エンターキー
    self.Escape = 0 # エスケープキー
    self.Backspace = 0 # バックスペースキー
    self.Space = 0 # スペースキー
    self.Shift_left = 0 # Shift (左)
    self.Shift_right = 0 # Shift (右)
       
    # 前の入力tps内で入力されたもの(次のtpsで使用予定)
    self.before_atoz_list = self.atoz_list.copy()
    # self.before_AtoZ_list = self.AtoZ_list.copy()
    self.before_list_0to9 = self.list_0to9.copy()
    self.before_Arrow_keys = self.Arrow_keys.copy()
    self.before_Enter_key = self.Enter_key
    self.before_Escape = self.Escape
    self.before_Backspace = self.Backspace
    self.before_Space = self.Space
    self.before_Shift_left = self.Shift_left
    self.before_Shift_right = self.Shift_right
       
    # マウスのクリック座標
    self.Tracking_mouse_pos = [0, 0] # 現在の座標を追尾
    self.click_mouse_pos = [0, 0] # [x, y] ピクセル単位
    self.click_mouse_grid_pos = [0, 0]   # [x, y] マス単位 (math_sizeで割ったもの)
    self.click_now_bool = True # クリックした瞬間を記録
    
    # 図形用の初期化
    self.Shapes_bool = True # 枠線を描写するかのbool
    self.color = (255,255,255) # 図形内の色用RGB
    self.Border_bool = True # 枠線を描写するかのbool
    self.Border_size = 1 # 枠線のサイズ
    self.stroke_color = (255,255,255) # 枠専用のRGB
    
    # フォント初期化
    self.font_box = {} # フォントのオブジェクトを保存するための辞書
    self.Anti_aliasing = False # フォントのギザギザがある状態
    
    # BGM初期化
    self.BGM_box = {} # BGMのオブジェクトを保存するための辞書
    self.BGM_flag_box = {} # BGMのフラッグのオブジェクトを保存するための辞書(0:流れていない,1:流れてる)
    self.BGM_volume_box = {} # BGMの音量のオブジェクトを保存するための辞書
    self.BGM_delete_box = {} # BGMの削除フラグのオブジェクトを保存するための辞書
    
    # 画像用
    self.image_box = {} # 画像オブジェクトの記録
    
    
    # プレイヤーオブジェクト
    self.prayer = None
    self.Dominus = False
    
 
    # キャラクター
    self.character = {}   
    
    
    
    
    
    # メイン実行
    # ウインドウの作成
    self.screen = Stage_preparations(self.Weight_windowSize,self.Height_windowSize, self.Window_title)
    
    
    # キュー用のリストの初期化を行う
    self.film_create()
    
    # setting関数の実行を行う
    if hasattr( __main__,'setting'):
      __main__.setting(self)
    
    # 命令スタックの解釈
    self.Opportunity_for_interpretation()
    self.auto_Opportunity_for_interpretation()
    # # キー情報の初期化
    # self.key_init()
    # キューの処理
    self.Stageing()
    self.Opportunity_for_interpretation()
    self.Stageing()
    self.Screening()
     
    # キー情報の初期化
    self.key_init()
    # # 画面の描写
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pass
    # pygame.display.flip()
      
    # メイン関数内にad_libがあるかを調査する
    if hasattr( __main__,'ad_lib'):
      self.running = True
    else:
      self.running = False
      
      
    while self.running:
      # キュー用のリストの初期化を行う
      self.film_create()
      
      # ad_lib関数の実行を行う
      __main__.ad_lib(self)
      
      # キューの処理
      self.Opportunity_for_interpretation()
      self.auto_Opportunity_for_interpretation()
      # # キー情報の初期化
      # self.key_init()
      # キューの処理
      self.Stageing()
      self.Opportunity_for_interpretation()
      self.Stageing()
      self.Screening()
            
      # # 画面の描写
      # pygame.display.flip()
      
      # キー情報の初期化
      self.key_init()
      
    
  # キューの作成を行う
  def film_create(self):
    # settingとad_libの保存用の初期化を行う
    self.scenario_script = deque()
      
    # stage_directionsの初期化
    self.stage_directions = deque()
    
    self.projection_frame = deque()
      
    # 待機時間の計算
    self.fps_sleep_time = self.tps / self.fps
      
    # フィルムにコマの切れ目を入れる
    for i in range(self.fps):
      self.projection_frame.append(["sleep_time",[],[self]])
    # print( self.projection_frame)
      


  # scenario_scriptを解釈
  def Opportunity_for_interpretation(self):
    # 解釈のために呼び出す辞書
    self.Opportunity_COMMAND_MAP = {
      "background_Reservation": show_time_sport.background_Reservation,
      "set_color_Reservation": show_time_sport.set_color_Reservation,
      "rect_Reservation": show_time_sport.rect_Reservation,
      "set_stroke_color_Reservation": show_time_sport.set_stroke_color_Reservation,
      "noStroke_Reservation": show_time_sport.noStroke_Reservation,
      "noFill_Reservation": show_time_sport.noFill_Reservation,
      "set_fps_Reservation": show_time_sport.set_fps_Reservation,
      "set_tps_Reservation": show_time_sport.set_tps_Reservation,
      "rect_free_Reservation": show_time_sport.rect_free_Reservation,
      "rect_animation_Reservation": show_time_sport.rect_animation_Reservation,
      "key_output_Reservation": show_time_sport.key_output_Reservation,
      "Font_settings_Reservation": show_time_sport.Font_settings_Reservation,
      "text_box_Reservation": show_time_sport.text_box_Reservation,
      "text_box_free_Reservation": show_time_sport.text_box_free_Reservation,
      "text_box_animation_Reservation": show_time_sport.text_box_animation_Reservation,
      "set_Border_size_Reservation": show_time_sport.set_Border_size_Reservation,
      "image_create_Reservation": show_time_sport.image_create_Reservation,
      "image_rect_Reservation": show_time_sport.image_rect_Reservation,
      "image_cut_create_Reservation": show_time_sport.image_cut_create_Reservation,
      "image_rect_animation_Reservation": show_time_sport.image_rect_animation_Reservation,
      "line_display_Reservation": show_time_sport.line_display_Reservation,
      "BGM_create_Reservation": show_time_sport.BGM_create_Reservation,
      "BGM_play_Reservation": show_time_sport.BGM_play_Reservation,
      # "BGM_loop_play_Reservation": show_time_sport.BGM_loop_play_Reservation,
      "BGM_volume_Reservation": show_time_sport.BGM_volume_Reservation,
      "BGM_stop_Reservation": show_time_sport.BGM_stop_Reservation,
      "BGM_memory_delete_Reservation": show_time_sport.BGM_memory_delete_Reservation,
      "grid_lines_Reservation": show_time_sport.grid_lines_Reservation,
      "map_display_Reservation": show_time_sport.map_display_Reservation,
      "map_display_animation_Reservation": show_time_sport.map_display_animation_Reservation,
      "texts_free_Reservation": show_time_sport.texts_free_Reservation,
      "limit_map_display_Reservation": show_time_sport.limit_map_display_Reservation,
      "raw_image_create_Reservation": show_time_sport.raw_image_create_Reservation,
      "limit_map_display_animation_Reservation": show_time_sport.limit_map_display_animation_Reservation,
      "SE_play_Reservation": show_time_sport.SE_play_Reservation,
      "rect_animation_fps_setting_Reservation": show_time_sport.rect_animation_fps_setting_Reservation,
      "rect_animation_fps_setting_free_size_Reservation": show_time_sport.rect_animation_fps_setting_free_size_Reservation,
      "limit_map_display_animation_fps_setting_Reservation": show_time_sport.limit_map_display_animation_fps_setting_Reservation,
      "image_create_rotate_Reservation": show_time_sport.image_create_rotate_Reservation,
      "image_rect_animation_fps_setting_free_size_Reservation": show_time_sport.image_rect_animation_fps_setting_free_size_Reservation
    }
    
    scenario_script = self.scenario_script # 仮代入
    # キューが空になるまで処理
    while self.scenario_script:
      first_task = scenario_script.popleft()
      command_name = first_task[0]
      if command_name in self.Opportunity_COMMAND_MAP:
        # print(command_name)
        self.Opportunity_COMMAND_MAP[command_name](self,first_task[1])
    # print(self.projection_frame)


  # auto_scenario_scriptに登録されとものを処理する
  def auto_Opportunity_for_interpretation(self):
  # 解釈のために呼び出す辞書
    self.auto_Stageing_COMMAND_MAP = {
      "BGM_flag_reset_Reservation": show_time_sport.BGM_flag_reset_Reservation,
      "Prayer_action_Reservation": show_time_sport.Prayer_action_Reservation,
      "Character_action_Reservation": show_time_sport.Character_action_Reservation
    } 
    # print(self.auto_scenario_script)
    auto_scenario_script = self.auto_scenario_script
    for i in range(len(auto_scenario_script)):
      first_task = auto_scenario_script[i]
      command_name = first_task[0]
      # print("ここ")
      # print(first_task[1][0])
      paraeter = [first_task[1][0],i]
      if command_name in self.auto_Stageing_COMMAND_MAP:
        self.auto_Stageing_COMMAND_MAP[command_name](self,paraeter) 
        
        
  # stage_directionsの解釈を行う
  def Stageing(self):
  # 解釈のために呼び出す辞書
    self.Stageing_COMMAND_MAP = {
      "set_fps_order": set_fps_order,
      "set_tps_order": set_tps_order,
      "key_output_order": key_output_order,
      "Font_settings_order": Font_settings_order,
      "image_create_order": image_create_order,
      "image_cut_create_order": image_cut_create_order,
      "BGM_create_order": BGM_create_order,
      "BGM_play_order": BGM_play_order,
      # "BGM_loop_play_order": BGM_loop_play_order,
      "BGM_volume_order": BGM_volume_order,
      "BGM_stop_order": BGM_stop_order,
      "BGM_memory_delete_order": BGM_memory_delete_order,
      "raw_image_create_order": raw_image_create_order,
      "Prayer_action_order": Prayer_action_order,
      "Character_action_order" : Character_action_order,
      "SE_play_order": SE_play_order,
      "image_create_rotate_order": image_create_rotate_order
    } 
    # print(self.stage_directions)
    stage_directions = self.stage_directions
    while self.stage_directions:
      first_task = stage_directions.popleft()
      command_name = first_task[0]
      if command_name in self.Stageing_COMMAND_MAP:
        self.Stageing_COMMAND_MAP[command_name](self,first_task[1],first_task[2]) 
        
        
  # projection_frameの解釈を行う
  def Screening(self):
    # 解釈のために呼び出す辞書
    self.Screenin_COMMAND_MAP = {
      "sleep_time": sleep_time,
      "background_order": background_order,
      "set_color_order": set_color_order,
      "rect_order": rect_order,
      "set_stroke_color_order": set_stroke_color_order,
      "noStroke_order": noStroke_order,
      "noFill_order": noFill_order,
      "rect_free_order": rect_free_order,
      "rect_animation_order": rect_animation_order,
      "text_box_order": text_box_order,
      "text_box_free_order": text_box_free_order,
      "text_box_animation_order": text_box_animation_order,
      "set_Border_size_order": set_Border_size_order,
      "image_rect_order": image_rect_order,
      "image_rect_animation_order": image_rect_animation_order,
      "line_display_order": line_display_order,
      "BGM_flag_reset_order": BGM_flag_reset_order,
      "grid_lines_order": grid_lines_order,
      "map_display_order": map_display_order,
      "map_display_animation_order": map_display_animation_order,
      "texts_free_order": texts_free_order,
      "limit_map_display_order": limit_map_display_order,
      "limit_map_display_animation_order": limit_map_display_animation_order,
      "rect_animation_fps_setting_free_size_order": rect_animation_fps_setting_free_size_order
    }
    
    # print(self.projection_frame)
    # print()
    projection_frame = self.projection_frame # 仮代入
    # キューが空になるまで処理
    while self.projection_frame:
      first_task = projection_frame.popleft()
      command_name = first_task[0]
      if command_name in self.Screenin_COMMAND_MAP:
        self.Screenin_COMMAND_MAP[command_name](self,first_task[1],first_task[2])    

        


  # キー情報を初期化する
  def key_init(self):
    # 前の入力
    self.before_atoz_list = self.atoz_list.copy()
    # self.before_AtoZ_list = self.AtoZ_list.copy()
    self.before_list_0to9 = self.list_0to9.copy()
    self.before_Arrow_keys = self.Arrow_keys.copy()
    self.before_Enter_key = self.Enter_key
    self.before_Escape = self.Escape
    self.before_Backspace = self.Backspace
    self.before_Space = self.Space
    self.before_Shift_left = self.Shift_left
    self.before_Shift_right = self.Shift_right
    
    # 現在の入力
    self.atoz_list = [0 for i in range(26)] # a〜zの順番
    # self.AtoZ_list = [0 for i in range(26)] # A〜Zの順番
    self.list_0to9 = [0 for i in range(10)] # 0〜9の順番
    self.Arrow_keys = [0 for i in range(4)] # 左、右、上、下の順番
    self.Enter_key = 0 # エンターキー
    self.Escape = 0 # エスケープキー
    self.Backspace = 0 # バックスペースキー
    self.Space = 0 # スペースキー
    self.Shift_left = 0 # Shift (左)
    self.Shift_right = 0 # Shift (右)
    
    
    
  # 命令スタック追加用
  #背景を塗りつぶす
  def background(self):      
    self.scenario_script.append(["background_Reservation",[]])
  
  # 図形の色を設定する。
  def set_color(self,R,G = None,B = None,a = None):
    if a == None:
      a = 1
    if G == None and B == None:
      G,B = R,R
    elif B == None:
      G,B,a = R,R,B

    self.scenario_script.append(["set_color_Reservation",[R,G,B,a]])  
    
  # 図形を描く
  def rect(self,wight_grid_coordinates,height_grid_coordinates,math_size=None):
    if math_size == None:
      math_size = 1
    elif math_size <= 0:
      print("マスの大きさが0以下です")
      raise 0 

    self.scenario_script.append(["rect_Reservation",[wight_grid_coordinates,height_grid_coordinates,math_size]])  
  
  
  # 枠線の色を設定する
  def set_stroke_color(self,R,G = None,B = None):
    if G == None and B == None:
      G,B = R,R

    self.scenario_script.append(["set_stroke_color_Reservation",[R,G,B]])  
    
  # 枠線を表示させない
  def noStroke(self):
    self.scenario_script.append(["noStroke_Reservation",[]])
    
  # 図形を表示させない。枠線のみ。
  def noFill(self):
    self.scenario_script.append(["noFill_Reservation",[]])
    
  # fosの値を設定する
  def set_fps(self,fps_num):
    self.scenario_script.append(["set_fps_Reservation",[fps_num]])
    
  # fosの値を設定する
  def set_tps(self,tps_num):
    self.scenario_script.append(["set_tps_Reservation",[tps_num]])


  # 図形を自由な座標、サイズで描くことができる
  def rect_free(self,wight_coordinates,height_coordinates,wigh_size,height_size = None):
    if height_size == None:
      height_size = wigh_size
      
    self.scenario_script.append(["rect_free_Reservation",[wight_coordinates,height_coordinates,wigh_size,height_size]])  
    
    
  # 図形を描く(アニメーション)
  def rect_animation(self,wight_grid_coordinates_1,height_grid_coordinates_1,wight_grid_coordinates_2,height_grid_coordinates_2,math_size=None):
    if math_size == None:
      math_size = 1
    elif math_size <= 0:
      print("マスの大きさが0以下です")
      raise 0 

    self.scenario_script.append(["rect_animation_Reservation",[wight_grid_coordinates_1,height_grid_coordinates_1,wight_grid_coordinates_2,height_grid_coordinates_2,math_size]])   
  
  
  # 入力されたキーを出力するためのデバック関数
  def key_output(self):
    self.scenario_script.append(["key_output_Reservation",[]])  


  # フォントの設定
  def Font_settings(self,font_name = None,font_kind = None,font_size = None):
    
    if font_name ==  None:
      font_name = "default_font"
    if font_kind ==  None:
      base_dir = os.path.dirname(os.path.abspath(__main__.__file__))
      font_path = os.path.join(base_dir, "フォント", "NotoSerifJP-VariableFont_wght.ttf")
      font_kind = font_path
    if font_size == None:
      font_size = 20
      
    self.scenario_script.append(["Font_settings_Reservation",[font_name,font_kind,font_size]])
    
    
  # 1文字出力
  def text_box(self,output_text,font_obj_name,x_mas_con,y_mas_con):
    if len(output_text) != 1:
      print("1文字のみの出力のみを許可しています。")
      raise 0
    
    self.scenario_script.append(["text_box_Reservation",[output_text,font_obj_name,x_mas_con,y_mas_con]])
    
    
  # 1文字出力(座標自由)
  def text_box_free(self,output_text,font_obj_name,x_mas_con,y_mas_con):
    if len(output_text) != 1:
      print("1文字のみの出力のみを許可しています。")
      raise 0
    
    self.scenario_script.append(["text_box_free_Reservation",[output_text,font_obj_name,x_mas_con,y_mas_con]])
    
  # 1文字出力(アニメーション)
  def text_box_animation(self,output_text,font_obj_name,x_mas_con_1,y_mas_con_1,x_mas_con_2,y_mas_con_2):
    if len(output_text) != 1:
      print("1文字のみの出力のみを許可しています。")
      raise 0

    self.scenario_script.append(["text_box_animation_Reservation",[output_text,font_obj_name,x_mas_con_1,y_mas_con_1,x_mas_con_2,y_mas_con_2]])  
    

  # 枠線の太さの値を設定する
  def set_Border_size(self,Border_num):
    self.scenario_script.append(["set_Border_size_Reservation",[Border_num]])
    
    
  # 画像の宣言
  def image_create(self,image_name,image_path,image_size = 1):
    self.scenario_script.append(["image_create_Reservation",[image_name,image_path,image_size]])
    
  # 画像の表示
  def image_rect(self,image_name,wight_grid_coordinates,height_grid_coordinates):
    self.scenario_script.append(["image_rect_Reservation",[image_name,wight_grid_coordinates,height_grid_coordinates]])  
    
  # 切り抜き画像の宣言
  def image_cut_create(self,image_name,image_path,cut_x_coordinates,cut_y_coordinates,cut_size,image_size = 1):
    self.scenario_script.append(["image_cut_create_Reservation",[image_name,image_path,cut_x_coordinates,cut_y_coordinates,cut_size,image_size]])
    
    
  # 画像の表示(アニメーション)
  def image_rect_animation(self,image_name,x_mas_con_1,y_mas_con_1,x_mas_con_2,y_mas_con_2):
    self.scenario_script.append(["image_rect_animation_Reservation",[image_name,x_mas_con_1,y_mas_con_1,x_mas_con_2,y_mas_con_2]])  
    
  # 線を引く
  def line_display(self,x_con_1,y_con_1,x_con_2,y_con_2):
    self.scenario_script.append(["line_display_Reservation",[x_con_1,y_con_1,x_con_2,y_con_2]])  
    
    
  # BGMを宣言する
  def BGM_create(self,BGM_name,BGM_path):
    self.scenario_script.append(["BGM_create_Reservation",[BGM_name,BGM_path]])
    
  # BGMを流す
  def BGM_play(self,BGM_name):
    self.scenario_script.append(["BGM_play_Reservation",[BGM_name]])
    
  # SEを流す
  def SE_play(self,BGM_name):
    self.scenario_script.append(["SE_play_Reservation",[BGM_name]])
    
  # BGMを無限ループ()
  # def BGM_loop_play(self,BGM_name):
  #   self.scenario_script.append(["BGM_play_Reservation",[BGM_name]])
    
  # BGMの音声の変更
  def BGM_volume(self,BGM_name,volum_parsent):
    self.scenario_script.append(["BGM_volume_Reservation",[BGM_name,volum_parsent]])
    
  # BGMの停止をする
  def BGM_stop(self,BGM_name):
    self.scenario_script.append(["BGM_stop_Reservation",[BGM_name]])
    
  # BGMのメモリを解放する
  def BGM_memory_delete(self,BGM_name):
    self.scenario_script.append(["BGM_memory_delete_Reservation",[BGM_name]])
  
  
  # grid線を引く
  def grid_lines(self,start_math_x,start_math_y,last_math_x,last_math_y):
    self.scenario_script.append(["grid_lines_Reservation",[start_math_x,start_math_y,last_math_x,last_math_y]])
    
  
  # マップ出力
  def map_display(self,map,con):
     self.scenario_script.append(["map_display_Reservation",[map,con]])
     

  # マップ出力(アニメーション)
  def map_display_animation(self,map,x1,y1,x2,y2):
     self.scenario_script.append(["map_display_animation_Reservation",[map,x1,y1,x2,y2]])
     
  
  # 複数文字列を好きな座標で出力可能
  def texts_free(self,output_text,font_obj_name,x_mas_con,y_mas_con):    
    self.scenario_script.append(["texts_free_Reservation",[output_text,font_obj_name,x_mas_con,y_mas_con]])
    
  # マップ出力_制限
  def limit_map_display(self,map,con_x,con_y,start_map_x,start_map_y,final_map_x,fainal_map_y):
     self.scenario_script.append(["limit_map_display_Reservation",[map,con_x,con_y,start_map_x,start_map_y,final_map_x,fainal_map_y]])
     
  # マップ出力_制限_アニメーション
  def limit_map_display_animation(self,map,con_x,con_y,start_map_x,start_map_y,final_map_x,fainal_map_y,move_x,move_y):
     self.scenario_script.append(["limit_map_display_animation_Reservation",[map,con_x,con_y,start_map_x,start_map_y,final_map_x,fainal_map_y,move_x,move_y]])
          
               
  # 生画像の宣言
  def raw_image_create(self,image_name,image_path,image_size_height,image_size_wight):
    self.scenario_script.append(["raw_image_create_Reservation",[image_name,image_path,image_size_height,image_size_wight]])    
     
     
  # プレイヤー作成
  def CAST_IN_THE_NAME_OF_GOD___YE_NOT_GUILTY(self):
    if self.Dominus == False:
      self.Dominus = True
      self.prayer = Prayer(self)
    elif self.Dominus == True:
      print("YE_GUILTY")
      exit
      
  def Crank_up(self):
    self.Dominus = False
    
  def prayer_damage(self,damage):
    self.prayer.damage_box.append(damage)
    
    
  # 登場人物作成
  def go_on_stage(self,name):
    if name in self.character:
      print(f"その役（{name}）は既に与えられています")
    else:
      self.character[name] = Character(self,name)    
      self.character[name].name = name
      
  def Crank_up_Character(self,name):
    if name in self.character:
      self.character[name].Crank_up = True
    else:
      print(f"{name}は存在しません")
      
  def Character_damage(self,name,damage):
    self.character[name].damage_box.append(damage)


  # 図形を描く(アニメーション_fps_setting)
  def rect_animation_fps_setting(self,wight_grid_coordinates_1,height_grid_coordinates_1,wight_grid_coordinates_2,height_grid_coordinates_2,start_fps,final_fps,math_size=None):
    if math_size == None:
      math_size = 1
    elif math_size <= 0:
      print("マスの大きさが0以下です")
      raise 0 

    self.scenario_script.append(["rect_animation_fps_setting_Reservation",[wight_grid_coordinates_1,height_grid_coordinates_1,wight_grid_coordinates_2,height_grid_coordinates_2,start_fps,final_fps,math_size]])     


  # 図形を描く_free_size(アニメーション_fps_setting)
  def rect_animation_fps_setting_free_size(self,wight_grid_coordinates_1,height_grid_coordinates_1,wight_grid_coordinates_2,height_grid_coordinates_2,start_fps,final_fps,math_size_w,math_size_h):
    self.scenario_script.append(["rect_animation_fps_setting_free_size_Reservation",[wight_grid_coordinates_1,height_grid_coordinates_1,wight_grid_coordinates_2,height_grid_coordinates_2,start_fps,final_fps,math_size_w,math_size_h]])  


  # 画像_free_size(アニメーション_fps_setting)   
  def image_rect_animation_fps_setting_free_size(self,image_name,wight_grid_coordinates_1,height_grid_coordinates_1,wight_grid_coordinates_2,height_grid_coordinates_2,start_fps,final_fps):
    self.scenario_script.append(["image_rect_animation_fps_setting_free_size_Reservation",[image_name,wight_grid_coordinates_1,height_grid_coordinates_1,wight_grid_coordinates_2,height_grid_coordinates_2,start_fps,final_fps]])  
        
        
  # マップ出力_制限_アニメーション
  def limit_map_display_animationn_fps_setting(self,map,con_x,con_y,start_map_x,start_map_y,final_map_x,fainal_map_y,move_x,move_y,start_fps,final_fps,bools = False):
     self.scenario_script.append(["limit_map_display_animation_fps_setting_Reservation",[map,con_x,con_y,start_map_x,start_map_y,final_map_x,fainal_map_y,move_x,move_y,start_fps,final_fps,bools]])
     
     
  # 画像の宣言(回転)
  def image_create_rotate(self,image_name,image_path,rotate = 0,image_size = 1):
    self.scenario_script.append(["image_create_rotate_Reservation",[image_name,image_path,image_size,rotate]])
         
     
# プレイヤークラス作成
class Prayer:
  def __init__(self,obj):
    # プレイヤーの座標
    self.Prayer_conmaas_x = 0
    self.Prayer_conmaas_y = 0
    
    # 存在登録
    obj.auto_scenario_script.append(["Prayer_action_Reservation",[self],[obj]])
    
    # プレイヤーHP
    self.MX_HP = 1
    self.HP = 1
    self.MX_energy = 1
    self.energy = 1
    self.defence = 1
    self.death_flag = False
    self.hyper_muteki = False
    self.TPS_clock = 0
    
    # ダメージ
    self.damage_box = []
    
    # メモリ
    self.role = None
    self.prayer_img = None
    self.memori_1 = None
    self.memori_2 = None
    self.memori_3 = None
    self.memori_4 = None
    
    
# キャラクタークラス作成
class Character:
  def __init__(self,obj,name):
    # 削除フラグ
    self.Crank_up = False
    # プレイヤーの座標
    self.Character_conmaas_x = 0
    self.Character_conmaas_y = 0
    
    # キャラクター名
    self.name = name
    
    # 存在登録
    obj.auto_scenario_script.append(["Character_action_Reservation",[self,self.name],[obj]])
    
    # キャラクターHP
    self.HP = 1
    self.death_flag = False
    self.hyper_muteki = False

    # ダメージ
    self.damage_box = []
    
    # メモリ
    self.role = None
    self.sub_role = None
    self.before_key = None
    self.Initialization = True
    self.memori_0 = None
    self.memori_1 = None
    self.memori_2 = None
    self.memori_3 = None 
    self.memori_4 = None 
    self.memori_5 = None 
    self.memori_6 = None 
    self.TPS_clock = 0
    self.lock = False

       