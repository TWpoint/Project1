# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import cv2
import numpy as np
import os
import itertools
import torch.utils.data as utils_data

a= cv2.resize(cv2.imread('./dataset/images/left/left (1).jpg'),(48,48))
cv2.imshow('',a)

cv2.waitKey(0)
