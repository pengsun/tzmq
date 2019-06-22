import time
import datetime
import sys
import random
from os import path

from absl import app
from absl import flags
import zmq


FLAGS = flags.FLAGS
flags.DEFINE_string("port", "10001", "Learner port")
flags.DEFINE_string("save_dir", ".", "Model saving path")
flags.DEFINE_integer("save_freq", 12, "Model saving frequency in steps")


def now():
  return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")


def make_nn_modle(n_bytes=200):
  return bytearray([random.randint(0, 255) for _ in range(n_bytes)])


def make_cur_model_path():
  return path.join(FLAGS.save_dir, time.strftime('%Y%m%d%H%M%S') + '.model')


def main(_):
  context = zmq.Context()
  socket = context.socket(zmq.REP)
  socket.bind("tcp://*:%s" % FLAGS.port)
  step = 0
  while True:
    #  Wait for next request from client
    message = socket.recv()
    print(now() + "Learner: Received trajectory: {}".format(message))
    time.sleep(1)
    print(now() + "Learner: Sending NN model to port {}".format(FLAGS.port))
    socket.send("NN model from learner".encode('ascii'))

    # save model file periodically
    if step % FLAGS.save_freq == 0:
      model = make_nn_modle()
      p = make_cur_model_path()
      print("Learner: saving model to {}".format(p))
      with open(p, "wb") as f:
        f.write(model)

    step += 1


if __name__ == '__main__':
  app.run(main)
