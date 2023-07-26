from woocommerce import API
import json

wcapi = API(
    url="http://localhost:8888/mysite1/",
    consumer_key="ck_8e8ae1e5992cc2ccdd3ca276279b21b3e18fcda8",
    consumer_secret="cs_88d97b24beaa2fc723b40bcb592606d79bad80c8",
    version="wc/v3",
    timeout=15
)

# rs = wcapi.get("products")

payload = {"per_page": 90}
rs = wcapi.get("coupons", params=payload)
body = rs.json()
breakpoint()