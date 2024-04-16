"""
_*_ coding   :    utf-8 _*_
@ File       :    authentication.py
@ Time       :    2024/04/10 23:20:03
@ Author     :    Farmer&Architect
@ Email      :    18797671241@163.com
@ Version    :    1.0
@ Description:    获取阿里云的STS认证凭据
"""
import os
import sys
from typing import Optional

from alibabacloud_sts20150401.client import Client as sts_client
from alibabacloud_sts20150401 import models as sts_models
from Tea.exceptions import TeaException
from alibabacloud_tea_openapi import models as tea_models
from alibabacloud_tea_util import models as util_models


class Token:
    """
     这是一个令牌
    """
    def __init__(self):
        self.request_id:Optional[str] = ''
        self.access_key_id: Optional[str] = ''
        self.access_key_secret: Optional[str] = ''
        self.expiration: Optional[str] = ''
        self.security_token: Optional[str] = ''

class Authenticator:
    def __init__(self):
        # 从环境变量中获取ACCESS_KEY_ID和ACCESS_KEY_SECRET
        self.__ACCESS_KEY_ID=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID']
        self.__ACCESS_KEY_SECRET=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        # 定义一个快一点的ENDPOINT、合理的持续时间、正确的角色名称和会话名称
        self.__ENDPOINT = 'sts.cn-guangzhou.aliyuncs.com'
        # 最小值为900
        self.__DURATION_SECONDS = 900
        self.__ROLE_ARN = 'acs:ram::1265013316073857:role/guangzhan2-manager'
        self.__ROLE_SESSION_NAME = 'guangzhan2-manager'

    def __createClient(self) -> sts_client:
        config = tea_models.Config(access_key_id=self.__ACCESS_KEY_ID,
                                  access_key_secret=self.__ACCESS_KEY_SECRET,
                                  endpoint=self.__ENDPOINT)
        return sts_client(config=config)

    @staticmethod
    def getToken() -> Token:
        authenticator = Authenticator()
        token = Token()
        client = authenticator.__createClient()
        assume_role_request = sts_models.AssumeRoleRequest(
            duration_seconds=authenticator.__DURATION_SECONDS,
            role_arn=authenticator.__ROLE_ARN,
            role_session_name=authenticator.__ROLE_SESSION_NAME
        )
        runtime = util_models.RuntimeOptions()
        try:
            assume_role_response = client.assume_role_with_options(assume_role_request, runtime)
            token.request_id = assume_role_response.body.request_id
            token.access_key_id = assume_role_response.body.credentials.access_key_id
            token.access_key_secret = assume_role_response.body.credentials.access_key_secret
            token.expiration = assume_role_response.body.credentials.expiration
            token.security_token = assume_role_response.body.credentials.security_token
            # TODO 添加日志记录，等级为info
            return token

        except TeaException as warn:
            # TODO 添加日志记录，等级为warn
            # TODO 添加警告弹窗
            print(warn.message)
            sys.exit(1)

if __name__ == '__main__':
    client = Authenticator()
    token = client.getToken()
    print(token)
