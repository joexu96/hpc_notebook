# Cuda by Examples
[ebook-zh](https://hpc.pku.edu.cn/docs/20170829223652566150.pdf)
[ebook-en](https://hpc.pku.edu.cn/docs/20170830181942363132.pdf)
[src](https://github.com/CodedK/CUDA-by-Example-source-code-for-the-book-s-examples-)


## 1. why cuda

1. 作为一个算法工程师,对底层计算不了解
2. 作为一个参与AI编译器开发的工程师,我对硬件单元不了解
3. AI 推理优化是我的目标, cuda 是业内常见的方案,gpu 也是最常被选的硬件, 了解 cuda 能不能帮我理解 基于 GPU 的AI 推理加速

## 2. work with Cuda C

配置开发环境

1. install cuda driver & toolkit
2. gcc

## 3. Cuda C

note: 
    1. 在GPU设备上执行的函数通常被成为kernel,核函数
    2. __global__ void kernel(void){} #定义空函数kernel,修饰符__global__告诉编译器,编译为在设备上而非主机上运行.
    3. kernel<<<1,1>>>();

