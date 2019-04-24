import tensorflow as tf
import numpy as np
from PIL import Image
import mnist_backward
import mnist_forward

def restore_model(pic_array):
    with tf.Graph().as_default() as tg:
        x = tf.placeholder(tf.float32, [None, mnist_forward.INPUT_NODE])
        y = mnist_forward.forward(x, None)
        pre_value = tf.argmax(y, 1)

        # 实例化带有滑动平均值的saver
        variable_averages = tf.train.ExponentialMovingAverage(mnist_backward.MOVING_AVERAGE_DECAY)
        variable_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variable_to_restore)

        with tf.Session() as sess:
            ckpt = tf.train.get_checkpoint_state(mnist_backward.MODEL_SAVE_PATH)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess, ckpt.model_checkpoint_path)

                pre_value = sess.run(pre_value, feed_dict={x: pic_array})
                return pre_value
            else:
                print('No checkpoint file found!')
                return -1

def pre_pic(pic_name):
    img = Image.open(pic_name)
    resize_img = img.resize((28, 28), Image.ANTIALIAS)  # 用消除锯齿的方法resize
    img_array = np.array(resize_img.convert('L'))  # 变成灰度图
    threshold = 50
    for i in range(28):          # 使图片反色，只留下阈值点，尽量消除噪声
        for j in range(28):
            img_array[i][j] = 255 - img_array[i][j]
            if img_array[i][j] < threshold:
                img_array[i][j] = 0
            else:
                img_array[i][j] = 255

    new_img_array = img_array.reshape([1, 784]).astype(np.float32)
    img_ready = np.multiply(new_img_array, 1.0/255.0)
    return img_ready  # 整理好的待识别图片

def application():
    test_num = int(input('input the number of test pictures:'))
    for i in range(test_num):
        test_pic = input('path:')
        test_pic_address = pre_pic(test_pic)
        pre_value = restore_model(test_pic_address)
        print('the prediction number is:', pre_value)

if __name__ == '__main__':
    application()



