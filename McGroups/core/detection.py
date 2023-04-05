import requests
import json
from requests_futures.sessions import FuturesSession
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import RequestException

roblox_cookie = {".ROBLOSECURITY": "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_C7B465036EC16C831732D7B0CB9CEF57F841D6605852D63AC6A345B64022F5D93F08EF0BF4F3BBFB3F7353286BE4F950E76672C0A15F2AAA7B456511FA9A7A26796EE848C80BD89991055C24F3185ED8C2015C4F011077B4CFA82D02BB5C91FF11CD8F1CF897D1995AAF1CAABA503E9A5A0F38D2155D512A2CF2F8E1825E6AE5397B10325E83BE89F265B547D076E3EAA23BA4BABD9C354CC06A49B6FA70B0D577DB0F1433DAD5AAFBFDD27908603935DE7DA7CF6A03CD9345C0A4C10E71771BF68A73C620F059AF323CCC0A80D6DA575DA0FE9E3F671103986BA9751B8E0108662BE00FB8B35B2E8C7403FF70C9391114A391DFAAEB7B5B5549EFF446ED30AF272CFC1AC53AFE92C85E1ADCC555C81FE8BEA82CD7D7E2465675E1A9416ADA2A5D5C8DD5A58E5AB34B506128A17098BE02FBD3932D4E76CC0A5497AFC560D92B0746C707A4C1C4ED9E409A869AF368AC1FF451BA035302C56DB988A7DB69C27D1712385D"}
def clothings(id):
  clothings = 0
  session = FuturesSession()
  retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
  session.mount('https://', HTTPAdapter(max_retries=retries))
  try:
    check = session.get(f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorTargetId={id}&CreatorType=2&Limit=30").result()
    check = check.json()
  except RequestException as e:
    print(e)
    return 0

  def get_page(cursor=None):
      nonlocal check
      try:
        if cursor:
          url = f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorTargetId={id}&CreatorType=2&Limit=30&cursor={cursor}"
        else:
          url = f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorTargetId={id}&CreatorType=2&Limit=30"
        check = session.get(url).result().json()
      except RequestException as e:
        print(e)
        return 0
      return check

  while True:
      if "data" in check:
          clothings += len(check['data'])
      if "nextPageCursor" not in check or not check['nextPageCursor']:
          break
      else:
          check = get_page(check['nextPageCursor'])
  return clothings

def robux(id):
  # Import Local Cookie Variable
  global roblox_cookie
  session = FuturesSession()
  retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
  session.mount('https://', HTTPAdapter(max_retries=retries))
  try:
      # Send the request asynchronously and return a Future object
      future = session.get(f'https://economy.roblox.com/v1/groups/{id}/currency', cookies=roblox_cookie, timeout=5)
  except RequestException as e:
    print(e)
    return 0
  try:
    response = future.result()
    data = json.loads(response.text)
    if "robux" in data:
      robux = data.get("robux", 0)
    else:
      robux = 0
  except RequestException as e:
    print(e)
    return 0
  return robux

def gamevisits(id):
  # Create a FuturesSession object
  session = FuturesSession()
  retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
  session.mount('https://', HTTPAdapter(max_retries=retries))

  # Make the API request asynchronously
  try:
    future = session.get(f'https://games.roblox.com/v2/groups/{id}/games?accessFilter=All&sortOrder=Asc&limit=100', timeout=5)
  except RequestException as e:
    print(e)
    return 0

  # Wait for the request to complete and load the response into a dictionary
  try:
    response = future.result()
    os = json.loads(response.text)
    if "data" in os:
      data = os["data"]
    else:
      data = 0
      
  except RequestException as e:
    print(e)
    return 0

  # If there are no games, return "None"
  if not data:
    return 0
  
  # Find the total number of visits for all games
  total_visits = 0
  for game in data:
    visits = game["placeVisits"]
    total_visits += visits
  return total_visits
  
def gamecount(id):
  session = FuturesSession()
  retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
  session.mount('https://', HTTPAdapter(max_retries=retries))
  try:
      # Send the request asynchronously and return a Future object
      future = session.get(f'https://games.roblox.com/v2/groups/{id}/games?accessFilter=All&sortOrder=Asc&limit=100', timeout=5)
  except RequestException as e:
    print(e)
    return 0
  try:
    response = future.result()
    os = json.loads(response.text)
    if "data" in os:
      data = os["data"]
    else:
      data = 0
  except RequestException as e:
    print(e)
    return 0
  if not data:
    return 0
  else:
    return len(data)

def groupimage(id):
  # Create a session with retries enabled
  session = FuturesSession()
  retry = Retry(connect=3, backoff_factor=0.5, status_forcelist=[502, 503, 504])
  adapter = HTTPAdapter(max_retries=retry)
  session.mount('https://', adapter)

  # Send the request asynchronously and return a Future object
  future = session.get(f'https://thumbnails.roblox.com/v1/groups/icons?groupIds={id}&size=150x150&format=Png&isCircular=false', timeout=5)

  # Wait for the request to complete and handle any errors that may occur
  try:
    response = future.result()
    icon_url = response.json()
    if "data" in icon_url and len(icon_url["data"]) > 0:
       image = icon_url["data"][0]["imageUrl"]
    else:
       image = "https://cdn.discordapp.com/attachments/1008516436840431636/1083821033846485043/nigger.jpeg"

  except RequestException as e:
    print(e)
    image = "https://cdn.discordapp.com/attachments/1008516436840431636/1083821033846485043/nigger.jpeg"
  return image 
