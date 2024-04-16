<h1 align="center">Backupoo</h1>

这是阿里云 OSS 自动备份模块，用于实现本地文件定时同步到阿里云 OSS。

<h2>环境配置</h2>

- 根据官方文档，Linux 系统需要安装 python-devel，否则会对性能有较大影响，安装命令如下：

  ```bash
  sudo apt-get install python-dev
  ```

- 安装 SDK；

  ```python
  pip install oss2
  ```

- 详情请参考[官方文档](https://help.aliyun.com/zh/oss/developer-reference/python/)。
