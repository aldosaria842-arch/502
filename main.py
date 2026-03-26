def on_travelled_walk():
    blocks.place(VINES, pos(2, 4, 0))
    gameplay.time_add(100)
    for index in range(mobs.monster(ZOMBIE)):
        if True:
            mobs.kill(mobs.target(NEAREST_PLAYER))
player.on_travelled(WALK, on_travelled_walk)

def on_on_chat():
    pass
player.on_chat("run", on_on_chat)
