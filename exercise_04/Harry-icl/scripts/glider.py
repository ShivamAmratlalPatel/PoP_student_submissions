import life

g = life.Game(20)
g[0:3, 0:3] = life.glider
g.play()
