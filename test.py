from flask_script import Manager
from hello import Message
msg = Message('test subject', sender='1257699625@qq.com', recipients=['1319885580@qq.com'])
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
with app.app_context():
	mail.send(msg)
