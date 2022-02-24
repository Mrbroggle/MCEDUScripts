agent.teleport_to_player()
agent.turn(TurnDirection.Right)
i = 0
while True:
    agent.destroy(FORWARD)
    agent.move(FORWARD, 1)
    agent.destroy(UP)

    i += 1
    if i == 5:
        agent.place(DOWN)
        agent.set_item(TORCH, 1, 1)
        
