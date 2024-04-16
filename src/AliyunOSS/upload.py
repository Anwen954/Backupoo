"""
_*_ coding   :    utf-8 _*_
@ File       :    upload.py
@ Time       :    2024/04/12 18:46:31
@ Author     :    Farmer&Architect
@ Email      :    18797671241@163.com
@ Version    :    1.0
@ Description:    上传文件
"""

import oss2

from authentication import Authenticator

class Bucket(oss2.Bucket):
    def __init__(self):

        # 获取Token，并进行认证
        token = Authenticator.getToken()
        auth = oss2.StsAuth(token.access_key_id, token.access_key_secret, token.security_token, 'v4')
        # 创建Bucket对象
        super(Bucket, self).__init__(auth=auth,
                                     bucket_name='guangzhan2',
                                     endpoint='https://oss-cn-guangzhou.aliyuncs.com',
                                     region='cn-guangzhou')

if __name__ == '__main__':
    bucket = Bucket()
    bucket.put_object('motto.txt','Never give up. - Jack Ma')
    bucket.get_object_to_file('motto.txt', '马言.txt')
