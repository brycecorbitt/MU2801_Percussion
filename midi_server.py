from pymidi import server
from percussion import PercussionMotor

drum = PercussionMotor(0, 13, 26, 16)

class MIDIHandler(server.Handler):
    def __init__(self):
        self.logger = None

    def on_peer_connected(self, peer):
        print('Peer connected: {}'.format(peer))

    def on_peer_disconnected(self, peer):
        print('Peer disconnected: {}'.format(peer))

    def on_midi_commands(self, peer, command_list):
        for command in command_list:
            if command.command == 'note_on':
                key = command.params.key
                velocity = command.params.velocity
                print('Someone hit the key {} with velocity {}'.format(key, velocity))
                drum.hit()

midi_server = server.Server([('::', 5051)])

midi_server.add_handler(MIDIHandler())
midi_server.serve_forever()