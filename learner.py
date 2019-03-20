import time
import sys

from absl import app
from absl import flags
import zmq


FLAGS = flags.FLAGS
flags.DEFINE_string("port", "10001", "Learner port")


def main(_):
  context = zmq.Context()
  socket = context.socket(zmq.REP)
  socket.bind("tcp://*:%s" % FLAGS.port)
  while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received trajectory: {}".format(message))
    time.sleep(1)
    print("Sending NN model to port {}".format(FLAGS.port))
    socket.send("NN model from learner".encode('ascii'))


if __name__ == '__main__':
  app.run(main)
