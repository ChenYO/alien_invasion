class Setting():
	#遊戲設定
	def __init__(self):
		#畫面基本設定
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230 ,230)
		#太空船速度設定
		self.ship_speed_factor = 1.5
		#子彈射擊設定
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60 , 60, 60
		self.bullets_allowed = 3
