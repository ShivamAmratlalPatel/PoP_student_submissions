import life

g = life.Game(40)
g[0:36, 0:9] = life.glider_gun
g.play()
