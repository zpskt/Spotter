# alert/sms_notifier.py

from aliyunsdkcore.client import AcsClient
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
import json
import yaml
from pathlib import Path


class SMSNotifier:
    def __init__(self, config_path=None):
        """
        初始化阿里云短信客户端
        :param config_path: 短信配置文件路径，默认为 config/sms_config.yaml
        """
        config_path = config_path or Path(__file__).parent.parent / "config" / "sms_config.yaml"

        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

        self.provider = self.config.get('provider')

        if self.provider != 'aliyun':
            raise ValueError("当前仅支持阿里云短信服务")

        credentials = self.config['credentials']
        region = 'cn-hangzhou'  # 阿里云短信服务默认区域

        self.client = AcsClient(
            access_key_id=credentials['access_key_id'],
            access_secret=credentials['access_key_secret'],
            region_id=region
        )

    def send_alert(self, message: str):
        """
        发送短信告警
        :param message: 要发送的短信内容
        :return: API 响应结果
        """
        sms_config = self.config['sms']
        sign_name = sms_config['sign_name']
        template_code = sms_config['template_code']
        recipients = sms_config['recipients']

        success_count = 0
        for phone in recipients:
            request = SendSmsRequest.SendSmsRequest()
            request.set_PhoneNumbers(phone)
            request.set_SignName(sign_name)
            request.set_TemplateCode(template_code)

            # 根据模板设置参数，这里假设模板中有一个变量叫 "content"
            request.set_TemplateParam(json.dumps({"content": message}))

            try:
                response = self.client.do_action_with_exception(request)
                response_json = json.loads(response.decode('utf-8'))
                if response_json.get('Code') == 'OK':
                    print(f"[INFO] 短信发送成功至 {phone}")
                    success_count += 1
                else:
                    print(f"[ERROR] 短信发送失败至 {phone}: {response_json.get('Message')}")
            except Exception as e:
                print(f"[ERROR] 发送短信异常至 {phone}: {str(e)}")

        return {
            "total": len(recipients),
            "success": success_count,
            "failed": len(recipients) - success_count
        }
