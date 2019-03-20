import time
import sys
from time import sleep

from absl import app
from absl import flags
import zmq


FLAGS = flags.FLAGS
flags.DEFINE_string("lrn_addr", "localhost:10001",
                    "Learner address. ip:port or dns_name:port")
flags.DEFINE_string("task_index", "0", "task index.")


def main(_):
  context = zmq.Context()
  print("Connecting to server {}...".format(FLAGS.lrn_addr))
  socket = context.socket(zmq.REQ)
  socket.connect("tcp://{}".format(FLAGS.lrn_addr))
  while True:
    sleep(0.5)
    print("Sending request from task {}".format(FLAGS.task_index))
    socket.send ("Trajectory from task {}".format(FLAGS.task_index).encode('ascii'))
    #  Get the reply.
    message = socket.recv()
    print("Received: {}".format(message))


if __name__ == '__main__':
  app.run(main)
