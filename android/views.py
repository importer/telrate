import string

from android.models import Useraccount, GoodsInfo, Accounts
from django.http import HttpResponse
from decimal import Decimal
from django.contrib.auth.decorators import login_required

from django.contrib import auth
import json


def login(request):
    try:
        if request.method == 'POST':
            req = json.loads(request.body)
            username = req['tbUserAccount']
            password = req['tbUserPwd']
            device = req['device']
            phone = req['auto']
        # game_id1 = datas[0]['game_id']
    except Exception as e:
        print(e)
        resp = {'msg': '网络错误'
            , 'userID': 0000
            , 'error': 400}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    if username == "xxxx" and password == 'xxxx' and phone is not None:
        puser, created = Useraccount.objects.get_or_create(
            phone=phone,
            device=device,
            defaults={'username': device, 'password': password},
        )
        #   puser=Useraccount.objects.filter(phone=phone,device=device).all()[0]
        #   if puser is None:
        #   	user = Useraccount.objects.create_user(username=device, password=password, phone=phone, device=device)
        # user.save()
        auth.login(request, puser)
        resp = {'msg': '登录成功',
                'userID': puser.id,
                'error': 200}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        resp = {'msg': '登录成功',
                'userID': user.id,
                'error': 200}
    else:
        resp = {'msg': '登录失败',
                'userID': user.id,
                'error': 300}
    return HttpResponse(json.dumps(resp), content_type="application/json")


# 200:成功
# 300:失败
# 400:异常


def sign(request):
    try:
        if request.method == 'POST':
            req = json.loads(request.body)
            device = req.get('tbImei', '')
            username = req.get('tbUserAccount', device)
            password = req.get('tbUserPwd', '')
        # game_id1 = datas[0]['game_id']
    except Exception as e:
        print(e)
        resp = {'error': 400,
                'hongbao': 25,
                'msg': '网络错误',
                'net': 2,
                'pd': 100,
                'rmb': 1000,
                'sessionid': 5678,
                'userID': 1234
                }
        return HttpResponse(json.dumps(resp), content_type="application/json")
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user:
        resp = {'error': 300,
                'hongbao': 25,
                'msg': '已注册',
                'net': 2,
                'pd': 100,
                'rmb': 1000,
                'sessionid': 5678,
                'userID': user.id
                }
        return HttpResponse(json.dumps(resp), content_type="application/json")
    # 添加到数据库（还可以加一些字段的处理）
    user = Useraccount.objects.create_user(username=username, password=password, device=device)
    user.save()
    resp = {'error': 200,
            'hongbao': 25,
            'msg': '注册成功',
            'net': 2,
            'pd': 100,
            'rmb': 1000,
            'sessionid': 5678,
            'userID': 1234
            }
    return HttpResponse(json.dumps(resp), content_type="application/json")


def logout(request):
    auth.logout(request)
    return HttpResponse("退出成功")


def getdou(request):
    req = json.loads(request.body)
    print(req)
    userid = req.get('sessionid', '')
    userG = req.get('userG', 0)
    user_id = Useraccount.objects.get(id=userid)
    acct_user, created = Accounts.objects.get_or_create(use_id=userid,
                                                        defaults={'Coin': 1000, 'amount': 0, 'use_id': user_id}
                                                        )
    if userG > 0:
        coins = acct_user.Coin
        amount = acct_user.amount
        print(Decimal(userG))
        if acct_user and coins >= Decimal(userG):
            acct_user.Coin = coins - Decimal(userG)
            acct_user.amount = amount + Decimal(userG) * 10
            acct_user.save()
            resp = {'userG': str(Decimal(acct_user.Coin).quantize(Decimal('0.0'))),
                    'sessionid': "12345678",
                    'msg': '兑换成功'
                    }
        else:
            resp = {'userG': str(Decimal(acct_user.Coin).quantize(Decimal('0.0'))),
                    'sessionid': "12345678",
                    'msg': '豆豆不足'
                    }
    else:
        resp = {'userG': str(Decimal(acct_user.Coin).quantize(Decimal('0.0'))),
                'sessionid': "12345678",
                'msg': '获取豆豆成功'
                }
    return HttpResponse(json.dumps(resp), content_type="application/json")


def saveinfo(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        device = req.get('tbImei', '')
        username = req.get('tbUserAccount', device)
        password = req.get('userPwd', "")
        userPwdRe = req.get('userPwdRe', "")
    resp = {'error': 200, 'msg': 'succeed!!'}
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def cookiestest(request):
    resp = {'userG': 123456,
            'sessionid': "12345678",
            'msg': '获取豆豆成功'
            }
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def getcell(request):
    resp = {'error': 200, 'msg': '成功获取Q币信息',
            'list': [
                {'net': 12, 'pid': '1', 'price': 10},
                {'net': 13, 'pid': '2', 'price': 20},
                {'net': 14, 'pid': '3', 'price': 40},
                {'net': 15, 'pid': '4', 'price': 50},
            ]
            }
    return HttpResponse(json.dumps(resp), content_type="application/json")


# {"userCell":"1229323202","sessionid":"","pid":"1","netType":1,"netNum":12}

@login_required
def duicell(request):
    try:
        if request.method == 'POST':
            req = json.loads(request.body)
            userCell = req['userCell']
            sessionid = req['sessionid']
            pid = req['pid']
            netType = req['netType']
            netNum = req['netNum']
            user = request.user
    except Exception as e:
        print(e)
        resp = {'msg': '网络错误'
            , 'userID': 0000
            , 'error': 400}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    resp = {'msg': '充值成功:%sM' % netNum,
            'error': 200}
    print(user)
    return HttpResponse(json.dumps(resp), content_type="application/json")
