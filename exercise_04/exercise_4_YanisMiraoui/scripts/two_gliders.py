from life import Game, Pattern, glider

g = Game(30)
g.insert(Pattern(glider), [1, 1])
g.insert(Pattern(glider).flip_horizontal(), [1, 28])
g.play()
