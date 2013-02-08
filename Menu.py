import pygame

class EzMenu():
	def __init__(self, *options):
		"""Initialize the EzMenu! options should be a sequence of lists in the
		format of [option_name, option_function]"""
		
		self.options = options
		self.option = 0
		self.offset_x = 0
		self.offset_y = 0
		self.color = [0, 0, 0]
		self.width = 1
		self.hcolor = [255, 0, 0]
		self.font = pygame.font.Font(None, 32)
		self.height = len(self.options)*self.font.get_height()
		self.title = ''
		self.background_image = ''

		
	def setup_options(self):
		for menu_items in self.options:
			text = menu_items[0]
			font_rendered = self.font.render(text, 1, (0, 0, 0))
			if font_rendered.get_width() > self.width:
				self.width = font_rendered.get_width()
	
	def draw(self, screen, over):
		if not over:
			'''if self.background_image != None or self.background_image != '':
				screen.blit(self.background_image,(0,0))'''
			if self.title != None:
				screen.blit(pygame.font.Font(None, 42).render(self.title, 1, self.color),self.title_tl)
			menu_highlight=0
			for menu_items in self.options:
				if menu_highlight==self.option:
					menu_color = self.hcolor
				else:
					menu_color = self.color
				text = menu_items[0]
				font_rendered = self.font.render(text, 1, menu_color)
				if font_rendered.get_width() > self.width:
					self.width = font_rendered.get_width()
				screen.blit(font_rendered, (self.offset_x, self.offset_y + menu_highlight*self.font.get_height()))
				menu_highlight+=1

	
	def update(self, events):
		for event in events:
			if event.type == pygame.MOUSEMOTION:
				self.option = self.mouse_location(event.pos)
				#print self.option
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						self.options[self.option][1]()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					self.option += 1
				if event.key == pygame.K_UP:
					self.option -= 1
				if event.key == pygame.K_RETURN:
					self.options[self.option][1]()
		if self.option > len(self.options)-1:
			self.option = 0
		if self.option < 0:
			self.option = len(self.options)-1
			
	def mouse_location(self, pos):
		if pos[0] >= self.offset_x and pos[0] <= self.offset_x + self.width \
		and pos[1] >= self.offset_y and pos[1] <= self.offset_y + self.height:
			#print "pos", (pos[1] - self.offset_y)/self.font.get_height()
			return (pos[1] - self.offset_y)/self.font.get_height()
		return self.option
	
	def set_pos(self, x, y):
		"""Set the topleft of the menu at x,y"""
		self.x = x
		self.y = y
		
	def set_font(self, font):
		"""Set the font used for the menu."""
		self.font = font
	
	def set_highlight_color(self, color):
		"""Set the highlight color"""
		self.hcolor = color
		
	def set_normal_color(self, color):
		"""Set the normal color"""
		self.color = color
	
	def center_at(self, x, y):
		"""Center the center of the menu at x,y"""
		self.offset_x = x-(self.width/2)
		self.offset_y = y-(self.height/2)
		
	def set_bgimage(self, image_file):
		self.background_image = pygame.image.load(image_file) 
		
	def set_title(self, title, topleft):
		self.title = title
		self.title_tl = topleft
		
