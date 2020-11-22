# lx-step
【Python】腾讯云云函数配合乐心健康刷QQ、微信、支付宝步数(支持随机步数、微信QQ推送)

# 说在前面
已经解决步数数据不同步第三方应用问题，感谢吾爱破解[xwj1612](https://www.52pojie.cn/?1113315),感谢项目[https://github.com/BBboy01/ChangeStype](https://github.com/BBboy01/ChangeStype)

# 测试截图
![QQ截图20201030125740.png](https://i.loli.net/2020/10/30/HyoYs8MNnu9gQjI.png)
![Screenshot_20201030_125105_com.eg.android.AlipayG.jpg](https://i.loli.net/2020/10/30/ODLjcw3FEpy6ZvK.jpg)

# 方法
1. 下载乐心健康APP：官方下载地址：http://www.lifesense.com/app/
2. 从应用商店下载乐心健康App，打开软件并选择手机号登录
3. 登录之后，点击我的->设置->账号与安全->设置密码(修改密码)，设置你自己记得住的密码
4. 回到App首页，点击我的->数据共享，绑定你想同步数据的项目注：同步微信运动请按照要求关注【乐心运动】公众号。
5. 回到云函数代码，配置好下图参数，运行即可提交步数即可同步至你绑定的所有平台
![1](https://attach.52pojie.cn/forum/202009/26/220610s1ehd59u55uh5uce.png)
6. 设置好云函数触发规则

# 其他
[https://www.52pojie.cn/thread-1274977-1-1.html](https://www.52pojie.cn/thread-1274977-1-1.html)
