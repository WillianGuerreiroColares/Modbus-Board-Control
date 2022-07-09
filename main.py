from Utils.engine import Engine

engine = Engine('COM6', 1, 9600, 10)

engine.open_all()

value = engine.read_channel_state(1)

engine.close_all()

value = engine.read_channel_state(1)

engine.open(2)

value = engine.read_multiple_channel_state(1,16)

print(value)

