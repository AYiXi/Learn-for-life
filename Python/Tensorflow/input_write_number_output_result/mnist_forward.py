import tensorflow as tf


INPUT_NODE = 784  # 28X28
OUTPUT_NODE = 10
LAYEAR1_NODE = 500  # 隐藏层的节点个数

# 定义神经网络的输入，参数和输出，定义前向传播过程
def get_weight(shape, regularizer):
    w = tf.Variable(tf.truncated_normal(shape, stddev=0.1), dtype=tf.float32)
    if regularizer is not None:
        tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w

def get_bias(shape):
    b = tf.Variable(tf.zeros(shape))
    return b

def forward(x, regularizer):
    w1 = get_weight([INPUT_NODE, LAYEAR1_NODE], regularizer)
    b1 = get_bias([LAYEAR1_NODE])
    y1 = tf.nn.relu(tf.matmul(x, w1) + b1)

    w2 = get_weight([LAYEAR1_NODE, OUTPUT_NODE], regularizer)
    b2 = get_bias([OUTPUT_NODE])
    y = tf.matmul(y1, w2) + b2
    return y

