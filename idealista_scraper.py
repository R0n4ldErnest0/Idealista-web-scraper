import time
import requests
import json
from selectolax.parser import HTMLParser
import csv
import random

#Web Scraper for recent barcelona houses of the web page idealista.com
#First we get all the ids of the house through the obtention of the html with the list of houses
#Then,once we have the house_ids,we extract the html of each house_id page,then proceed to extract the desired info.



def get_house_html(house_id:str):

    cookies = {
        '_pprv': 'eyJjb25zZW50Ijp7IjAiOnsibW9kZSI6Im9wdC1pbiJ9LCIxIjp7Im1vZGUiOiJvcHQtaW4ifSwiMiI6eyJtb2RlIjoib3B0LWluIn0sIjMiOnsibW9kZSI6Im9wdC1pbiJ9LCI0Ijp7Im1vZGUiOiJvcHQtaW4ifSwiNSI6eyJtb2RlIjoib3B0LWluIn0sIjYiOnsibW9kZSI6Im9wdC1pbiJ9LCI3Ijp7Im1vZGUiOiJvcHQtaW4ifX0sInB1cnBvc2VzIjpudWxsLCJfdCI6Im1odjE0enk1fG0yNm03aW01In0%3D',
        '_pcid': '%7B%22browserId%22%3A%22m26m7ilzfx0t8kb1%22%2C%22_t%22%3A%22mhv150dq%7Cm26m7j1q%22%7D',
        '_pctx': '%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbABYA3AIwBWAAysIAH34AmAGz8A7ACtR8AL5A',
        '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D',
        '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22yd6nbNJJyBPrMd4wP0Mg%22%7D',
        'didomi_token': 'eyJ1c2VyX2lkIjoiMTkyODI3MGEtNDkxOS02OWFkLWE1NGEtNDRmODY3NGUzMTg3IiwiY3JlYXRlZCI6IjIwMjQtMTAtMTJUMjA6MzQ6MzMuMjMzWiIsInVwZGF0ZWQiOiIyMDI0LTEwLTEyVDIwOjM0OjM2LjU4MVoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpsaW5rZWRpbi1tYXJrZXRpbmctc29sdXRpb25zIiwiYzptaXhwYW5lbCIsImM6YWJ0YXN0eS1MTGtFQ0NqOCIsImM6aG90amFyIiwiYzpiZWFtZXItSDd0cjdIaXgiLCJjOnRlYWxpdW1jby1EVkRDZDhaUCIsImM6dGlrdG9rLUtaQVVRTFo5IiwiYzpnb29nbGVhbmEtNFRYbkppZ1IiLCJjOmlkZWFsaXN0YS1MenRCZXFFMyIsImM6aWRlYWxpc3RhLWZlUkVqZTJjIiwiYzpjb250ZW50c3F1YXJlIiwiYzptaWNyb3NvZnQiXX0sInB1cnBvc2VzIjp7ImVuYWJsZWQiOlsiZ2VvbG9jYXRpb25fZGF0YSIsImRldmljZV9jaGFyYWN0ZXJpc3RpY3MiXX0sInZlcnNpb24iOjIsImFjIjoiQ2hHQUVBRmtGQ0lBLkFBQUEifQ==',
        'euconsent-v2': 'CQGYVgAQGYVgAAHABBENBKFsAP_gAAAAAAAAHXwBwAIAAqABaAFsAUgC8wHXgAAAFJQAYAAgqEUgAwABBUIhABgACCoQ6ADAAEFQgkAGAAIKhAAA.f_wAAAAAAAAA',
        '_hjSessionUser_250321': 'eyJpZCI6IjEyMGI3Njk2LTI4NDUtNWI3OC1iZTVhLWExYTg4YzY2NDkzMSIsImNyZWF0ZWQiOjE3Mjg3NjUyNzcxNjYsImV4aXN0aW5nIjp0cnVlfQ==',
        '_tt_enable_cookie': '1',
        '_ttp': 'u4Rbpu_5llkAz5MAJaKjddMg4Ch',
        '_fbp': 'fb.1.1728765335251.485214494580389561',
        '_gcl_au': '1.1.2098306035.1728766111',
        'askToSaveAlertPopUp': 'false',
        'smc': '"{}"',
        'userUUID': 'e3e83fa8-88fa-4079-9a74-41d9bbbb5856',
        'SESSION': 'f210a8a454e0afe2~856c91c1-749f-402d-ac58-f1de590ea353',
        'utag_main__sn': '3',
        'utag_main_ses_id': '1728799614862%3Bexp-session',
        'utag_main__prevVtUrlReferrer': '%3Bexp-1728803215033',
        'utag_main__prevVtUrl': 'https%3A%2F%2Fwww.idealista.com%2F%3Bexp-1728803215033',
        'utag_main__prevVtSource': 'Direct traffic%3Bexp-1728803215033',
        'utag_main__prevVtCampaignName': 'organicWeb%3Bexp-1728803215033',
        'utag_main__prevVtCampaignCode': '%3Bexp-1728803215033',
        'utag_main__prevVtCampaignLinkName': '%3Bexp-1728803215033',
        'utag_main__prevVtRecipientId': '%3Bexp-1728803215033',
        'utag_main__prevVtProvider': '%3Bexp-1728803215033',
        'utag_main__ss': '0%3Bexp-session',
        '_hjSession_250321': 'eyJpZCI6ImQ4Y2MwZjJhLWEzNGItNGMwNC04ZjdlLTE5ZjFjYTc4ZWViMCIsImMiOjE3Mjg3OTk2MTYzNjcsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
        '_hjHasCachedUserAttributes': 'true',
        '_clck': '7jvrnx%7C2%7Cfpz%7C0%7C1746',
        'utag_main__prevCompleteClickName': '',
        'contact856c91c1-749f-402d-ac58-f1de590ea353': '"{\'maxNumberContactsAllow\':10}"',
        '_last_search': 'officialZone',
        'dicbo_id': '%7B%22dicbo_fetch%22%3A1728800263573%7D',
        'cookieSearch-1': '"/venta-viviendas/barcelona-barcelona/:1728800340814"',
        'utag_main__pn': '49%3Bexp-session',
        'utag_main__se': '68%3Bexp-session',
        'utag_main__st': '1728802142108%3Bexp-session',
        'utag_main__prevCompletePageName': '254-idealista/404 > portal > viewResults%3Bexp-1728803942322',
        'utag_main__prevLevel2': '254-idealista/404%3Bexp-1728803942322',
        'ABTastySession': 'mrasn=&lp=https%253A%252F%252Fwww.idealista.com%252F',
        'ABTasty': 'uid=nbnztztfp0y1jsng&fst=1728765277130&pst=1728772897148&cst=1728799615015&ns=4&pvt=69&pvis=41&th=',
        '_uetsid': '6600550088d911ef8ebe0fbe5b27a85b',
        '_uetvid': '66008bb088d911efbc2653cadf889408',
        'cto_bundle': 'i6MdUV9nZEFMNFpMSVkzWUVPRFJmUWQ2JTJGYndwUUxiQnpNMkVneHd0ZXB4d1BTNUNRY2hpOFBhZFJnajRsWWVFTGh6aVVZZnR3MkxIWVB2bU9XVklJekthajVEVGNvb2VzcEJRRlNKTVZsWkgzTG1OdmZTRmVvblB3YXN1MzJNRU12UHphNk9XJTJCYnBDJTJCdE8xS0RlSmJDZ3FSYkZMU3JicWxLT3BPQ3BRYkR0WTNRbXM2SDB2cFZ0SEtqWFdCSVNqWUJMUXN3UVo1aHdvaWdPMnJnJTJCYWJGUXBob2Q3dVZhUm90JTJGUUhyQ0x0YzFtbWRuU0FVa1pmUUN1OWNvRyUyRiUyQiUyQkN6VWxOUzcwcE4xZ21vJTJGYm5VeE1EODRpdnFkZyUzRCUzRA',
        '_clsk': 's8ng70%7C1728800343544%7C50%7C0%7Cb.clarity.ms%2Fcollect',
        'datadome': '2qLle4I5SwFr7HNat0jvfmzRWHrXsJz6Hx3kURPKjxPqSrLy4Hj69DuL~oOpAoE5NmTjIhCkTcNY~p9Dq0Oxq6WSMQm6EvCbMYAqzv6TD1QtfYpHrpBIwfam~D6KpPi5',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'es-ES,es;q=0.9',
        # 'cookie': '_pprv=eyJjb25zZW50Ijp7IjAiOnsibW9kZSI6Im9wdC1pbiJ9LCIxIjp7Im1vZGUiOiJvcHQtaW4ifSwiMiI6eyJtb2RlIjoib3B0LWluIn0sIjMiOnsibW9kZSI6Im9wdC1pbiJ9LCI0Ijp7Im1vZGUiOiJvcHQtaW4ifSwiNSI6eyJtb2RlIjoib3B0LWluIn0sIjYiOnsibW9kZSI6Im9wdC1pbiJ9LCI3Ijp7Im1vZGUiOiJvcHQtaW4ifX0sInB1cnBvc2VzIjpudWxsLCJfdCI6Im1odjE0enk1fG0yNm03aW01In0%3D; _pcid=%7B%22browserId%22%3A%22m26m7ilzfx0t8kb1%22%2C%22_t%22%3A%22mhv150dq%7Cm26m7j1q%22%7D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbABYA3AIwBWAAysIAH34AmAGz8A7ACtR8AL5A; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22yd6nbNJJyBPrMd4wP0Mg%22%7D; didomi_token=eyJ1c2VyX2lkIjoiMTkyODI3MGEtNDkxOS02OWFkLWE1NGEtNDRmODY3NGUzMTg3IiwiY3JlYXRlZCI6IjIwMjQtMTAtMTJUMjA6MzQ6MzMuMjMzWiIsInVwZGF0ZWQiOiIyMDI0LTEwLTEyVDIwOjM0OjM2LjU4MVoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpsaW5rZWRpbi1tYXJrZXRpbmctc29sdXRpb25zIiwiYzptaXhwYW5lbCIsImM6YWJ0YXN0eS1MTGtFQ0NqOCIsImM6aG90amFyIiwiYzpiZWFtZXItSDd0cjdIaXgiLCJjOnRlYWxpdW1jby1EVkRDZDhaUCIsImM6dGlrdG9rLUtaQVVRTFo5IiwiYzpnb29nbGVhbmEtNFRYbkppZ1IiLCJjOmlkZWFsaXN0YS1MenRCZXFFMyIsImM6aWRlYWxpc3RhLWZlUkVqZTJjIiwiYzpjb250ZW50c3F1YXJlIiwiYzptaWNyb3NvZnQiXX0sInB1cnBvc2VzIjp7ImVuYWJsZWQiOlsiZ2VvbG9jYXRpb25fZGF0YSIsImRldmljZV9jaGFyYWN0ZXJpc3RpY3MiXX0sInZlcnNpb24iOjIsImFjIjoiQ2hHQUVBRmtGQ0lBLkFBQUEifQ==; euconsent-v2=CQGYVgAQGYVgAAHABBENBKFsAP_gAAAAAAAAHXwBwAIAAqABaAFsAUgC8wHXgAAAFJQAYAAgqEUgAwABBUIhABgACCoQ6ADAAEFQgkAGAAIKhAAA.f_wAAAAAAAAA; _hjSessionUser_250321=eyJpZCI6IjEyMGI3Njk2LTI4NDUtNWI3OC1iZTVhLWExYTg4YzY2NDkzMSIsImNyZWF0ZWQiOjE3Mjg3NjUyNzcxNjYsImV4aXN0aW5nIjp0cnVlfQ==; _tt_enable_cookie=1; _ttp=u4Rbpu_5llkAz5MAJaKjddMg4Ch; _fbp=fb.1.1728765335251.485214494580389561; _gcl_au=1.1.2098306035.1728766111; askToSaveAlertPopUp=false; smc="{}"; userUUID=e3e83fa8-88fa-4079-9a74-41d9bbbb5856; SESSION=f210a8a454e0afe2~856c91c1-749f-402d-ac58-f1de590ea353; utag_main__sn=3; utag_main_ses_id=1728799614862%3Bexp-session; utag_main__prevVtUrlReferrer=%3Bexp-1728803215033; utag_main__prevVtUrl=https%3A%2F%2Fwww.idealista.com%2F%3Bexp-1728803215033; utag_main__prevVtSource=Direct traffic%3Bexp-1728803215033; utag_main__prevVtCampaignName=organicWeb%3Bexp-1728803215033; utag_main__prevVtCampaignCode=%3Bexp-1728803215033; utag_main__prevVtCampaignLinkName=%3Bexp-1728803215033; utag_main__prevVtRecipientId=%3Bexp-1728803215033; utag_main__prevVtProvider=%3Bexp-1728803215033; utag_main__ss=0%3Bexp-session; _hjSession_250321=eyJpZCI6ImQ4Y2MwZjJhLWEzNGItNGMwNC04ZjdlLTE5ZjFjYTc4ZWViMCIsImMiOjE3Mjg3OTk2MTYzNjcsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; _clck=7jvrnx%7C2%7Cfpz%7C0%7C1746; utag_main__prevCompleteClickName=; contact856c91c1-749f-402d-ac58-f1de590ea353="{\'maxNumberContactsAllow\':10}"; _last_search=officialZone; dicbo_id=%7B%22dicbo_fetch%22%3A1728800263573%7D; cookieSearch-1="/venta-viviendas/barcelona-barcelona/:1728800340814"; utag_main__pn=49%3Bexp-session; utag_main__se=68%3Bexp-session; utag_main__st=1728802142108%3Bexp-session; utag_main__prevCompletePageName=254-idealista/404 > portal > viewResults%3Bexp-1728803942322; utag_main__prevLevel2=254-idealista/404%3Bexp-1728803942322; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.idealista.com%252F; ABTasty=uid=nbnztztfp0y1jsng&fst=1728765277130&pst=1728772897148&cst=1728799615015&ns=4&pvt=69&pvis=41&th=; _uetsid=6600550088d911ef8ebe0fbe5b27a85b; _uetvid=66008bb088d911efbc2653cadf889408; cto_bundle=i6MdUV9nZEFMNFpMSVkzWUVPRFJmUWQ2JTJGYndwUUxiQnpNMkVneHd0ZXB4d1BTNUNRY2hpOFBhZFJnajRsWWVFTGh6aVVZZnR3MkxIWVB2bU9XVklJekthajVEVGNvb2VzcEJRRlNKTVZsWkgzTG1OdmZTRmVvblB3YXN1MzJNRU12UHphNk9XJTJCYnBDJTJCdE8xS0RlSmJDZ3FSYkZMU3JicWxLT3BPQ3BRYkR0WTNRbXM2SDB2cFZ0SEtqWFdCSVNqWUJMUXN3UVo1aHdvaWdPMnJnJTJCYWJGUXBob2Q3dVZhUm90JTJGUUhyQ0x0YzFtbWRuU0FVa1pmUUN1OWNvRyUyRiUyQiUyQkN6VWxOUzcwcE4xZ21vJTJGYm5VeE1EODRpdnFkZyUzRCUzRA; _clsk=s8ng70%7C1728800343544%7C50%7C0%7Cb.clarity.ms%2Fcollect; datadome=2qLle4I5SwFr7HNat0jvfmzRWHrXsJz6Hx3kURPKjxPqSrLy4Hj69DuL~oOpAoE5NmTjIhCkTcNY~p9Dq0Oxq6WSMQm6EvCbMYAqzv6TD1QtfYpHrpBIwfam~D6KpPi5',
        'priority': 'u=0, i',
        'referer': 'https://www.idealista.com/venta-viviendas/barcelona-barcelona/pagina-2100000900.htm?ordenado-por=fecha-publicacion-desc',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }
    #url="https://www.idealista.com/inmueble/106244192/"
    house_url=f"https://www.idealista.com/inmueble/{house_id}/"
    response = requests.get(house_url, cookies=cookies, headers=headers)
    print("Response status code: "+str(response.status_code))
    #print(response.text)
    return response.text
    house_html=HTMLParser(response.text)
    #with open('web_scraping_idealista_bclnhouses/pages.html', 'w',encoding="utf-8") as f:
    #    f.write(response.text)
    return house_html

def get_bcln_house_htmls(page_number:int=1):

    cookies = {
        'userUUID': '94ea1894-a0de-428f-803b-e48e46737188',
        'SESSION': 'fba8d6cc5f6e779c~0ea7b55f-7092-47c2-be35-783491be80c9',
        'utag_main__sn': '1',
        'utag_main_ses_id': '1728765273554%3Bexp-session',
        'utag_main__prevVtUrl': 'https%3A%2F%2Fwww.idealista.com%2F%3Bexp-1728768873728',
        'utag_main__prevVtUrlReferrer': '%3Bexp-1728768873728',
        'utag_main__prevVtSource': 'Direct traffic%3Bexp-1728768873728',
        'utag_main__prevVtCampaignName': 'organicWeb%3Bexp-1728768873728',
        'utag_main__prevVtCampaignCode': '%3Bexp-1728768873728',
        'utag_main__prevVtCampaignLinkName': '%3Bexp-1728768873728',
        'utag_main__prevVtRecipientId': '%3Bexp-1728768873728',
        'utag_main__prevVtProvider': '%3Bexp-1728768873728',
        '_pprv': 'eyJjb25zZW50Ijp7IjAiOnsibW9kZSI6Im9wdC1pbiJ9LCIxIjp7Im1vZGUiOiJvcHQtaW4ifSwiMiI6eyJtb2RlIjoib3B0LWluIn0sIjMiOnsibW9kZSI6Im9wdC1pbiJ9LCI0Ijp7Im1vZGUiOiJvcHQtaW4ifSwiNSI6eyJtb2RlIjoib3B0LWluIn0sIjYiOnsibW9kZSI6Im9wdC1pbiJ9LCI3Ijp7Im1vZGUiOiJvcHQtaW4ifX0sInB1cnBvc2VzIjpudWxsLCJfdCI6Im1odjE0enk1fG0yNm03aW01In0%3D',
        'utag_main__ss': '0%3Bexp-session',
        '_pcid': '%7B%22browserId%22%3A%22m26m7ilzfx0t8kb1%22%2C%22_t%22%3A%22mhv150dq%7Cm26m7j1q%22%7D',
        '_pctx': '%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbABYA3AIwBWAAysIAH34AmAGz8A7ACtR8AL5A',
        '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D',
        '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22yd6nbNJJyBPrMd4wP0Mg%22%7D',
        'didomi_token': 'eyJ1c2VyX2lkIjoiMTkyODI3MGEtNDkxOS02OWFkLWE1NGEtNDRmODY3NGUzMTg3IiwiY3JlYXRlZCI6IjIwMjQtMTAtMTJUMjA6MzQ6MzMuMjMzWiIsInVwZGF0ZWQiOiIyMDI0LTEwLTEyVDIwOjM0OjM2LjU4MVoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpsaW5rZWRpbi1tYXJrZXRpbmctc29sdXRpb25zIiwiYzptaXhwYW5lbCIsImM6YWJ0YXN0eS1MTGtFQ0NqOCIsImM6aG90amFyIiwiYzpiZWFtZXItSDd0cjdIaXgiLCJjOnRlYWxpdW1jby1EVkRDZDhaUCIsImM6dGlrdG9rLUtaQVVRTFo5IiwiYzpnb29nbGVhbmEtNFRYbkppZ1IiLCJjOmlkZWFsaXN0YS1MenRCZXFFMyIsImM6aWRlYWxpc3RhLWZlUkVqZTJjIiwiYzpjb250ZW50c3F1YXJlIiwiYzptaWNyb3NvZnQiXX0sInB1cnBvc2VzIjp7ImVuYWJsZWQiOlsiZ2VvbG9jYXRpb25fZGF0YSIsImRldmljZV9jaGFyYWN0ZXJpc3RpY3MiXX0sInZlcnNpb24iOjIsImFjIjoiQ2hHQUVBRmtGQ0lBLkFBQUEifQ==',
        'euconsent-v2': 'CQGYVgAQGYVgAAHABBENBKFsAP_gAAAAAAAAHXwBwAIAAqABaAFsAUgC8wHXgAAAFJQAYAAgqEUgAwABBUIhABgACCoQ6ADAAEFQgkAGAAIKhAAA.f_wAAAAAAAAA',
        '_hjSessionUser_250321': 'eyJpZCI6IjEyMGI3Njk2LTI4NDUtNWI3OC1iZTVhLWExYTg4YzY2NDkzMSIsImNyZWF0ZWQiOjE3Mjg3NjUyNzcxNjYsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjSession_250321': 'eyJpZCI6ImNiNDA3MTQ1LTAzN2EtNGQwYi05MmMxLWJkOTNlMjVkOWQ3MSIsImMiOjE3Mjg3NjUyNzcxNjcsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
        '_hjHasCachedUserAttributes': 'true',
        '_tt_enable_cookie': '1',
        '_ttp': 'u4Rbpu_5llkAz5MAJaKjddMg4Ch',
        '_clck': '7jvrnx%7C2%7Cfpy%7C0%7C1746',
        '_fbp': 'fb.1.1728765335251.485214494580389561',
        'contact0ea7b55f-7092-47c2-be35-783491be80c9': '"{\'maxNumberContactsAllow\':10}"',
        '_last_search': 'officialZone',
        '_gcl_au': '1.1.2098306035.1728766111',
        'send0ea7b55f-7092-47c2-be35-783491be80c9': '"{}"',
        'utag_main__prevCompleteClickName': '',
        'dicbo_id': '%7B%22dicbo_fetch%22%3A1728767878024%7D',
        'cookieSearch-1': '"/venta-viviendas/barcelona-barcelona/:1728767877503"',
        'askToSaveAlertPopUp': 'false',
        'utag_main__pn': '18%3Bexp-session',
        'utag_main__se': '36%3Bexp-session',
        'utag_main__st': '1728769728395%3Bexp-session',
        'utag_main__prevCompletePageName': '005-idealista/portal > portal > viewAdDetail%3Bexp-1728771528411',
        'utag_main__prevLevel2': '005-idealista/portal%3Bexp-1728771528411',
        'ABTastySession': 'mrasn=&lp=https%253A%252F%252Fwww.idealista.com%252F',
        'ABTasty': 'uid=nbnztztfp0y1jsng&fst=1728765277130&pst=-1&cst=1728765277130&ns=1&pvt=21&pvis=21&th=',
        '_uetsid': '6600550088d911ef8ebe0fbe5b27a85b',
        '_uetvid': '66008bb088d911efbc2653cadf889408',
        'cto_bundle': '8R_AhV9nZEFMNFpMSVkzWUVPRFJmUWQ2JTJGYjlXQXAyYldWb2x5S0lVY1VhNGNaSiUyRnkzdkw0Qm9hSjAyUDRFZDJPcFBEOVJTVHNvSmE4UmdtRnkySGdoJTJGdzNiMGhvd1llc2x5dldLS3pDeHZ1RmdWUkROdWpXZVltb00xRFU0YnowMTlsVklzYTY0bjBFUFVhRnglMkJKdzFOSk9yc1VIWiUyRlJZMSUyQlJDQXZrcEp6JTJGaTF4bVR5TGFIUzRGcXQyS0pHa2lzUmhXa2tjYmFGTmt3bHpCUU1JdnpHekVTdFdKa1hsV2J5MUtkQWFRaFU2a25PVklyMkdKNVdmMjclMkZoTlZWamhIWVloYnVoZzZVdFVPUmdRSnRQZ1BmMUJNSFElM0QlM0Q',
        '_clsk': '12yvnjf%7C1728767929728%7C23%7C0%7Cb.clarity.ms%2Fcollect',
        'datadome': '_g3QJiNDhA9C77csmlgZexrglZcCO2g22hY_uXd4a6oy6Sx2KIDef6Ry77T~rdUSukllhlVz__thfMtoZx1DJHJCD9d4jel24X0D__957ncOF11nTf_wm55xlqVGt6fj',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'es-ES,es;q=0.9',
        # 'cookie': 'userUUID=94ea1894-a0de-428f-803b-e48e46737188; SESSION=fba8d6cc5f6e779c~0ea7b55f-7092-47c2-be35-783491be80c9; utag_main__sn=1; utag_main_ses_id=1728765273554%3Bexp-session; utag_main__prevVtUrl=https%3A%2F%2Fwww.idealista.com%2F%3Bexp-1728768873728; utag_main__prevVtUrlReferrer=%3Bexp-1728768873728; utag_main__prevVtSource=Direct traffic%3Bexp-1728768873728; utag_main__prevVtCampaignName=organicWeb%3Bexp-1728768873728; utag_main__prevVtCampaignCode=%3Bexp-1728768873728; utag_main__prevVtCampaignLinkName=%3Bexp-1728768873728; utag_main__prevVtRecipientId=%3Bexp-1728768873728; utag_main__prevVtProvider=%3Bexp-1728768873728; _pprv=eyJjb25zZW50Ijp7IjAiOnsibW9kZSI6Im9wdC1pbiJ9LCIxIjp7Im1vZGUiOiJvcHQtaW4ifSwiMiI6eyJtb2RlIjoib3B0LWluIn0sIjMiOnsibW9kZSI6Im9wdC1pbiJ9LCI0Ijp7Im1vZGUiOiJvcHQtaW4ifSwiNSI6eyJtb2RlIjoib3B0LWluIn0sIjYiOnsibW9kZSI6Im9wdC1pbiJ9LCI3Ijp7Im1vZGUiOiJvcHQtaW4ifX0sInB1cnBvc2VzIjpudWxsLCJfdCI6Im1odjE0enk1fG0yNm03aW01In0%3D; utag_main__ss=0%3Bexp-session; _pcid=%7B%22browserId%22%3A%22m26m7ilzfx0t8kb1%22%2C%22_t%22%3A%22mhv150dq%7Cm26m7j1q%22%7D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbABYA3AIwBWAAysIAH34AmAGz8A7ACtR8AL5A; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22yd6nbNJJyBPrMd4wP0Mg%22%7D; didomi_token=eyJ1c2VyX2lkIjoiMTkyODI3MGEtNDkxOS02OWFkLWE1NGEtNDRmODY3NGUzMTg3IiwiY3JlYXRlZCI6IjIwMjQtMTAtMTJUMjA6MzQ6MzMuMjMzWiIsInVwZGF0ZWQiOiIyMDI0LTEwLTEyVDIwOjM0OjM2LjU4MVoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpsaW5rZWRpbi1tYXJrZXRpbmctc29sdXRpb25zIiwiYzptaXhwYW5lbCIsImM6YWJ0YXN0eS1MTGtFQ0NqOCIsImM6aG90amFyIiwiYzpiZWFtZXItSDd0cjdIaXgiLCJjOnRlYWxpdW1jby1EVkRDZDhaUCIsImM6dGlrdG9rLUtaQVVRTFo5IiwiYzpnb29nbGVhbmEtNFRYbkppZ1IiLCJjOmlkZWFsaXN0YS1MenRCZXFFMyIsImM6aWRlYWxpc3RhLWZlUkVqZTJjIiwiYzpjb250ZW50c3F1YXJlIiwiYzptaWNyb3NvZnQiXX0sInB1cnBvc2VzIjp7ImVuYWJsZWQiOlsiZ2VvbG9jYXRpb25fZGF0YSIsImRldmljZV9jaGFyYWN0ZXJpc3RpY3MiXX0sInZlcnNpb24iOjIsImFjIjoiQ2hHQUVBRmtGQ0lBLkFBQUEifQ==; euconsent-v2=CQGYVgAQGYVgAAHABBENBKFsAP_gAAAAAAAAHXwBwAIAAqABaAFsAUgC8wHXgAAAFJQAYAAgqEUgAwABBUIhABgACCoQ6ADAAEFQgkAGAAIKhAAA.f_wAAAAAAAAA; _hjSessionUser_250321=eyJpZCI6IjEyMGI3Njk2LTI4NDUtNWI3OC1iZTVhLWExYTg4YzY2NDkzMSIsImNyZWF0ZWQiOjE3Mjg3NjUyNzcxNjYsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_250321=eyJpZCI6ImNiNDA3MTQ1LTAzN2EtNGQwYi05MmMxLWJkOTNlMjVkOWQ3MSIsImMiOjE3Mjg3NjUyNzcxNjcsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; _tt_enable_cookie=1; _ttp=u4Rbpu_5llkAz5MAJaKjddMg4Ch; _clck=7jvrnx%7C2%7Cfpy%7C0%7C1746; _fbp=fb.1.1728765335251.485214494580389561; contact0ea7b55f-7092-47c2-be35-783491be80c9="{\'maxNumberContactsAllow\':10}"; _last_search=officialZone; _gcl_au=1.1.2098306035.1728766111; send0ea7b55f-7092-47c2-be35-783491be80c9="{}"; utag_main__prevCompleteClickName=; dicbo_id=%7B%22dicbo_fetch%22%3A1728767878024%7D; cookieSearch-1="/venta-viviendas/barcelona-barcelona/:1728767877503"; askToSaveAlertPopUp=false; utag_main__pn=18%3Bexp-session; utag_main__se=36%3Bexp-session; utag_main__st=1728769728395%3Bexp-session; utag_main__prevCompletePageName=005-idealista/portal > portal > viewAdDetail%3Bexp-1728771528411; utag_main__prevLevel2=005-idealista/portal%3Bexp-1728771528411; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.idealista.com%252F; ABTasty=uid=nbnztztfp0y1jsng&fst=1728765277130&pst=-1&cst=1728765277130&ns=1&pvt=21&pvis=21&th=; _uetsid=6600550088d911ef8ebe0fbe5b27a85b; _uetvid=66008bb088d911efbc2653cadf889408; cto_bundle=8R_AhV9nZEFMNFpMSVkzWUVPRFJmUWQ2JTJGYjlXQXAyYldWb2x5S0lVY1VhNGNaSiUyRnkzdkw0Qm9hSjAyUDRFZDJPcFBEOVJTVHNvSmE4UmdtRnkySGdoJTJGdzNiMGhvd1llc2x5dldLS3pDeHZ1RmdWUkROdWpXZVltb00xRFU0YnowMTlsVklzYTY0bjBFUFVhRnglMkJKdzFOSk9yc1VIWiUyRlJZMSUyQlJDQXZrcEp6JTJGaTF4bVR5TGFIUzRGcXQyS0pHa2lzUmhXa2tjYmFGTmt3bHpCUU1JdnpHekVTdFdKa1hsV2J5MUtkQWFRaFU2a25PVklyMkdKNVdmMjclMkZoTlZWamhIWVloYnVoZzZVdFVPUmdRSnRQZ1BmMUJNSFElM0QlM0Q; _clsk=12yvnjf%7C1728767929728%7C23%7C0%7Cb.clarity.ms%2Fcollect; datadome=_g3QJiNDhA9C77csmlgZexrglZcCO2g22hY_uXd4a6oy6Sx2KIDef6Ry77T~rdUSukllhlVz__thfMtoZx1DJHJCD9d4jel24X0D__957ncOF11nTf_wm55xlqVGt6fj',
        'priority': 'u=0, i',
        'referer': 'https://www.idealista.com/venta-viviendas/barcelona-barcelona/?ordenado-por=fecha-publicacion-desc',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    params = {
        'ordenado-por': 'fecha-publicacion-desc',
    }
    
    url=f'https://www.idealista.com/venta-viviendas/barcelona-barcelona/pagina-{page_number}.htm'

    response = requests.get(
        url=url,
        params=params,
        cookies=cookies,
        headers=headers,
    )

    print("Response status code: "+str(response.status_code))
    print(response.text)
    html=HTMLParser(response.text)
    #with open('web_scraping_idealista_bclnhouses/pages.html', 'w',encoding="utf-8") as f:
    #    f.write(response.text)
    return html


def get_house_ids(page_html):
    #article=page_html.css_first("section[class='items-container items-list']>article")
    articles=page_html.css("section[class='items-container items-list'] > article")
    house_ids=[]
    print(len(articles))
    for article in articles:
        if 'data-element-id' in article.attributes.keys():
            house_ids.append(article.attributes['data-element-id'])

    print(house_ids)
    return house_ids

def get_house_info(house_id,page_html):

    house_name=page_html.css_first("h1 > span[class='main-info__title-main']").text()
    location=page_html.css_first("span[class='main-info__title-minor']").text()
    price=page_html.css_first("span[class='info-data-price']").text()
    announcer_comment=page_html.css_first("div[class='comment']").text()
    info_features=page_html.css_first("div[class='info-features']").text()
    #characteristics=page_html.css_first("div[class='details-property-feature-one']").text()
    characteristics=page_html.css_first("div[class='details-property']").text()
    #area=
    #number_rooms=
    #description=
    house_info={
        "house_id":house_id,
        "name":house_name,
        "location":location,
        "price":price,
        "announcer_comment":announcer_comment,
        "info_features":info_features,
        "characteristics":characteristics
    }
    print(house_info)
    return house_info
 

def get_all_house_ids():
    house_ids=[]
    houses_data=[]
    index=1
    #approx maximum number of houses=2100000000
    while(index<65):
        try:
            html_page=get_bcln_house_htmls(index)
            house_ids=house_ids+get_house_ids(html_page)
        except:
            print("Ya no hay más páginas para scrapear")
            break
        else:
            print("Se descargo los ids de las casas de la página"+str(index))
            index+=1
    print(house_ids)
    return house_ids

def get_all_house_info(house_ids:list):
    failed_house_ids=[]
    all_house_info=[]
    house_htmls=[]
    print("Cantidad de casas para extraer información :" + str(len(house_ids)))
    # Response status code: 200
    # Extrayendo data de casa : 106192662...
    # Response status code: 403
    # Extrayendo data de casa : 105663269...
    for house_id in house_ids:
        try:
            print("Extrayendo data de casa : " + house_id+"...")
            house_html=get_house_html(house_id=house_id)
            time.sleep(7)
            house_htmls.append(house_html)
            #all_house_info.append(get_house_info(house_id=house_id,page_html=house_html))
        except Exception as e:
            print(str(e))
            print("No se pudo capturar la info de la casa : "+house_id)
            failed_house_ids.append(house_id)
            continue

    print("Se terminó de extraer la data de todas las casas.")
    print("Guardando en un json...")

    with open("house_htmls_total.json","w",encoding="utf-8") as json_file:
        json.dump(house_htmls,json_file,indent=4,ensure_ascii=False)
    print("Se guardó exitosamente la información de las casas de Barcelona")

    # with open("web_scraping_idealista_bclnhouses/bcln_houses_data.json","w",encoding="utf-8") as json_file:
    #     json.dump(all_house_info,json_file,indent=4,ensure_ascii=False)
    # print("Se guardó exitosamente la información de las casas de Barcelona")

    with open("failed_houses.json","w",encoding="utf-8") as json_file:
        json.dump(failed_house_ids,json_file,indent=4,ensure_ascii=False)

    print(len(house_ids))
    print(len(house_htmls))
    print(len(failed_house_ids))

    #create_csv_from_json(all_house_info)

    return all_house_info

def get_all_house_info_by_html():
    failed_house_ids=[]
    all_house_info=[]
    with open("house_htmls.json", 'r',encoding="utf-8") as f:
        house_html_strings=json.load(f) 
    print("Cantidad de casas para extraer información :" + str(len(house_html_strings)))
    for i,house_html_str in enumerate(house_html_strings):
        try:
            print("Extrayendo data de casa : " + str(i)+"...")
            house_html=HTMLParser(house_html_str)
            all_house_info.append(get_house_info(house_id=str(i),page_html=house_html))
        except Exception as e:
            print(str(e))
            print("No se pudo capturar la info de la casa : "+str(i))
            failed_house_ids.append(house_html_str)
            continue

    print("Se terminó de extraer la data de todas las casas.")
    print("Guardando en un json...")

    with open("bcln_houses_data.json","w",encoding="utf-8") as json_file:
        json.dump(all_house_info,json_file,indent=4,ensure_ascii=False)
    print("Se guardó exitosamente la información de las casas de Barcelona")

    with open("failed_houses.json","w",encoding="utf-8") as json_file:
        json.dump(failed_house_ids,json_file,indent=4,ensure_ascii=False)
    
    print("-------------------")
    print("Cantidad de casas para extraer información :" + str(len(house_html_strings)))
    print("Extraidos"+str(len(all_house_info)))
    print("Fallidos"+str(len(failed_house_ids)))
    print("-------------------")
    #create_csv_from_json(all_house_info)

    return all_house_info


def create_csv_from_json(data:list):

    columns = data[0].keys()
    columns = list(set(columns))

    with open("bcln_houses_data.csv", 'wb') as out_file:
        csv_w = csv.writer(out_file)
        csv_w.writerow(columns)

        for i_r in input:
            csv_w.writerow(map(lambda x: i_r.get(x, ""), columns))


def response_to_json(self,responseLoad,name:str):
    print("Saving response to json...")
    save_folder_concil=name+".json"
    #save_folder_odoo="oodoo_falabella_test/mkp_to_gs_order_pipeline/"+name+".json"
    with open(save_folder_concil,"w",encoding="utf-8") as json_file:
        json.dump(responseLoad,json_file,indent=4,ensure_ascii=False)


if __name__ == "__main__":
    #house_ids=get_all_house_ids()
    #print(house_ids)
    with open("house_ids_list", 'r',encoding="utf-8") as f:
        house_ids=json.load(f)
    print(len(house_ids))
    house_ids=list(set(house_ids))
    print(len(house_ids))
    all_house_info=get_all_house_info(house_ids=house_ids)
    print(all_house_info)
    #get_all_house_info()
    #get_all_house_info_by_html()







