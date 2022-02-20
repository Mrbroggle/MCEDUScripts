agent.teleport_to_player()
i=0
agent.set_item(TORCH, 1, 1)
agent.set_slot(1)

while True:
    agent.destroy(FORWARD)
    agent.move(FORWARD, 1)
    agent.destroy(UP)
    agent.destroy(DOWN)
    loops.pause(30)
    agent.move(DOWN, 1)
    agent.collect_all()
    i += 1
    if i == 5:
        agent.place(DOWN)
        agent.set_item(TORCH, 1, 1)
        i = 0
