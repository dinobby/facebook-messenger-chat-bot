import requests
from bs4 import BeautifulSoup as bs
from transitions.extensions import GraphMachine
from utils import send_text_message

path = ['綠幹線','綠1','綠2','綠3','綠4','綠5','綠6','綠7','綠10','綠11','綠12','綠13','綠14','綠15','綠16','綠17','綠20','綠20-1','綠21','綠22','綠23','綠24','綠25','綠26','綠27',
        '藍幹線','藍1','藍2','藍3','藍10','藍11','藍12','藍13','藍20','藍21','藍22','藍23','藍24','藍25',
        '棕幹線','棕1','棕2','棕3','棕3-1','棕10','棕11',
        '橘幹線','橘1','橘2','橘3','橘4','橘4-1','橘5','橘10','橘10-1','橘11','橘12','橘20',
        '黃幹線','黃1','黃2','黃3','黃4','黃5','黃6','黃6-1','黃7','黃9','黃10','黃10-1','黃11','黃11-1','黃11-2','黃12','黃12-2','黃13','黃14','黃14-1','黃15','黃16','黃20',
        '紅幹線','紅1','紅2','紅3','紅3-1','紅4','紅10','紅11','紅12','紅13','紅14']

ids = [1100,1101,1102,1103,1104,1105,1106,1107,1110,1111,1112,1113,1114,1115,1116,1117,1120,1804,1121,1122,1123,1124,1125,1126,1127,
       1200,1201,1202,1203,1210,1211,1212,1213,1220,1221,1222,1223,1224,1225,
       1300, 1301, 1302, 1303, 1810, 1310, 1311,
       1400,1401,1402,1403,1404,1808,1405,1410,1807,1411,1412,1420,
       1500,1501,1502,1503,1504,1505,1506,1802,1507,1509,1510,1812,1511,1809,1813,1512,1805,1513,1514,1806,1515,1516,1520,
       1600,1601,1602,1603,1801,1604,1610,1611,1612,1613,1614]

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '開始使用'
        return False

    def state1_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '1'
        return False

    def state1_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '2'
        return False

    def state1_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '3'
        return False

    def state2_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return len(text) > 0 and self.state == 'state2'

    def state5_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '返回'

    def state3_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return len(text) > 0 and self.state == 'state3'

    def state6_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '返回'

    def on_enter_state1(self, event):
        print("I'm entering state1")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "歡迎使用「沒有機車沒關係我來幫你找公車」！\n輸入「1」查詢公車到站時間\n輸入「2」查詢公車票價\n輸入「3」查詢公車優惠說明")
        #self.go_back()

    # def on_exit_state1(self):
    #     print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入您想要查詢的路線以及去/返程，例如：綠1 去 / 橘4-1 返 / 紅13 去...等，路線名稱與去返程中間以空格隔開")
        #self.go_back()

    # def on_exit_state2(self):
    #     print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "輸入路線及起訖站來查詢票價，例如：綠1 新化站 國泰大樓，路線與起訖站中間以空格隔開")
        #self.go_back()

    # def on_exit_state3(self):
    #     print('Leaving state3')

    def on_enter_state4(self, event):
        print("I'm entering state4")
        s = '⭐市民卡1日9元搭到飽\n\
                台南市民持市民卡搭乘市區公車（0~99路，33路除外），\
                並且上、下車都刷市民卡，第1段半價（9元），當日第2段起免費！💖\
                （下車未刷卡時，當日搭乘下一段次仍維持半價9元計費）\n\
                \n\
                ⭐幹支線公車8公里免費\n\
                持電子票證（市民卡、一卡通、悠遊卡、iCash 2.0）\
                搭乘幹支線公車（綠、藍、棕、橘、黃、紅），並且上、下車都刷卡，享前8公里免費！💖\
                \n\
                ⭐轉乘優惠加碼為4小時\n\
                持電子票證（市民卡、一卡通、悠遊卡、iCash 2.0）\
                搭乘台鐵及大台南公車，並且上、下車都刷卡，\
                4小時內轉乘市區公車1段票免費、轉乘幹支線公車8公里免費再折扣9元！💖\n\
                \n\
                ⚡特別提醒⚡\n\
                學生證就是市民卡：本市高中職以下學生，刷學生證即享優惠。\
                設籍臺南市民眾，可攜帶身分證至臺南市37區公所申辦市民卡一般卡，每張新臺幣100元。\
                107年9月1日開放iCash 2.0，9月底前每趟加贈OPENPOINT 300點，歡迎多加利用👍\n\
                \n\
                ※實施期間：自107年8月1日起至107年12月31日止。'
        sender_id = event['sender']['id']
        send_text_message(sender_id, s)
        self.go_back()

    def on_enter_state5(self, event):
        global path, ids
        query_path = 0
        sender_id = event['sender']['id']
        if sender_id != '312249102747382':
            if event.get("message"):
                if event.get("message") == '返回':
                    self.go_back()
                else:
                    l = event['message']['text'].split(" ")
            if len(l) == 2:
                query_path = l[0]
                if l[1] == '去':
                    goback = 0
                elif l[1] == '返':
                    goback = 1
                else:
                    goback = 0

            try:
                id = ids[path.index(query_path)]
                url = 'http://2384.tainan.gov.tw/NewTNBusAPI_V2/API/GoAndBackWithTimeV1.ashx?id={0}&goback={1}&Lang=cht'.format(id,goback)
                res = requests.get(url)
                d = res.json()
                s = ''
                for i in d:
                    if i['Time'] == '末班已駛離':
                        s+=('離{0}站，末班已駛離').format(i['StopName']) + '\n'
                    else:
                        s+=('離{0}站，還有{1}分鐘'.format(i['StopName'],i['Time'])) + '\n'
                send_text_message(sender_id, s)
            except ValueError:
                send_text_message(sender_id, "對不起，您輸入的路線不存在")

    def on_enter_state6(self, event):
        global path, ids
        query_path = 0
        query_start = ''
        query_end = ''
        sender_id = event['sender']['id']
        if sender_id != '312249102747382':
            if event.get("message"):
                if event.get("message") == '返回':
                    self.go_back()
                else:
                    l = event['message']['text'].split(" ")
                
            if len(l) == 3:
                query_path = l[0]
                query_start = l[1]
                query_end = l[2]
            try:
                id = ids[path.index(query_path)]
                url = 'http://2384.tainan.gov.tw/NewTNBusAPI_V2/API/FareV1.ashx?pathid={0}&sname={1}&ename={2}'.format(id, query_start, query_end)
                res = requests.get(url)
                d = res.json()

                s = '現金全票：' + d['fareCash'] + '元\n' + \
                '現金半票：' + d['fareCashHalf'] + '元\n' + \
                '電子票卡全票：' + d['fareIc'] + '元\n' + \
                '電子票卡半票：' + d['fareIcHalf'] + '元'

                send_text_message(sender_id, s)
            except ValueError:
                send_text_message(sender_id, "對不起，您輸入的路線或起訖站不存在")
    # def on_exit_state3(self):
    #     print('Leaving state4') 