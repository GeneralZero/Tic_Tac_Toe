import pygame
import AI

board =[[0,0,0],
        [0,0,0],
        [0,0,0]]
boxes_player = []
boxes_ai = []
wins = []
next_move_ai = []

class Game(object):
	def __init__(self):
		pygame.init()
		global board
		global wins
		global boxes_player
		global next_move_ai 
		self.screen = pygame.display.set_mode((300,300))
		self.game_over = False
		self.player_ai = AI.AI()
		self.player_ai.set_win_conditions(wins)
		
	def setup_board(self, white=0):
		if white == 0:
			self.screen.fill([255,255,255])
		pygame.draw.line(self.screen,(0,0,0),(100,0),(100,300))
		pygame.draw.line(self.screen,(0,0,0),(200,0),(200,300))
		pygame.draw.line(self.screen,(0,0,0),(0,100),(300,100))
		pygame.draw.line(self.screen,(0,0,0),(0,200),(300,200))
		
	def move(self, side, pos):
		board[pos[1]][pos[0]] = side
		pygame.draw.rect(self.screen,(side*100,0,side*100),(pos[0]*100,pos[1]*100,100,100))
		self.setup_board(white=1)
		self.check_win()
		if side == 2 and self.game_over == False:
			boxes_ai.append(pos)
		elif side == 1 and self.game_over == False:
			boxes_player.append(pos)
			self.move(2,self.player_ai.move(board, wins, boxes_player, boxes_ai))
			self.check_win()
			
	def check_win(self):
		for winners in wins:
			i=0
			#Check to see if player wins
			for boxes in boxes_player:
				if boxes in winners and self.game_over == False:
					i+=1
					if i==3:
						self.screen.blit(pygame.font.Font(None, 22).render('Player wins '+str(winners), True, (255, 255, 255), (159, 182, 205)), (10,150))
						self.game_over = True
			i=0
			#Check to see if AI wins
			for boxes in boxes_ai:
				if boxes in winners and self.game_over == False:
					i+=1
					if i==3:
						self.screen.blit(pygame.font.Font(None, 22).render('AI wins '+str(winners), True, (255, 255, 255), (159, 182, 205)), (10,150))
						self.game_over = True
		#Check To see if none wins
		open_squares = [[i, j] for i in range(3) for j in range(3) if board[i][j] == 0]
		if len(open_squares) == 0:
			#print "Tie Game"
			self.screen.blit(pygame.font.Font(None, 22).render('Tie Game', True, (255, 255, 255), (159, 182, 205)), (150,150))
			self.game_over = True
			
	def main_loop(self, ai_first):
		self.setup_board()
		#Does AI move first?
		if(ai_first):
			self.move(2,self.player_ai.move(board, wins, boxes_player, boxes_ai))
		#Game Loop
		while self.game_over==False:
			self.G_input()
			pygame.display.flip()
			if self.game_over==True:
				pygame.time.wait(1000)
					
	def G_input(self):
		#Get Mouse and Keyboard input
		mousepos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				#Select square on which was clicked on
				if board[int(mousepos[1]/100)][int(mousepos[0]/100)] == 0 and event.button == 1:
					self.move(1,[int(mousepos[0]/100),int(mousepos[1]/100)])
				if event.type == pygame.QUIT:
					pygame.quit()
					self.game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.game_over = True
					pygame.quit()
if __name__ == "__main__":
	g=Game()
