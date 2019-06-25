import requests

import dns.resolver



res = requests.get('https://www.ygdy8.com/')

from dns import resolver

ans = resolver.query("'https://www.ygdy8.com/", "A")
print("qname:",ans.qname)
print ("reclass:",ans.rdclass)
print ("rdtype:",ans.rdtype)
print ("rrset:",ans.rrset)
print ("response:",ans.response)


# dns 服务器信息








# print(res)

