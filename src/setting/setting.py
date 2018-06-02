class Setting():
	#遊戲設定
	def __init__(self):
		#畫面基本設定
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230 ,230)
		#太空船設定
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		#子彈射擊設定
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60 , 60, 60
		self.bullets_allowed = 3
		#alien設定
		self.alien_speed = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	#初始設定
	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed = 1

		self.fleet_direction = 1

	#升級時就增加一點難度
	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

