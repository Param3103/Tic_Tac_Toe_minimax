import copy

class TicTacToe:
    def __init__(self):
        self.game = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.X_scores = {'X': 1, 'O': -1, 'Tie': 0}
        self.O_scores = {'X': -1, 'O': 1, 'Tie': 0}

    def is_player_turn(self):
        X_count = 0
        O_count = 0
        for sq in self.game:
            if sq == 'X':
                X_count += 1
            elif sq == 'O':
                O_count += 1
            else:
                continue
        if X_count == O_count:
            return 'X'
        return 'O'
    def display_board(self):
        print('+-+-+-+')
        for i in range(3):
            print('', end='|')
            for j in range(3):
                print(self.game[i*3+j], end='|')
            print('')
            print('+-+-+-+')
    def is_winner(self):
        for i in range(3):
            if self.game[3*i] == self.game[3*i+1] == self.game[3*i+2]:
                return self.game[3*i]
        for i in range(3):
            if self.game[i] == self.game[3+i] == self.game[6+i]:
                return self.game[i]
        if self.game[0] == self.game[4] == self.game[8]:
            return self.game[0]
        if self.game[2] == self.game[4] == self.game[6]:
            return self.game[2]
        if len(self.space_is_free()) == 0:
            return 'Tie'
        return None
    def space_is_free(self):
        avail = []
        for i in range(1,10):
            if self.game[i-1] == i:
                avail.append(i)
        return avail
    def make_move(self, sign, position):
        if position in self.space_is_free():
            self.game[position-1] = sign
        else:
            return'Error!'
    def comp_move(self, sign):
        best_sq = TicTacToe.minimax(self, sign, 4)[1]
        self.game[best_sq-1] = sign

    def minimax(self, max_player, depth):
        min_player = 'O'
        scores = self.O_scores
        if max_player == 'O':
            min_player = 'X'
            scores = self.X_scores
        if depth == 0:
            return -10, None
        if self.is_winner() is not None:
            score = scores[self.is_winner()]
            return score, None
        if self.is_player_turn() is max_player:
            best_score = -100
            best_sq = None
            for sq in self.game:
                if sq == self.game.index(sq) + 1:
                    temp = self.game.index(sq)
                    self.game[temp] = max_player
                    score = TicTacToe.minimax(self, max_player, depth-1)[0]
                    self.game[temp] = sq
                    if score > best_score:
                        best_score = score
                        best_sq = sq
            return best_score, best_sq
        else:
            best_score = 100
            for sq in self.game:
                if sq == self.game.index(sq) + 1:
                    temp = self.game.index(sq)
                    self.game[temp] = min_player
                    score = TicTacToe.minimax(self, max_player, depth-1)[0]
                    self.game[temp] = sq
                    if score < best_score:
                        best_score = score
                        best_sq = sq
            return best_score, best_sq
