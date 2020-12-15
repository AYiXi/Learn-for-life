# 3-live 一节课教你深度学习解决验证码识别问题
- [captcha_trainer](https://github.com/kerlomz/captcha_trainer)
- GPU 训练效率是 CPU 的几十倍
- 阿里云 GPU ECS:
  - 成都节点
  - 按量付费
  - 不自动安装 GPU 驱动
  - 带宽 100M
  - ubuntu 16.04
- 淘宝 <西电机房> GPU 2080Ti, 大约 900 一月 (2020.06.14)
- 下载 CUDA Toolkit 10.0, nvidia [runfile]
- 下载 cuDNN
- Anaconda, 清华镜像
- 环境验证: `nvidia-smi`, `nvcc -V`
- 创建虚拟环境, 安装 python library
- 倒入模型
- 开始训练
- 安装宝塔面板(官网), wget ....
- 寻找极验验证码的一些参数, 搜索 w `"\u0077"`
  - a: 图片地址
  - ep: 鼠标滑动轨迹, 时间戳, 版本等

# 极验
- Promise
- 两次 get, 两次 ajax
- w=o+n 参数
- script 断点
  - 每次进入 js 都会先断住
  - 找到大致相同结构
  - 对于每次返回不同的 js 有用
- 鼠标移动轨迹
  - UA 为手机时
  - fp = []
- 鼠标滑动轨迹
  - 多滑动几次, 模拟出来
  - 找一条成功的轨迹, 其他估计用缩放的方式模拟
  ```py
  def generate_path(pointer, scale_factor):
      x, y, t = pointer
      return [int(x * scale_factor), y, t]
  ```