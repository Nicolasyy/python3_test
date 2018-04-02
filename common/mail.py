#!/usr/bin/python3

import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error
from common.log import logger


class Email(object):
    def __init__(self, title, server, sender, receiver, password, message=None, path=None):
        """初始化Email

        :param title: 邮件标题，必填。
        :param message: 邮件正文，非必填。
        :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
        :param server: smtp服务器，必填。
        :param sender: 发件人，必填。
        :param password: 发件人密码，必填。
        :param receiver: 收件人，多收件人用“；”隔开，必填。
        """
        self.title = title
        self.message = message
        self.path = path
        self.msg = MIMEMultipart('related')
        self.server = server
        self.sender = sender
        self.receiver = receiver
        self.password = password

    def _attach_file(self, attach_file):
        """将单个文件添加到附件列表中"""
        att = MIMEText(open('%s' % attach_file, 'rb').read(), 'plain', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        file_name = re.split('[\\|/]',attach_file)
        att['Content-Disposition'] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {}'.format(attach_file))

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        # 邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))  # 邮件正文可更改为Html格式
        # 添加附件，支持多个附件(传入list)，或者单个附件(传入str)
        if self.path:
            if isinstance(self.path, list):
                for f in self.path:
                    self._attach_file(f)
            elif isinstance(self.path, str):
                self._attach_file(self.path)
            else:
                raise TypeError('Please pass in <type list> or <type str>, not {0}'.format(type(self.path)))

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP_SSL(self.server, 465)  # 使用ssl加密连接server
        except(gaierror and error) as e:
            logger.exception('发送邮件失败，无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)
        else:
            try:
                smtp_server.login(self.sender, self.password) # 登录
            except smtplib.SMTPAuthenticationError as e:
                logger.exception('用户名密码验证失败！%s', e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string()) # 发送邮件
            finally:
                smtp_server.quit()
                logger.info('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                            '同时检查收件人地址是否正确'.format(self.title, self.receiver))

if __name__ == '__main__':
    report = 'F:\\testReport.html'
    e = Email(title='测试报告',
              message='你好',
              receiver='zny591501006@gmail.com',
              server='smtp.qq.com',
              sender='591501006@qq.com',
              password='coajmzjmgytnbcef',
              path=report
              )
    e.send()