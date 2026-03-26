player.onTravelled(WALK, function () {
    blocks.place(VINES, pos(2, 4, 0))
    gameplay.timeAdd(100)
    for (let index = 0; index < mobs.monster(ZOMBIE); index++) {
        if (true) {
            mobs.kill(
            mobs.target(NEAREST_PLAYER)
            )
        }
    }
})
player.onChat("run", function () {
	
})
