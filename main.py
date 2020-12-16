import http.client
import json
import time
import pymongo


class Arknights:

    def __init__(self):
        self.myClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.arknights = self.myClient["arknights"]

    def insert_db(self):
        data = self.arknights["data"]
        history = self.get_data()
        for x in history:
            x["_id"] = x['ts']
            timeStamp = x['ts']
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime("%Y年%m月%d日 %H:%M:%S", timeArray)
            x['date'] = otherStyleTime
            query = {'_id': x['ts']}
            x.pop('ts')
            data.update_one(query, {'$set': x}, upsert=True)

    # def query_db(self):
    #     data = self.arknights["data"]
    #     # count = data.find({"chars.rarity": 2}, {"_id": 0, "date": 1, "chars": 1}).count()
    #     # print(count)
    #     for x in data.find():
    #         print(x)
    #
    #     # 稀有度 2:三星 3:4星 4:五星 5:六星
    #     # for x in data.find({"chars.rarity": 4}, {'_id': 0}):
    #     #     print(x)

    def get_data(self):
        cookie = '6dsBljPsKbKNkyA0dAe89fOapsdLZsDC23cG_4qdKjhQsQX9oUgkwFRbSes6mZR3TWMDnGrT0ll-dQzrTpuWIYpr2w_KeoqN3zmNlcvgjFD6Fld-HB8RMsAiDo6S5Q-SOhPjlfAVEc0vsoo5adwq4m474nRgzm4CprRAc4oJ6fRUd9spz_SiYXt0XEpnnvdaGJ9lGs5PVpthKNFPDGUi97YaoFXGcHOEn_M6pcyRP9-H_oQ-TEJ0AhXImW0EB_BCz_hOUBSDWT9o5G-jhF9xOsGSYvmDWN5MJWl8c80dmP8='
        conn = http.client.HTTPSConnection("ak.hypergryph.com")
        payload = ''
        headers = {
            'cookie':
                      # '_uab_collina=160706731608821027475838;'
                      # ' csrf_token=gSNWi-EQuxuxEoq6DarFeJL6;'
                      # ' _ga=GA1.2.145414709.1607067316;'
                      # ' _gid=GA1.2.180588982.1607067316;'
                      # ' acw_tc=77a7dc1716070769369115079ea7de0f63776c75bf8ed2df0ece221235;'
                      ' HG_ACCOUNT='+cookie+';'
                      # ' _gat=1;'
                      # ' u_asec=099%23KAFEmYEKEc5EhGTLEEEEEpEQz0yFZ6VTSXyoG6zcSXvqW6VJSrw7Z6V1D3QTEEjtBKlVjYFET%2FdEsyaStcYTEHIwZbqEjOT2qHGbkfMs%2BwD4kLJqmCXdpwIb06Mqm%2FN4kLjoxYPVWwISqwERvkxd0xEGctgMXREYqLzakjDuzZdY0He6ma2GkL0opQgyy%2FoboaSaAYFExGExbvedCwUQrjDt9yBXHaxdcEPcbdhdcw7B%2BUZVNOeVbLNtay%2FoPwoScblczVZBNs1D3oCPnyIVba47aOCxbyXZNGucbocB6RXZ1uQTEEMFluula3PoE7EIlllbCP8MreabE7EUlllPeliSlllllulJt37IJ9llWLaStEaollle33iS13slluUdt37InNQTEE7EERpCDEFET3llsR4%3D'
        }
        history = []
        for i in range(1, 4):
            conn.request("GET", "/user/api/inquiry/gacha?page=" + str(i), payload, headers)
            res = conn.getresponse()
            data = json.loads(res.read().decode("utf-8"))
            for s in data['data']['list']:
                history.append(s)
        return history


# 新增
if __name__ == '__main__':
    Arknights().insert_db()
# 查询
# if __name__ == '__main__':
#     Arknights().query_db()
