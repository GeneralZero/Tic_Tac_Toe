import pygame
import Menu
import TickTakToe

class Main(object):
	def __init__(self):
		self.fullscreen = False
		self.resolution = (300,300)
		self.name = "Tick Tack Toe"
		self.exit = False
		pygame.init()
		pygame.display.set_caption(self.name)
		self.screen = pygame.display.set_mode(self.resolution)
		self.setup_menu(title=self.name)
		self.game = TickTakToe.Game()

		
	def setup_menu(self, title="My Game", image=None):
		self.menu = Menu.EzMenu(
			["AI goes First", self.ai_first],
			["Player goes First", self.ai_second],
			["Quit Game", self.quit_game])
		self.menu.set_title(title,(20,50))
		#self.menu.set_bgimage('images/bg.jpg')
		self.menu.set_highlight_color((0,0,255))
		self.menu.set_normal_color((0,0,0))
		self.menu.center_at(75,150)
		self.main_menu = True
		
	def ai_first(self):
		#print "AI goes First"
		self.main_menu = False
		g.game.main_loop(True)
		
	def ai_second(self):
		#print "Options"
		self.main_menu = False
		g.game.main_loop(False)
	
	def credit_screen(self):
		#print "Credits"
		self.main_menu = False
		
	def quit_game(self):
		self.game.game_over = True
		#pygame.quit()
		
if __name__ =="__main__":
	g=Main()
	g.screen.fill((255, 255, 255))
	while(not g.game.game_over):
		events = pygame.event.get()
		if(g.main_menu):
			g.menu.update(events)
			g.menu.draw(g.screen, g.game.game_over)
		else:
			g.game.G_input()
			#print "start game"
			
		pygame.display.flip()


