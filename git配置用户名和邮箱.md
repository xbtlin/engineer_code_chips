git每次commit都会用用户名和邮箱纪录。
1、查看用户名和地址
git config user.name
git config user.email

2、修改用户名和地址
git config --global user.name "your name"
git config --global user.email "your email"

如果想让配置仅在当前文件夹生效，那么把--global去掉就可以了。

