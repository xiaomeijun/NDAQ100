#获取纳斯达克100指数钉钉发送到群消息
import requests
import yfinance as yf
from datetime import datetime

# 设置纳斯达克100指数的代码
nasdaq_symbol = '^NDX'

try:
    # 使用yfinance获取数据
    nasdaq_data = yf.Ticker(nasdaq_symbol)

    # 获取当天的数据
    today_data = nasdaq_data.history(period="1d")

    # 获取收盘价
    close_price = today_data['Close'].iloc[0]

    # 获取当前日期
    current_date = datetime.now().strftime('%Y-%m-%d')

    # 准备要发送的消息内容，增加了 'nsdk' 关键词和日期
    message = f"{current_date} nsdk: {close_price:.2f} "

    # 钉钉自定义机器人的Webhook URL（请替换为你的Webhook URL）
    webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=291f7177edfd07f9293522f2d9359184c72135488e2f9b876a2b058b94c3eeba"

    # 准备发送的消息体
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }

    # 发送请求
    response = requests.post(webhook_url, json=data, headers=headers)
    
    # 打印响应内容
    print(response.json())

except Exception as e:
    print(f"发生错误: {e}")
