# email

```python
import smtplib

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'your email'
password = 'your password'

to_addr = 'sendto email'

# html content
msg = MIMEText('<html><body><h1>smtplib</h1><p>send by <a href="https://python.silentnotes.top/">codingcat</a> ...</p></body></html>', 'html', 'utf-8')

# msg = MIMEText('Python smtplib send email demo', 'plain', 'utf-8')

msg['From'] = _format_addr('Python <{}>'.format(from_addr))
msg['To'] = _format_addr('Python <{}>'.format(to_addr))
msg['Subject'] = Header('From Python smtplib demo', 'utf-8')

# chose your smtp server
smtp_server = 'smtp.qq.com'
smtp_port = 465

server = smtplib.SMTP_SSL(smtp_server, smtp_port)

server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
```
