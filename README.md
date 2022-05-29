# python信息收集工具
**输入系统名称，自动搜集相关资产信息**

### 运行效果
![run1](img/run1.png)
![run2](img/run2.png)
![run3](img/run3.png)
![run4](img/run4.png)
![run5](img/run5.png)

---
### 功能
- [x] 资产扫描
- [x] CDN识别
- [x] WAF识别
- [x] 指纹识别
- [x] 目录扫描
- [x] 端口扫描

---
### 使用

**扫描结果会自动保存在result文件夹下**
```
D:\信息搜集工具>python main.py -h
usage: main.py [-h] [-k KEY]

optional arguments:
  -h, --help         show this help message and exit
  -k KEY, --key KEY  搜索关键词
  
  
eg: python main.py -k xx大学 
    
    python main.py -k xx公司

```

---
### 配置

```
@ apikey.yaml

360Quake:
  X-QuakeToken : 
  Content-Type : 
Fofa:
  email : 
  key : 
```
