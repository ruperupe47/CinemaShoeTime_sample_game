import Cinema_ShoeTime
import gs_statu
import map_dic
import map_info
import player_cons
import efect_dis
import mob
import enmy_efect_dis
import random
import rasbos


def setting(app):
  global GS
  # デバッグ用
  # GS.debag = True
  GS.Initialization = False

  # GSの設定
  GS.status = "blick"
  GS.begore_status = "黒"
  GS.map_data  = None
  GS.map_judg = None
  GS.map_kind = None
  GS.part = 0
  GS.new_part = 0  
  
  # 設定
  app.tps = 0.25
  
  # フォントの宣言
  app.Font_settings() # default_font
  app.Font_settings("title_font","フォント/NotoSerifJP-VariableFont_wght.ttf",80)
  app.Font_settings("30_font","フォント/NotoSerifJP-VariableFont_wght.ttf",30) 
  app.Font_settings("40_font","フォント/NotoSerifJP-VariableFont_wght.ttf",40) 
  app.Font_settings("small_font","フォント/NotoSerifJP-VariableFont_wght.ttf",15)
  app.Font_settings("13_font","フォント/NotoSerifJP-VariableFont_wght.ttf",13)  
  app.Font_settings("60_font","フォント/NotoSerifJP-VariableFont_wght.ttf",60) 
  app.Font_settings("8_font","フォント/NotoSerifJP-VariableFont_wght.ttf",8)  
  
  # 画像の宣言
  prayer_img_dic = map_dic.prayer_img_dic
  for key,path in prayer_img_dic.items():
    app.image_create_rotate(key+"_W",path,1,0)
    app.image_create_rotate(key+"_A",path,1,1)
    app.image_create_rotate(key+"_S",path,1,2)
    app.image_create_rotate(key+"_D",path,1,3)
  
  mob_img_dic = map_dic.mob_img_dic
  for key,path in mob_img_dic.items():
    app.image_create_rotate(key+"_W",path,1,0)
    app.image_create_rotate(key+"_A",path,1,1)
    app.image_create_rotate(key+"_S",path,1,2)
    app.image_create_rotate(key+"_D",path,1,3)
      
  key = "セイメイ"
  path = "画像素材/ラスボス/モノノケセイメイ.PNG"
  app.image_create_rotate(key+"_W",path,3,0)
  app.image_create_rotate(key+"_A",path,3,1)
  app.image_create_rotate(key+"_S",path,3,2)
  app.image_create_rotate(key+"_D",path,3,3)   
  
  sraid_img_dic = map_dic.sraid_img_dic
  for key,path in sraid_img_dic.items():
    app.raw_image_create(key,path,900,600)
  


  # 音声の宣言
  app.BGM_create("飛行音","音声素材/エフェクト/nc478417_高速移動する音【効果音】.mp3")
  app.BGM_volume("飛行音",20)
  app.BGM_create("キャタピラ走行","音声素材/エフェクト/nc308104_キャタピラ走行.wav")
  app.BGM_volume("キャタピラ走行",20)  
  app.BGM_create("キャタピラ走行","音声素材/エフェクト/nc308104_キャタピラ走行.wav")
  app.BGM_volume("キャタピラ走行",20)  
  app.BGM_create("ロボットSF","音声素材/エフェクト/nc303274_SFチックなロボットが空に飛び立つような音。動作音。.wav")
  app.BGM_volume("ロボットSF",20)  
  app.BGM_create("巨大ロボット","音声素材/エフェクト/nc393408_巨大ロボット・歩く・二歩.mp3")
  app.BGM_volume("巨大ロボット",10)    
  
  app.BGM_create("nc426264_打撃音4","音声素材/敵エフェクト/nc426264_打撃音4.mp3")
  app.BGM_volume("nc426264_打撃音4",10)      
  app.BGM_create("小化け物の威嚇","音声素材/敵エフェクト/nc46181_小化け物の威嚇.mp3")
  app.BGM_volume("小化け物の威嚇",10)      
  app.BGM_create("刀で打ち合う音","音声素材/敵エフェクト/nc425836_刀で打ち合う音.mp3")
  app.BGM_volume("刀で打ち合う音",10)       
  app.BGM_create("悪魔の笑い声","音声素材/敵エフェクト/nc296545_悪魔の笑い声(オス).wav")
  app.BGM_volume("悪魔の笑い声",10)       
  app.BGM_create("月人","音声素材/敵エフェクト/nc164731_神秘音.wav")
  app.BGM_volume("月人",10)         
  app.BGM_create("獣の唸る声","音声素材/敵エフェクト/nc364539_獣の唸る声.wav")
  app.BGM_volume("獣の唸る声",10)    
  app.BGM_create("神社の鈴","音声素材/敵エフェクト/nc426414_神社の鈴の音.mp3")
  app.BGM_volume("神社の鈴",10)    
  app.BGM_create("消滅音.mp3","音声素材/敵エフェクト/nc231914_消滅音.mp3")
  app.BGM_volume("消滅音.mp3",10)    

  app.BGM_create("つるはし","音声素材/敵エフェクト/nc225827_つるはし.mp3")
  app.BGM_volume("つるはし",10)     
  app.BGM_create("タイトルクリック","音声素材/素材/Kagura_Suzu01/Kagura_Suzu01-2.mp3")
  app.BGM_volume("タイトルクリック",30)   
  app.BGM_create("爆発音_ehu","音声素材/敵エフェクト/nc446378_効果音;爆発音.mp3")
  app.BGM_volume("爆発音_ehu",10)    

  app.BGM_create("Over Drive","音声素材/エフェクト/Over Drive.mp3")
  app.BGM_volume("Over Drive",50)    
        
                
  voice_dic = map_dic.voice_dic
  for key,path in voice_dic.items():
    app.BGM_create(key,path)
    app.BGM_volume(key,200)    

   
  # GS.status = "ゲーム"
  # GS.Initialization = True

  # GS.status = "ポーズ"
  
  # GS.status = "エンドスコア"


def ad_lib(app):
  global GS
  
  # 初期化のために使用
  if GS.Initialization == True:
    GS.Initialization = False
    GS.debag = False   # デバッグ変数
    
    GS.death_mob = 0
    
    GS.kara_count = 0
    GS.oni_1_count = 0
    GS.oni_2_count = 0
    GS.oni_3_count = 0
    
    GS.kumo_count = 0
    GS.kitune_count = 0
    GS.oogao_count = 0
    GS.tuki_1_count = 0
    
    GS.tuki_2_count = 0
    GS.tuki_3_count = 0   
    GS.tuki_4_count = 0 
    
    # ロジッククロック
    GS.rogic_clock = 0    
    
    # ゲームパラメータ
    GS.num = 0
    GS.clock = 0     # クロック
    GS.enter_clock = 0     # クロック
    GS.clock_1 = 0
    GS.clock_2 = 0
    GS.clock_3 = 0    
    GS.clock_4 = 0
    GS.Peeled = 2 # 方向
    GS.lock = False
    
    # 初期化用
    GS.Initialization = False
    
    # マップデータ
    GS.map_data = None # マップの描写データ
    GS.map_judg = None # マップの当たり判定
    GS.map_kind = None # マップの物体種類
    
    # メモリー
    GS.part = 0 # 説明とポーズ画面で使うメモリー
    GS.new_part = None # 説明とポーズ画面で使うメモリー
    GS.enter_parameter = False
    
    # 敵 
    GS.mob = [] # ["name",(x,y)]
    GS.bos = [] # ["name",(x,y)]
    GS.mob_count = 0
    GS.counter = 0
    
    # 
    GS.before_mob = []
    
    # スキルエフェクト
    GS.beam = False
    GS.bumerann_en = False
    GS.cuter_en = False
    GS.cut_en = False
    GS.misairu_ka = False
    GS.hariken_kai = False
    GS.toruned_kai = False
    GS.dorirucut_kai = False
    GS.orosi_mika = False
    GS.misairuran_mika = False
    
    GS.enrgy_flag = True
    
    
    # ゲーム内パラメーター
    GS.efficiency_meter = 10 # 出力効率メーター
    GS.power_count = 0 # パワーが上がる条件
    GS.ps_energy = 0# エネルギー回復量
    GS.ps_HP = 0 # HP回復量
    GS.plus_damage = 0 # 追加ダメージ分
    GS.kimewaza = False
    
    
    # 倒した敵の数
    GS.death_mob = 0
    
        
    app.set_color(0)
    app.background()
    import copy
    GS.map_data = copy.deepcopy(map_info.map_record)
    GS.efficiency_meter = 10
    map_img_dic = map_dic.map_img_dic
    for k,v in map_img_dic.items():
      app.image_create(k,v)  
      
    # プレイヤー初期化
    app.CAST_IN_THE_NAME_OF_GOD___YE_NOT_GUILTY()
    app.prayer.memori_1 = 0
    app.prayer.memori_2 = 0
    
    app.prayer.Prayer_conmaas_x = 105
    app.prayer.Prayer_conmaas_y = 292
    
    app.prayer.role = "エンペラー"
    app.prayer.memori_3 = "オウエンペラー"
    app.prayer.prayer_img = app.prayer.memori_3 + "_W"
    app.prayer.memori_4 = ""
    
    
    app.prayer.MX_HP = 100
    app.prayer.HP = 100
    app.prayer.MX_energy = 50
    app.prayer.energy = 50
    app.prayer.defence = 0
    app.prayer.TPS_clock = 0
    
    GS.ps_HP = 10
    GS.ps_energy = 1
    GS.plus_damage = 0
    GS.kimewaza = False
    GS.enrgy_flag = True
    
    name = "セイメイ"
    app.go_on_stage(name)
    app.character[name].Character_conmaas_x = 104
    app.character[name].Character_conmaas_y = 5
    app.character[name].role = "セイメイ"
    app.character[name].sub_role = "セイメイ"
    
    # app.character[name].Character_conmaas_x = 104
    # app.character[name].Character_conmaas_y = 280 
    # app.prayer.Prayer_conmaas_x = 3
    # app.prayer.Prayer_conmaas_y = 3
    # GS.efficiency_meter = 50
    
    # app.prayer.Prayer_conmaas_x = 105
    # app.prayer.Prayer_conmaas_y = 50
        
          
   # デバッグステータス
  # GS.status = "エンドスコア"
  
  # クロックカウント
  GS.clock += 1
  
  # 背景
  app.set_color(125)
  app.background()
  
  # 状態遷移
  # print(GS.status)
  
  if GS.status == "タイトル":
    gs_statu.statu_title(app,GS)
  elif GS.status == "説明":
    gs_statu.statu_explanation(app,GS)
  elif GS.status == "ゲーム":
    gs_statu.statu_game(app,GS)
  elif  GS.status == "ポーズ":
    gs_statu.statu_pose(app,GS)
  elif GS.status == "エンドスコア":
    gs_statu.statu_end_scorea(app,GS)
  elif GS.status == "ポーズ_0":
    GS.rogic_clock += 1
    app.set_color(0)
    app.background()   
    if 2 <= GS.rogic_clock:
      GS.status = "ゲーム"
      
  elif GS.status == "ポーズ_1":
    GS.rogic_clock += 1
    app.set_color(0)
    app.background()   
    if 2 <= GS.rogic_clock:
      GS.status = "タイトル"
      
  elif GS.status == "エンド":
    GS.rogic_clock += 1
    app.set_color(0)
    app.background()   
    if 2 <= GS.rogic_clock:
      GS.status = "エンドスコア"

  elif GS.status == "death":
    GS.rogic_clock += 1
    app.set_color(0)
    app.background()   
    if 2 <= GS.rogic_clock:
      GS.status = "タイトル"            
            
  elif GS.status == "blick":
    GS.rogic_clock += 1
    
    if GS.begore_status ==  "黒":
      app.set_color(0)
      app.background()      
    elif GS.begore_status ==  "タイトル":
      pass
    elif GS.begore_status ==  "ゲーム":
      app.set_color(0)
      app.background()      
    elif GS.begore_status ==  "説明":
      app.set_color(0)
      app.background()      
      
    
    if GS.begore_status ==  "黒" and 2 <= GS.rogic_clock:
      GS.status = "タイトル"
      GS.rogic_clock = 0
    elif GS.begore_status ==  "タイトル" and 3 <= GS.rogic_clock:
      GS.status = "説明"
      GS.part = 0
      GS.new_part = 0
      GS.rogic_clock = 0
    elif GS.begore_status ==  "説明" and 3 <= GS.rogic_clock:
      GS.status = "ゲーム"
      GS.rogic_clock = 0      
      GS.Initialization = True
    elif GS.begore_status ==  "ゲーム" and 3 <= GS.rogic_clock:
      GS.status = "ポーズ"
      GS.rogic_clock = 0
      GS.part = 0
      GS.new_part = 0



  # デバック
  if GS.debag == True:
    app.set_stroke_color(0)
    app.set_stroke_color(255)
    app.grid_lines(0,0,44,30)
    print(f"x:{app.click_mouse_grid_pos[0]},y:{app.click_mouse_grid_pos[1]}")



class Game_System():
  def __init__(self):
    self.debag = False   # デバッグ変数
    
    # ロジッククロック
    self.rogic_clock = 0    
    
    # ゲームパラメータ
    self.num = 0
    self.status = None # ステータス
    self.begore_status = None # 1つ前のステータス
    self.clock = 0     # クロック
    self.enter_clock = 0     # クロック
    self.clock_1 = 0
    self.clock_2 = 0
    self.clock_3 = 0    
    self.clock_4 = 0
    self.Peeled = 2 # 方向
    self.lock = False
    
    # 初期化用
    self.Initialization = False
    
    # マップデータ
    self.map_data = None # マップの描写データ
    self.map_judg = None # マップの当たり判定
    self.map_kind = None # マップの物体種類
    
    # メモリー
    self.part = 0 # 説明とポーズ画面で使うメモリー
    self.new_part = None # 説明とポーズ画面で使うメモリー
    self.enter_parameter = False
    
    # 敵 
    self.mob = [] # ["name",(x,y)]
    self.bos = [] # ["name",(x,y)]
    self.mob_count = 0
    self.counter = 0
    
    # 
    self.before_mob = []
    
    # スキルエフェクト
    self.beam = False
    self.bumerann_en = False
    self.cuter_en = False
    self.cut_en = False
    self.misairu_ka = False
    self.hariken_kai = False
    self.toruned_kai = False
    self.dorirucut_kai = False
    self.orosi_mika = False
    self.misairuran_mika = False
    
    self.enrgy_flag = True
    
    
    # ゲーム内パラメーター
    self.efficiency_meter = 10 # 出力効率メーター
    self.power_count = 0 # パワーが上がる条件
    self.ps_energy = 0# エネルギー回復量
    self.ps_HP = 0 # HP回復量
    self.plus_damage = 0 # 追加ダメージ分
    self.kimewaza = False
    
    
    # 倒した敵の数
    self.death_mob = 0
    
    self.kara_count = 0
    self.oni_1_count = 0
    self.oni_2_count = 0
    self.oni_3_count = 0
    
    self.kumo_count = 0
    self.kitune_count = 0
    self.oogao_count = 0
    self.tuki_1_count = 0
    
    self.tuki_2_count = 0
    self.tuki_3_count = 0   
    self.tuki_4_count = 0 


# プレイヤー
def Prayer_action_rule(app):
  if GS.status == "ゲーム":
    Prayer_action(app)
    
def Prayer_action(app):   
  global GS
  
  player_cons.rimokon(app,GS)
  
  if app.prayer.death_flag == True:
    if 7 <= random.randint(0, 10):
      if app.prayer.HP <= 0:
        app.prayer.HP = 1
    else:
      app.prayer.death_flag = False
      for name,obj in app.character.items():
       app.Crank_up_Character(name)
      app.Crank_up()
      GS.status = "death"
    
      


# モブ
import re
def Character_action_rule(app, name):
  if GS.status == "ゲーム":
    mob_chr(app, name)
    
def mob_chr(app, name):
  global GS
  # result = re.search(r"\d+", text)
  # char = app.character[name]
  # print(name)
  
  if app.prayer.role == "エンペラー":
    if "ビーム" in name:
      efect_dis.beam(app,GS,name)
    elif "ブーメラン" in name:
      efect_dis.bumerann(app,GS,name)
    elif "カッター" in name:
      efect_dis.cuter(app,GS,name)  
    elif "切り" in name:
      efect_dis.cut(app,GS,name)    
      
  if app.prayer.role == "カイザー":
    if "ミサイル" in name:
      efect_dis.misairu(app,GS,name)
    elif "ハリケーン" in name:
      efect_dis.hariken(app,GS,name)
    elif "トルネード" in name:
      efect_dis.toruned(app,GS,name)  
    elif "ドリル切り" in name:
      efect_dis.dorirucut(app,GS,name)  
      
  if app.prayer.role == "ミカド":
    if "おろし" in name:
      efect_dis.orosi(app,GS,name)
    elif "クラスター" in name:
      efect_dis.misairuran(app,GS,name)
    elif "ロケット" in name:
      efect_dis.rocket(app,GS,name)  
    elif "パンチ" in name:
      efect_dis.panti(app,GS,name)      

  
  if app.character[name].role == "雑魚敵":
    mob.weak_enemies(app,GS,name)
  if app.character[name].role == "小敵":
    mob.Little_Enemy(app,GS,name)
  if app.character[name].role == "中敵":
    mob.Middle_enemy(app,GS,name)
  if app.character[name].role == "大敵":
    mob.arch_enemy(app,GS,name)
  
  
  if  app.character[name].role == "モブ_黒_レーザー":
    enmy_efect_dis.mob_beam_bluk(app,GS,name)
  elif  app.character[name].role == "モブ_白_レーザー":
    enmy_efect_dis.mob_beam_white(app,GS,name)    
  elif app.character[name].role == "モブ_ボム":
    enmy_efect_dis.mob_bom(app,GS,name)
    
  if app.character[name].role == "セイメイ":
    rasbos.seimei_enemies(app,GS,name)
  elif app.character[name].role == "守り手":
    mob.dif_enemies_action(app,GS,name)
    
    
  # GS.efficiency_meter = 51
  


if __name__ == '__main__':
  GS = Game_System()
  game = Cinema_ShoeTime.Cinema_ShowTime(44,30,25,"シチューにカツを見出す")