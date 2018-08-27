import requests
import json
#git init && git remote add origin repoURL && git add . && git commit -am "Initial Commit" && git push
data = {
    "content": "a",
    "embeds": [{"title": None, "description": "e"} , {"title": "a"}],
    #"file": str(open("emojis.json")),
    "avatar_url": "https://i.pinimg.com/originals/7b/7a/97/7b7a970941939334649f90a3eede17fc.png",
    "username": "weeb-hook"
}
headers = {
    "Content-Type": "application/json"
}
b = requests.post("https://discordapp.com/api/webhooks/483378957983547392/g_JSon3JObKPS-SC71SU_yI-E-0Ym0BEJ_RBZsV6NbIpF0btdSeFUxjjeSbxel96dUs8",
                  data=json.dumps(data), headers=headers)
print(b.status_code)
