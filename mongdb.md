# 数据存储路径
data\db

# 激活存储路径
mongod --dbpath  安装路径\data\db

# 查看是否激活成功
localhost:27017

# 设置为windows 服务
mongodo --bind_ip 0.0.0.0 --logpath C:\MongoDB\3.4\data\logs\mongo.log
--logappend  --dbapth C:\MongoDB\3.4\data\db --port 27017 --serviceName "MongoDB" --serviceDisplayName "MongoDB" --install