from ..utils import send_webhook, make_embed
from ..detection import robux, clothings, gamecount, gamevisits, groupimage
import requests, random, time

def send_to_free_finder(name, id, members):
  webhook = "https://discord.com/api/webhooks/1076501289770434630/WzOdksJAXgLb7KUZQk2wurUeF16ySpAbgCWflYSEoT2gxtIi5nlWfZi-KmeZjJrXNObx"
  data = {"content": ""}
  data["embeds"] = [
    {
      "title": "∆ New Group Found!",
      "description": f"**• ID:** `{id}`\n**• Name:** `{name}`\n**• Members:** `{members}`\n**• Ad:** **__[McGroups Group Finder](https://discord.gg/robloxgroups)__**",
      "url": f"https://www.roblox.com/groups/{id}",
      "color": random.randint(8000000, 16777215),
      "footer": {
        "text": "© McGroups",
        "icon_url": "https://media.discordapp.net/attachments/1055864885650673665/1064158737775997088/pfp2.png"
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ]
  return requests.post(webhook, json=data)

def send_to_level_5(name, id, members, robux):
  webhook = "https://discord.com/api/webhooks/1076501289770434630/WzOdksJAXgLb7KUZQk2wurUeF16ySpAbgCWflYSEoT2gxtIi5nlWfZi-KmeZjJrXNObx"
  data = {"content": ""}
  data["embeds"] = [
    {
      "title": "∆ New Group Found!",
      "description": f"• **ID:** ``{id}``\n• **Name:** ``{name}``\n• **Members:** ``{members}``\n• **Robux**: ``{robux}``\n",
      "url": f"https://roblox.com/groups/{id}",
      "color": random.randint(8000000, 16777215),
      "footer": {
        "text": "© McGroups",
        "icon_url": "https://media.discordapp.net/attachments/1055864885650673665/1064158737775997088/pfp2.png"
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ]
  requests.post(webhook, json=data)

def send_to_premium_finder(name, id, members, robx, clothin, gams, gamevisi):
  webhook = "https://discord.com/api/webhooks/1076501289770434630/WzOdksJAXgLb7KUZQk2wurUeF16ySpAbgCWflYSEoT2gxtIi5nlWfZi-KmeZjJrXNObx"
  data = {"content": ""}
  data["embeds"] = [
    {
      "title": "∆ New Group Found!",
      "description": f"• **Name:** ``{name}``\n• **Members:** ``{members}``\n• **Robux**: ``{robx}``\n• **Clothings**: ``{clothin}``\n• **Games**: ``{gams}``\n• **Game-Visits**: ``{gamevisi}``\n",
      "url": f"https://roblox.com/groups/{id}",
      "color": random.randint(8000000, 16777215),
      "footer": {
        "text": "© McGroups",
        "icon_url": "https://media.discordapp.net/attachments/1055864885650673665/1064158737775997088/pfp2.png"
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ]
  return requests.post(webhook,json=data)


def trulymore_group_feed(name, id, members, robx, clothin, gams, gamevisi):
    webhook = "https://discord.com/api/webhooks/1076501289770434630/WzOdksJAXgLb7KUZQk2wurUeF16ySpAbgCWflYSEoT2gxtIi5nlWfZi-KmeZjJrXNObx"
    data = {"content": "@everyone | **Claim the Group**."}
    data["embeds"] = [
    {
      "title": "∆ New Group without lad Found!",
      "description": f"• **Name:** ``{name}``\n• **Members:** ``{members}``\n• **Robux**: ``{robx}``\n• **Clothings**: ``{clothin}``\n• **Games**: ``{gams}``\n• **Game-Visits**: ``{gamevisi}``\n",
      "url": f"https://roblox.com/groups/{id}",
      "color": random.randint(8000000, 16777215),
      "footer": {
        "text": "© fuck lad | Private Feed",
        "icon_url": "https://media.discordapp.net/attachments/1055864885650673665/1064158737775997088/pfp2.png"
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ]  
    return requests.post(webhook, json=data)


def xyz_group_feed(name, id, members, robx, clothin, gams, gamevisi):
    webhook = "https://discord.com/api/webhooks/1076501289770434630/WzOdksJAXgLb7KUZQk2wurUeF16ySpAbgCWflYSEoT2gxtIi5nlWfZi-KmeZjJrXNObx"
    data = {"content": "@everyone | **Claim the Group**."}
    data["embeds"] = [
    {
      "title": "∆ New Group Found!",
      "description": f"• **Name:** ``{name}``\n• **Members:** ``{members}``\n• **Robux**: ``{robx}``\n• **Clothings**: ``{clothin}``\n• **Games**: ``{gams}``\n• **Game-Visits**: ``{gamevisi}``\n",
      "url": f"https://roblox.com/groups/{id}",
      "color": random.randint(8000000, 16777215),
      "footer": {
        "text": "© fuck lad | Private Feed",
        "icon_url": "https://media.discordapp.net/attachments/1055864885650673665/1064158737775997088/pfp2.png"
      },
      "thumbnail": {"url": groupimage(id)}}] 
    return requests.post(webhook, json=data)

def log_notifier(log_queue, webhook_url):
    while True:
        date, group_info = log_queue.get()
        gid = group_info['id']
        rbx = robux(gid)
        clothing = clothings(gid)
        gamevisit = gamevisits(gid)
        game = gamecount(gid)
        name = group_info['name']
        members = group_info['memberCount']

        print(f"[SCRAPED] : ( ID: {group_info['id']} ) | ( Name: {group_info['name']} ) | ( Members: {group_info['memberCount']} )")
        if int(members) <= 10 and int(rbx) <= 5 and int(clothing) <= 5 and int(gamevisit) <= 50:
          send_to_free_finder(name, gid, members)
        elif int(members) <= 25 and int(rbx) <= 10 and int(clothing) <= 10 and int(gamevisit) <= 100:
          send_to_level_5(name, gid, members, rbx)
        elif int(members) <= 250 and int(rbx) <= 50 and int(clothing) <= 20 and int(gamevisit) <= 2500:
          send_to_premium_finder(group_info['name'], group_info['id'], group_info['memberCount'], robux(group_info['id']), clothings(group_info['id']), gamecount(group_info['id']), gamevisits(group_info['id']))
        elif int(members) <= 570 and int(rbx) <= 300 and int(clothing) <= 80 and int(gamevisit) <= 5000:
          trulymore_group_feed(group_info['name'], group_info['id'], group_info['memberCount'], robux(group_info['id']), clothings(group_info['id']), gamecount(group_info['id']), gamevisits(group_info['id']))
        else:
          xyz_group_feed(group_info['name'], group_info['id'], group_info['memberCount'], robux(group_info['id']), clothings(group_info['id']), gamecount(group_info['id']), gamevisits(group_info['id']))
