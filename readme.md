#git add # 全部文件
# git commit -m "备注""
# git tag 5d # 打上标签5d
# git push origin 5d #提交到5d




## 6a 执行的时候
## 先 
export FLASK_ADMIN='1319885580@qq.com' # 邮件介绍者
export MAIL_USERNAME='1257699625@qq.com'# 邮件发送者
export MAIL_PASSWORD='oyrohpxvpegaieja'## 生成码
export FLASK_APP=hello.py 
flask run

效果：向访问页面的时候，输入名称，会向服务器发送一封邮件
