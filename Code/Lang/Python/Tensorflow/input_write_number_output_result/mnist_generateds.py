import tensorflow as tf
from PIL import Image
import os

# 没有数据...
image_train_path = r'F:/Jupyter notebook/Meachine Learning/data/mnist_data_jpg/mnist_train_jpg_60000/'
label_train_path = r'F:/Jupyter notebook/Meachine Learning/data/mnist_data_jpg/mnist_train_jpg_60000.txt'
tfRecord_train = r'F:/Jupyter notebook/Meachine Learning/data/mnist_train.tfrecords'
image_test_path = r'F:/Jupyter notebook/Meachine Learning/data/mnist_data_jpg/mnist_test_jpg_10000/'
label_test_path = r'F:/Jupyter notebook/Meachine Learning/data/mnist_data_jpg/mnist_test_jpg_10000.txt'
tfRecord_test = r'F:/Jupyter notebook/Meachine Learning/data/mnist_test.tfrecords'
data_path = r'F:/Jupyter notebook/Meachine Learning/data'
resize_height = 28
resize_width = 28


def generate_tfrecord():
    if not os.path.exists(data_path):
        os.makedirs(data_path)
        print('the directory was created successfully.')
    else:
        print('directory already exist.')
    # 生成名叫·tfRecord_train·的tfrecord文件
    write_tfRecord(tfRecord_train, image_train_path, label_train_path)
    write_tfRecord(tfRecord_test, image_test_path, label_test_path)


def write_tfRecord(tfrecord_name, image_path, label_path):
    """
    0_5.jpg 5
    1_0.jpg 0
    2_4.jpg 4
    :param tfrecord_name: 文件名
    :param image_path: 图像路径
    :param label_path: 标签文件
    :return:
    """
    writer = tf.python_io.TFRecordWriter(tfrecord_name)
    num_pic = 0
    with open(label_path, 'r') as f:
        contents = f.readlines()

    for content in contents:
        value = content.split(' ')
        img_path = image_path + value[0]
        # 打开图片转换成二进制数据
        img = Image.open(img_path)
        img_raw = img.tobytes()
        labels = [0] * 10  # 构造全0数组
        labels[int(value[1])] = 1  # 标签位赋值为1

        example = tf.train.Example(
            features=tf.train.Feature(feature={
                'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw])),
                'label': tf.train.Feature(int64_list=tf.train.Int64List(value=labels)),
            }))
        writer.write(example.SerializeToString())  # 序列化
        num_pic += 1
        print('the number of pics:', num_pic)  # 打印进度提示
    writer.close()
    print('write tfrecord successful!')


def read_tfrecord(tfrecord_path):
    # 新建文件名队列
    filename_queue = tf.train.string_input_producer([tfrecord_path])
    reader = tf.TFRecordReader()
    # 每个样本保存到·serialized_example·中，进行解序列化
    _, serialized_example = reader.read(filename_queue)
    features = tf.parse_single_example(
        serialized_example,
        features={
            'label': tf.FixedLenFeature([10], tf.int64),   # 给出是几分类，手写数字是10分类
            'img_raw': tf.FixedLenFeature([], tf.string),  # 和制作时的键名相同
        }
    )
    img = tf.decode_raw(features['img_raw'], tf.uint8)
    img.set_shape([784])  # 变成1行784列
    img = tf.cast(img, tf.float32) * (1.0 / 255)  # 变成0-1之间的浮点数
    label = tf.cast(features['label'], tf.float32)
    return img, label


def get_tfrecord(num, is_train=True):
    """
    读取训练集或者测试集的标签
    :param num: 读取多少组
    :param is_train: 是否是训练集
    :return:
    """
    if is_train:  # 如果是训练集
        tfrecord_path = tfRecord_train
    else:
        tfrecord_path = tfRecord_test
    img, label = read_tfrecord(tfrecord_path)
    # 从总样本中顺序取出·num·组打乱顺序
    img_batch, label_batch = tf.train.shuffle_batch([img, label],
                                                    batch_size=num,
                                                    num_threads=2,
                                                    capacity=1000,
                                                    min_after_dequeue=700)
    return img_batch, label_batch


if __name__ == '__main__':
    generate_tfrecord()
