# python 彩票机选项目  
>__开发环境:__  
>* python3.x   
 
>__项目依赖__:  
>* redis(pip)
>* requests(pip) 
>* json
>* smtplib
>* email
>* time
>* datetime
##
>__目前功能:__
>- [x] 实现大乐透和双色球机选号  
>- [x] 实现缓存当日机选号码到Redis
>- [x] 实现获取当日彩票开奖号码并跟昨日缓存的机选号码做对比
##
>__后续实现:__
>- [x] 更多彩票类型的机选
>- [x] 定时任务自动将每日对应开奖的彩票类型机选号发送至指定邮箱
>- [x] 获取当天的开奖号码跟昨日机选号码做对比,发送邮箱通知命中球数    
>- [x] 定时任务未做，后续考虑部署服务器
##
__2021-7-8更新__
> 1.0版本已经初步完成,部署在乌班图上,采用shell脚本定时自动执行py文件的形式每天早上八点自动执行机选发送到指定邮箱
> ##
> __安装步骤__:
> * 将此项目clone到本地
> * 确保要安装的设备中有python3.x以上的环境
> * 执行 'pip3/pip install redis' 和 'pip3/pip install requests'
> * 修改 [redis_tool.py] 文件中的 host='你的redis地址'
> * 修改 [email_tool.py] 文件中的 username 和 password 为 你的邮箱和密码
> * 在 main.py 文件目录中执行 pyton main.py  
> ##
> __注意事项__:
> * 如果是在linux上运行,需要将email配置为ssl连接方式,否则会连接超时(改为ssl方式后若还是连接超时,请检查防火墙和对应的端口是否放行)
>   具体改的文件为 [email_tool.py] 中的 SMTP() 方法改为 SMTP_SSL() 方法, 25端口 改为 465  
> * Redis最好设置过期时间
> * 基类中的 [open_base_url] 为个人API,每天免费调用100次,作者贡献出来,恳请手下留情!
> * 附上shell脚本:  
> `#!/bin/bash`  
>   `PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin`  
>   `export PATH`  
>   `python 你的路径/main.py`  
>   `echo "----------------------------------------------------------------------------"  `
>   `endDate=date +"%Y-%m-%d %H:%M:%S"`
>   `echo "★[$endDate] Successful"`  
>   `echo "----------------------------------------------------------------------------"`  
> * 完 
##
>__说明__:  
>__作者正在python学习阶段 该项目纯属好玩 生成的彩票号码是随机产生 切勿当真__   
>__最后 欢迎大佬添砖加瓦和 star (抱拳)__
