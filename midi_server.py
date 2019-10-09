from pymidi import server
from percussion import PercussionMotor

drum = PercussionMotor(0, 13, 26, 16)

class MIDIHandler(server.handler)
    def on_peer_connected(self, peer):
        print('Peer connected: {}'.format(peer))

    def on_peer_disconnected(self, peer):
        print('Peer disconnected: {}'.format(peer))

    def on_midi_commands(self, command_list):
        for command in command_list:
            if command.command == 'note_on':
                key = command.params.key
                velocity = command.params.velocity
                print('Someone hit the key {} with velocity {}'.format(key, velocity))
                drum.hit()
Then install it in a server and start serving:

server = new Server()
server.add_handler(MIDIHandler())
server.serve_forever()