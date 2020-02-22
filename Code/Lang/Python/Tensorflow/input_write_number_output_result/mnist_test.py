import tensorflow as tf
import time
from tensorflow.examples.tutorials.mnist import input_data
import mnist_forward
import mnist_backward
import mnist_generateds

TEST_NUM = 10000  # 测试的总样本数

def test(mnist_test):
    with tf.Graph().as_default() as g:
        x = tf.placeholder(tf.float32, shape=(None, mnist_forward.INPUT_NODE))
        y_true = tf.placeholder(tf.float32, shape=(None, mnist_forward.OUTPUT_NODE))
        y_predict = mnist_forward.forward(x, mnist_backward.REGULARIZER)

        # 所有参数加载时会赋值为各自的滑动平均值
        ema = tf.train.ExponentialMovingAverage(mnist_backward.MOVING_AVERAGE_DECAY)
        ema_restore = ema.variables_to_restore()
        saver = tf.train.Saver(ema_restore)

        correct_prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(y_true, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        img_batch, label_batch = mnist_generateds.get_tfrecord(TEST_NUM, is_train=False)

        while True:
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(mnist_backward.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]

                    coord = tf.train.Coordinator()
                    threads = tf.train.start_queue_runners(sess, coord)

                    xs, ys = sess.run([img_batch, label_batch])

                    accuracy_score = sess.run(accuracy,
                                              feed_dict={x: xs,
                                                         y_true: ys})
                    print(f'after {global_step} steps, accuracy is {accuracy_score}')

                    coord.request_stop()
                    coord.join(threads)

                else:
                    print('no checkpoint file found!')
            time.sleep(5)

if __name__ == '__main__':
    mnist = input_data.read_data_sets(r'F:\Jupyter notebook\Meachine Learning\data\mnist\input_data', one_hot=True)
    test(mnist)