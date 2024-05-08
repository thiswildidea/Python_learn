## 目录
- [MongoDB](#MongoDB)
 - [数据存储路径](#数据存储路径)
 - [激活存储路径](#激活存储路径)
 - [查看是否激活成功](#查看是否激活成功)
 - [设置为windows服务](#设置为windows服务)
- [Redis](#Redis)
 - [相关软件](#相关软件)
 - [配置成windows服务](#配置成windows服务)
- [mysql](#mysql)
# MongoDB
## 数据存储路径
C:\MongoDB\3.4\data\db

## 激活存储路径
mongod --dbpath  C:\MongoDB\3.4\data\db

## 查看是否激活成功
localhost:27017

## 设置为windows服务
mongod --bind_ip 0.0.0.0 --logpath C:\MongoDB\3.4\data\logs\mongo.log
--logappend  --dbapth C:\MongoDB\3.4\data\db --port 27017 --serviceName "MongoDB" --install


# Redis
## 相关软件
MSOpentech\redis
RedisDesktop
## 配置成windows服务
redis-server --service-install redis.windows.conf 

# mysql
