class AI(object):
	def __init(self):
		self.boxes_ai = []
		self.dificulity = 3
		self.more = []
		self.ai_set =[]
		self.player_set = []
		self.open_squares = []
	
	def move(self, board, wins, boxes_player, boxes_ai):
		self.open_squares = [[j, i] for i in range(3) for j in range(3) if board[i][j] == 0]
		return self.move_hard(wins, boxes_player, boxes_ai)
	
	def set_win_conditions(self, wins):
		for x in range(0,3):
			wins.append([[x,0],[x,1],[x,2]])
		for y in range(0,3):
			wins.append([[0,y],[1,y],[2,y]])
		wins.append([[0,0],[1,1],[2,2]])
		wins.append([[0,2],[1,1],[2,0]])
		self.ai_set =[]
		self.player_set = []
		
	def move_hard(self, wins, boxes_player, boxes_ai):
		#print board
		#print "Open", self.open_squares

		#Check for Win conditions or loose conditions
		ret = self.check_to_win(wins, boxes_ai)
		if ret != None:
			return ret
		ret = self.check_to_block(wins, boxes_player)
		if ret != None:
			return ret
		ret = self.check_to_trap(boxes_player)
		if ret != None:
			return ret
		ret = self.check_to_traped(boxes_ai)
		if ret != None:
			return ret
		
		#Place the first block
		firsts = [[1,1],[0,0],[0,2],[2,0],[2,2]]
		for a in firsts:
			if a in self.open_squares:
				#print "GO" ,a
				return a
		return self.open_squares[0]
	
	def check_to_block(self, wins, boxes_player):
		#Can Player Win next turn? 
		for winners in wins:   
			i=0
			for boxes in boxes_player:
				if boxes in winners:
					i+=1
					if not (winners in self.player_set):
						self.player_set.append(winners)
						#print "Player:", winners
					if i==2:
						for openbox in self.open_squares:
							if openbox in winners:
								#print self.open_squares
								#print "Block", openbox
								return openbox
					
	def check_to_win(self, wins, boxes_ai):
		for winners in wins:
			i=0
			#Can AI Win this turn?
			for boxes in boxes_ai:
				if boxes in winners:
					if not (winners in self.ai_set):
						self.ai_set.append(winners)
						#print "AI:", winners
					i+=1
				if i==2:
					for openbox in self.open_squares:
						if openbox in winners:
							#print "Win", openbox
							return openbox
						
	def check_to_trap(self, boxes_player):
		#Check to see if AI is trapped
		for a in self.ai_set:
			for b in boxes_player:
				if b in a and a in self.ai_set:
					self.ai_set.remove(a)
		for openbox in self.open_squares:
			i=0
			for winner in self.ai_set:
				if openbox in winner:
					i+=1
					if i>1:
						#print "Trapped:", openbox
						return openbox
		#print "AI Win Moves after"
		#for a in self.ai_set:
		#    print a

	def check_to_traped(self, boxes_ai):
		#Check to see if AI can trap Player
		for a in self.player_set:
			for b in boxes_ai:
				if b in a and a in self.player_set:
					self.player_set.remove(a)
		for openbox in self.open_squares:
			i=0
			for winner in self.player_set:
				if openbox in winner:
					i+=1
					if i>1:
						#print "Trapping:", openbox
						return openbox