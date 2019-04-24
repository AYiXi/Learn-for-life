import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import mnist_forward, mnist_generateds
import os

BATCH_SIZE = 200
STEPS = 50000
MOVING_AVERAGE_DECAY = 0.99
MODEL_SAVE_PATH = 'F:\Jupyter notebook\Meachine Learning\data\model'
MODEL_NAME = 'mnist_model'
LEARN_RATE_BASE = 0.1
LEARN_RATE_DECAY = 0.99
REGULARIZER = 0.0001
train_num_examples = 60000  # 总样本数

def backward():
    x = tf.placeholder(tf.float32, shape=(None, mnist_forward.INPUT_NODE))
    y_true = tf.placeholder(tf.float32, shape=(None, mnist_forward.OUTPUT_NODE))
    y_predict = mnist_forward.forward(x, REGULARIZER)

    global_step = tf.Variable(0, trainable=False)

    ce = tf.nn.sparse_softmax_cross_entropy_with_logits(
        logits=y_predict,
        labels=tf.argmax(y_true, 1)
    )
    cem = tf.reduce_mean(ce)
    loss = cem + tf.add_n(tf.get_collection('losses'))

    learning_rate = tf.train.exponential_decay(
        LEARN_RATE_BASE,
        global_step,
        train_num_examples / BATCH_SIZE,
        LEARN_RATE_DECAY,
        staircase=True
    )

    # 有正则化
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(
        loss,
        global_step=global_step
    )

    ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    ema_op = ema.apply(tf.trainable_variables())
    with tf.control_dependencies([train_step, ema_op]):
        train_op = tf.no_op(name='train')

    saver = tf.train.Saver()
    # 一次批获取·batch·组
    img_batch, label_batch = mnist_generateds.get_tfrecord(BATCH_SIZE, is_train=True)

    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)

        ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
        print(ckpt)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)

        # 调用线程协调器
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess, coord)

        for i in range(STEPS):
            # xs, ys = mnist.train.next_batch(BATCH_SIZE)
            xs, ys = sess.run([img_batch, label_batch])
            _, loss_value, step = sess.run([train_op, loss, global_step],
                                           feed_dict={x: xs, y_true: ys})
            if i % 100 == 0:
                print(f'Step: {step}, loss: {loss_value}')
                saver.save(sess,
                           os.path.join(MODEL_SAVE_PATH, MODEL_NAME),
                           global_step=global_step
                           )
        coord.request_stop()
        coord.join(threads)


if __name__ == '__main__':
    mnist = input_data.read_data_sets(r'F:\Jupyter notebook\Meachine Learning\data\mnist\input_data', one_hot=True)
    backward()



