# -*- coding: utf-8 -*-
#zz7 Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

zz7 = LINETCR.LINE()
#zz7.login(qr=True)
zz7.login(token='EvoNQChPf2K0pB7mPTqa.gIHgalwJsMTFisMR+xM0wG.ZLB4FwpbMM+lU5tzye7IQBoYVRJ20qrETVhnc3/ecXg=')
zz7.loginResult()
print "zz7-Login Success\n\n=====[Sukses Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')


selfMessage ="""
╔═════════════════════════
║   ۩۞۩ S E L F ۩۞۩ 
╠═════════════════════════
┣🇮🇩━⏩〔Hi〕
┣🇮🇩━⏩〔Me〕
┣🇮🇩━⏩〔Mymid〕
┣🇮🇩━⏩〔Mid @〕
┣🇮🇩━⏩〔SearchID〕
┣🇮🇩━⏩〔Checkdate 〕
┣🇮🇩━⏩〔Kalender〕
┣🇮🇩━⏩〔Steal contact〕
┣🇮🇩━⏩〔Pp @〕
┣🇮🇩━⏩〔Cover @〕
┣🇮🇩━⏩〔Auto like〕
┣🇮🇩━⏩〔Scbc Text〕
┣🇮🇩━⏩〔Cbc Text〕
┣🇮🇩━⏩〔Gbc Text〕
┣🇮🇩━⏩〔Bio @〕
┣🇮🇩━⏩〔Info @〕
┣🇮🇩━⏩〔Name @〕
┣🇮🇩━⏩〔Profile @〕
┣🇮🇩━⏩〔Contact @〕
┣🇮🇩━⏩〔Getvid @〕
┣🇮🇩━⏩〔Friendlist〕
┣🇮🇩━⏩〔Micadd @〕
┣🇮🇩━⏩〔Micdel @〕
┣🇮🇩━⏩〔Miclist〕
╠═════════════════════════
║     👽 By : ZeroZeveN 👽
║  👽line.me/ti/p/ricco1311👽
╚═════════════════════════"""

botMessage ="""
╔═════════════════════════
║   ۩۞۩ B O T ۩۞۩
╠═════════════════════════
┣🇮🇩━⏩〔Absen〕
┣🇮🇩━⏩〔Respon〕
┣🇮🇩━⏩〔Runtime〕
┣🇮🇩━⏩〔copy @〕
┣🇮🇩━⏩〔Copycontact〕
┣🇮🇩━⏩〔Mybackup〕
┣🇮🇩━⏩〔Mybio 〔T〕
┣🇮🇩━⏩〔Myname 〔T〕
┣🇮🇩━⏩〔@bye〕
┣🇮🇩━⏩〔Bot on/off〕
╠═════════════════════════
║     👽 By : ZeroZeveN 👽
║  👽line.me/ti/p/ricco1311👽
╚═════════════════════════"""

mediaMessage ="""
╔═════════════════════════
║   ۩۞۩ M E D I A ۩۞۩
╠═════════════════════════
┣🇮🇩━⏩〔Youtube J 〕
┣🇮🇩━⏩〔Youtubevideo J〕
┣🇮🇩━⏩〔Youtubesearch:0 J〕
┣🇮🇩━⏩〔Image NamaGambar〕
┣🇮🇩━⏩〔Say T〕
┣🇮🇩━⏩〔Say-en T〕
┣🇮🇩━⏩〔Say-jp T〕
┣🇮🇩━⏩〔Tr-id T 〔 En  ID〕
┣🇮🇩━⏩〔Tr-en T 〔ID  En〕
┣🇮🇩━⏩〔Tr-th T 〔ID Th〕
┣🇮🇩━⏩〔Id@en T 〔ID En〕
┣🇮🇩━⏩〔Id@th T 〔ID TH〕
┣🇮🇩━⏩〔En@id T 〔 En  ID〕
┣🇮🇩━⏩〔Gift〕
┣🇮🇩━⏩〔Giftbycontact〕
┣🇮🇩━⏩〔Gif gore〕
┣🇮🇩━⏩〔Google 〔T〕
┣🇮🇩━⏩〔Playstore NamaApp〕
┣🇮🇩━⏩〔Fancytext T〕
┣🇮🇩━⏩〔musik J-Penyanyi〕
┣🇮🇩━⏩〔lirik J-Penyanyi〕
┣🇮🇩━⏩〔musrik J-Penyanyi〕
┣🇮🇩━⏩〔ig 〔UsrNameIG〕
┣🇮🇩━⏩〔Checkig 〔UsrIG〕
┣🇮🇩━⏩〔apakah 〔T〕
┣🇮🇩━⏩〔kapan 〔T〕
┣🇮🇩━⏩〔hari 〔T 〕
┣🇮🇩━⏩〔berapa〔 T 〕
┣🇮🇩━⏩〔berapakah 〔T〕
╠═════════════════════════
║     👽 By : ZeroZeveN 👽
║  👽line.me/ti/p/ricco1311👽
╚═════════════════════════"""

groupMessage ="""
╔═════════════════════════
║   ۩۞۩ G R O U P ۩۞۩
╠═════════════════════════
┣🇮🇩━⏩〔Welcome〕
┣🇮🇩━⏩〔Say welcome〕
┣🇮🇩━⏩〔Invite creator〕
┣🇮🇩━⏩〔Cctv〕
┣🇮🇩━⏩〔Ciduk〕
┣🇮🇩━⏩〔Gn:〔NG〕
┣🇮🇩━⏩〔Tag all〕
┣🇮🇩━⏩〔lurk on/off〕
┣🇮🇩━⏩〔lurkers〕
┣🇮🇩━⏩〔Recover〕
┣🇮🇩━⏩〔Cancel〕
┣🇮🇩━⏩〔Cancelall〕
┣🇮🇩━⏩〔Gcreator〕
┣🇮🇩━⏩〔Ginfo〕
┣🇮🇩━⏩〔Gurl〕
┣🇮🇩━⏩〔List group〕
┣🇮🇩━⏩〔Pict group:〔NG〕
┣🇮🇩━⏩〔Spam: 〔T〕
┣🇮🇩━⏩〔Add all〕
┣🇮🇩━⏩〔Kick: (Mid)〕
┣🇮🇩━⏩〔Invite: (Mid)〕
┣🇮🇩━⏩〔Invite〕
┣🇮🇩━⏩〔Memlist〕
┣🇮🇩━⏩〔Getgroup image〕
┣🇮🇩━⏩〔Urlgroup Image〕
╠═════════════════════════
║     👽 By : ZeroZeveN 👽
║  👽line.me/ti/p/ricco1311👽
╚═════════════════════════"""
vip="u1a284600b5a34a6b5f2129abfd79b45a"

setMessage ="""
╔═════════════════════════
║   ۩۞۩ S E T ۩۞۩
╠═════════════════════════
┣🇮🇩━⏩〔Notif on/off〕
┣🇮🇩━⏩〔Mimic on/off〕
┣🇮🇩━⏩〔Url on/off〕
┣🇮🇩━⏩〔Read on/off〕
┣🇮🇩━⏩〔Sider on/off〕
┣🇮🇩━⏩〔K on/off〕
┣🇮🇩━⏩〔Sticker on/off〕
┣🇮🇩━⏩〔Simi on/off〕
┣🇮🇩━⏩〔lurk on/off〕
┣🇮🇩━⏩〔Bot on/off 〕
╠═════════════════════════
║     👽 By : ZeroZeveN 👽
║  👽line.me/ti/p/ricco1311👽
╚═════════════════════════"""

creatorMessage ="""
╔═════════════════════════
║   ۩۞۩ C R E A T O R ۩۞۩
╠═════════════════════════
┣🇮🇩━⏩〔Crash〕
┣🇮🇩━⏩〔Kickall〕
┣🇮🇩━⏩〔Bc: 〔T〕
┣🇮🇩━⏩〔Join group: 〔NG〕
┣🇮🇩━⏩〔Leave group: 〔NG〕
┣🇮🇩━⏩〔Leave all group〕
┣🇮🇩━⏩〔Tag on/off〕
┣🇮🇩━⏩〔Bot restart〕
┣🇮🇩━⏩〔Turn off〕
╠═════════════════════════
║     👽 By : ZeroZeveN 👽
║  👽line.me/ti/p/ricco1311👽
╚═════════════════════════"""

adminMessage ="""
╔═════════════════════════
║   ۩۞۩ A D M I N ۩۞۩
╠═════════════════════════
┣🇮🇩━⏩〔Allprotect on/off〕
┣🇮🇩━⏩〔Ban〕
┣🇮🇩━⏩〔Unban〕
┣🇮🇩━⏩〔Ban @〕
┣🇮🇩━⏩〔Unban @〕
┣🇮🇩━⏩〔Ban list〕
┣🇮🇩━⏩〔Clear ban〕
┣🇮🇩━⏩〔Kill〕
┣🇮🇩━⏩〔Kick @〕
┣🇮🇩━⏩〔Set member: (Jml)〕
┣🇮🇩━⏩〔Ban group: 〔NG〕
┣🇮🇩━⏩〔Del ban: 〔NG〕
┣🇮🇩━⏩〔List ban〕
┣🇮🇩━⏩〔Kill ban〕
┣🇮🇩━⏩〔Glist〕
┣🇮🇩━⏩〔Glistmid〕
┣🇮🇩━⏩〔Details group: 〔〔(Gid)〕
┣🇮🇩━⏩〔Cancel invite: 〔(Gid)〕
┣🇮🇩━⏩〔Invitemeto: 〔(Gid)〕
┣🇮🇩━⏩〔Acc invite〕
┣🇮🇩━⏩〔Removechat〕
┣🇮🇩━⏩〔Qr on/off〕
┣🇮🇩━⏩〔Autokick on/off〕
┣🇮🇩━⏩〔Autocancel on/off〕
┣🇮🇩━⏩〔Invitepro on/off〕
┣🇮🇩━⏩〔Join on/off〕
┣🇮🇩━⏩〔Joincancel on/off〕
┣🇮🇩━⏩〔R1 on/off〕
┣🇮🇩━⏩〔R2 on/off〕
┣🇮🇩━⏩〔R3 on/off〕
┣🇮🇩━⏩〔Rkick on/off〕
╠═════════════════════════
║     👽 By : ZeroZeveN 👽
║  👽line.me/ti/p/ricco1311👽
╚═════════════════════════"""

teamMessage ="""👽👽👽WELCOME👽👽👽
┏━┳┳┳┓┏┳┳┳┳┳┓┏┳┳┓
┃zz7Bot┃ Bantai Pembangkang┃
┗ⓞ━━ⓞ┻━┻ⓞ━ⓞ┻┻ⓞ━ⓞ╯
👽line.me/ti/p/ricco1311👽
.        (҂`_´)
         <,︻╦̵̵̿╤━ ҉     ~  •
█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●
▂▄▅█████████▅▄▃▂…
[███████████████████]
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙
║╔═╗║        ║║
║╚══╦══╣║╔══╦╗╔╗
╚══╗║╔╗║║║╔╗║╚╝║
║╚═╝║╔╗║╚╣╔╗║║║║
╚═══╩╝╚╩═╩╝╚╩╩╩╝
────────────────────────────
👽        (҂`_´)
         <,︻╦̵̵̿╤─ ҉     ~  •
█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●
▂▄▅█████████▅▄▃▂…
[███████████████████]
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙
────────────────────────────

👽DILARANG BANYAK BACOT KEPADA KAMI👽
👽BECAUSE WE ARE COMBAT TEAM👽
────────────────────────────
🇮🇩 👽 🇮🇩 👽 🇮🇩 👽 🇮🇩 
🇮🇩 ┏━┳┳┳━┳┳┓
🇮🇩 ┃━┫┃┃┏┫━┫
🇮🇩 ┃┏┫┃┃┗┫┃┃
🇮🇩 ┗┛┗━┻━┻┻┛
🇮🇩 ┏┳┳━┳┳┓ 
🇮🇩 ┃┃┃┃┃┃┃
🇮🇩 ┣┓┃┃┃┃┃
🇮🇩 ┗━┻━┻━┛
🇮🇩 👽 🇮🇩 👽 🇮🇩 👽 🇮🇩
━━━━━━━━━━━━━━━━━━━━━━━━━ """

helpMessage ="""
╔═════════════════════════
║   ۩۞۩ H E L P ۩۞۩
╠═════════════════════════
┣🇮🇩━⏩〔Help self〕
┣🇮🇩━⏩〔Help bot〕
┣🇮🇩━⏩〔Help group〕
┣🇮🇩━⏩〔Help set〕
┣🇮🇩━⏩〔Help media〕
┣🇮🇩━⏩〔Help admin〕
┣🇮🇩━⏩〔Help creator〕
┣🇮🇩━⏩〔Owner〕
┣🇮🇩━⏩〔Speed〕
┣🇮🇩━⏩〔Speed test〕
┣🇮🇩━⏩〔Status〕
┣🇮🇩━⏩〔Team〕
╠═════════════════════════
║     👽 By : ZeroZeveN 👽
║  👽line.me/ti/p/ricco1311👽
╚═════════════════════════"""


KAC=[zz7]
mid = zz7.getProfile().mid
Bots=[mid]
Creator=["u1a284600b5a34a6b5f2129abfd79b45a"]
admin=["u1a284600b5a34a6b5f2129abfd79b45a"]

contact = zz7.getProfile()
backup1 = zz7.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = zz7.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "Bot":True,
    "AutoJoin":False,
    "AutoJoinCancel":False,
    "memberscancel":30,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'copy':{},    
    'likeOn':{},
    'detectMention':False,
    'detectMention2':True,
    'detectMention3':False,
    'kickMention':False,  
    'sticker':False,  
    'timeline':False,
    "Timeline":False,
    "comment":"\n────────────────────────\n 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n╭━ A✒ U━ T✒ O━ L✒ I━ K✒E✒✒\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫\n┃ARIFISTIFIK ◾ID SMULE▪ARIF_MH┃\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n.        (҂`_´)\n         <,︻╦̵̵̿╤─ ҉     ~  •\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●\n▂▄▅█████████▅▄▃▂…\n[███████████████████]\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n───────────────\n",    
    "comment1":"\n────────────────────────\n 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n╭━ A✒ U━ T✒ O━ L✒ I━ K✒E✒✒\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫\n┃ARIFISTIFIK ◾ID SMULE▪ARIF_MH┃\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n.        (҂`_´)\n         <,︻╦̵̵̿╤─ ҉     ~  •\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●\n▂▄▅█████████▅▄▃▂…\n[███████████████████]\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n───────────────\n",
    "comment2":"\n────────────────────────\n 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n╭━ A✒ U━ T✒ O━ L✒ I━ K✒E✒✒\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫\n┃ARIFISTIFIK ◾ID SMULE▪ARIF_MH┃\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n.        (҂`_´)\n         <,︻╦̵̵̿╤─ ҉     ~  •\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●\n▂▄▅█████████▅▄▃▂…\n[███████████████████]\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n───────────────\n",
    "comment3":"\n────────────────────────\n 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n╭━ A✒ U━ T✒ O━ L✒ I━ K✒E✒✒\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫\n┃ARIFISTIFIK ◾ID SMULE▪ARIF_MH┃\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n.        (҂`_´)\n         <,︻╦̵̵̿╤─ ҉     ~  •\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●\n▂▄▅█████████▅▄▃▂…\n[███████████████████]\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n───────────────\n",
    "comment4":"\n────────────────────────\n 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n╭━ A✒ U━ T✒ O━ L✒ I━ K✒E✒✒\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫\n┃ARIFISTIFIK ◾ID SMULE▪ARIF_MH┃\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n.        (҂`_´)\n         <,︻╦̵̵̿╤─ ҉     ~  •\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●\n▂▄▅█████████▅▄▃▂…\n[███████████████████]\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n───────────────\n",
    "comment5":"\n────────────────────────\n 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n╭━ A✒ U━ T✒ O━ L✒ I━ K✒E✒✒\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫\n┃ARIFISTIFIK ◾ID SMULE▪ARIF_MH┃\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n.        (҂`_´)\n         <,︻╦̵̵̿╤─ ҉     ~  •\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●\n▂▄▅█████████▅▄▃▂…\n[███████████████████]\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n───────────────\n",
    "comment6":"SEKIAN LIKE DAN KOMENTAR GUE SEMOGA LU BAHAGIA DISANA WKWKWK",
    "commentOn":True,
    "commentBlack":{},
    "message":"Thx For Add Me (^_^)\nInvite Me To Your Group ヘ(^_^)ヘ",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":False,
    "Notif":False,
    "inviteprotect":False,    
    "alwaysRead":False,    
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{True}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
    
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }    

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')
            
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       zz7.sendMessage(msg)
    except Exception as error:
       print error          
                        
       

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              zz7.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                zz7.sendText(op.param1,str(wait["ThankS for add me"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	
	    if op.type == 55:
                try:
                     if op.param1 in wait2['readPoint']:     
                         if op.param2 in wait2['readMember'][op.param1]:
                              pass
                         else:
                              wait2['readMember'][op.param1] += op.param2
                         wait2['ROM'][op.param1][op.param2] = op.param2
                         with open('sider.json', 'w') as fp:
                          json.dump(wait2, fp, sort_keys=True, indent=4)
                     else:
                         pass
                except:
                    pass
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = zz7.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        zz7.sendText(op.param1, "Waduh Ada"+"🇮🇩━⏩" + Name + "╦╩"+"\nLagi Ngintip\nSini Ikutan Chat Bos Jangan Sider Mulu(-__-)")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        zz7.sendText(op.param1, "🇮🇩👽zz7Bot🇮🇩Jakarta🇮🇩Indonesia👽🇮🇩"+"\nHallo" + Name + "\nNgapain Ngintip??Sini Ikutan Chat Sama Kita(-__-)")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    zz7.sendText(op.param1, "🇮🇩👽zz7Bot🇮🇩Jakarta🇮🇩Indonesia👽🇮🇩"+"\nHaaii" + Name + "\nNgapain Ngintip??Kagak Ada Janda Atau Bujang Disini\nSana Cari Di Room Laen")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            zz7.leaveRoom(op.param1)

        if op.type == 21:
            zz7.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    zz7.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = zz7.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        zz7.acceptGroupInvitation(op.param1)
                        zz7.sendText(op.param1,"Maaf " + zz7.getContact(op.param2).displayName + "\nMember Kurang Dari 30 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        zz7.leaveGroup(op.param1)                        
		    else:
                        zz7.acceptGroupInvitation(op.param1)
			zz7.sendText(op.param1,"♠Ketik ✴Help✴ Untuk Bantuan♠\n♠Harap Gunakan Dengan Bijak ^_^ ♠")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = zz7.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        zz7.rejectGroupInvitation(op.param1)
		    else:
                        zz7.acceptGroupInvitation(op.param1)
			zz7.sendText(op.param1,"♠Ketik ✴Help✴ Untuk Bantuan♠\n♠Harap Gunakan Dengan Bijak ^_^ ♠")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        zz7.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			zz7.cancelGroupInvitation(op.param1, [op.param3])
			zz7.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    zz7.cancelGroupInvitation(op.param1,[op.param3])
                    zz7.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               zz7.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    zz7.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        zz7.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        zz7.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        zz7.kickoutFromGroup(op.param1,[op.param2])
			zz7.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    zz7.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        zz7.kickoutFromGroup(op.param1,[op.param2])
			zz7.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                zz7.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        zz7.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    zz7.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    zz7.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
          if wait["Notif"] == True:
            if op.param2 in Creator:
                return
            ginfo = zz7.getGroup(op.param1)
            contact = zz7.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            zz7.sendText(op.param1,"Assalamualaikum.wr.wb" + zz7.getContact(op.param2).displayName + "⋱ ⋮ ⋰" + "\n⋯ ◯ ⋯ ︵ 　　　　　　^v^" + "\n¸︵︵( ░░ )︵.︵.︵" + "\n(´░░░░░░ ') ░░░' ) `´︶´¯`︶´`︶´︶´`　^v^　　^v^" + "\n" + "\n╔┓┏╦━━╦┓╔┓╔━━╗╔╗" + "\n║┗┛║┗━╣┃║┃║╯╰║║║" + "\n║┏┓║┏━╣┗╣┗╣╰╯║╠╣" + "\n╚┛┗╩━━╩━╩━╩━━╝╚╝" + "\n♪♫•*¨*•.¸¸❤¸¸.•*¨*•♫♪♪♫•*¨*•.¸¸❤¸¸.•*¨*•♫♪" + "\nSELAMAT DATANG DI ✴ " + str(ginfo.name) + " ✴" + "\nYuk kenalan sama temen-temen 😄\nJangan lupa baca note ya kak...\nSemoga Betah Disini ^_^")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            zz7.sendMessage(c)  
            zz7.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269548",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            zz7.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Notif"] == True:
            if op.param2 in Creator:
                return
            zz7.sendText(op.param1,"Good Bye " + zz7.getContact(op.param2).displayName +  "\nBawain Sekalian Bajunya Dan Sendalnya Awas Ketinggalan . . . (p′︵‵。) 🤗")
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269542",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            zz7.sendMessage(d)                  
            print "MEMBER HAS LEFT THE GROUP"
            
        if op.type == 26:
            msg = op.message
            
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        zz7.sendText(msg.to,text)             
            
            
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                zz7.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = zz7.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  zz7.sendText(msg.to,ret_)
                                  zz7.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = zz7.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag!! Lagi Sibuk Anu",cName + " Ngapain Ngetag? Mau Dicipok?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Japri Aja","Eeh Dasar Pekok Loe, Gue Lagi Nanggung", cName + " Eeh KoplakcNgapain Sih Tag Gue Trus?","Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gue " + cName, "Loe Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, lagi Modol!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  zz7.sendText(msg.to,ret_)
                                  break   
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = zz7.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [ "Sekali lagi ngetag gw sumpahin Jempol Loe Kutilan!!","Nggak Usah Tag-Tag! Gue Tau Loe Kangen Berat Ke Gue","Woii " + cName + " Jangan Ngetag, Lagi Enak Anu Nih!"  ]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  zz7.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "20001316",
                                                       "STKPKGID": "1582380",
                                                       "STKVER": "1" }
                                  zz7.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = zz7.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Woii " + cName + ", Dasar Jones Ngetag Mulu!"]
                    balas1 = "Ini Foto Sii Jones Yang Suka Ngetag. . ."
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  zz7.sendText(msg.to,ret_)
                                  zz7.sendText(msg.to,balas1)
                                  zz7.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "11764508",
                                                       "STKPKGID": "6641",
                                                       "STKVER": "1" }
                                  zz7.sendMessage(msg)                                
                                  break  
                                  
        if op.type == 25:
            msg = op.message                                  
                              
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                zz7.sendText(msg.to,"Combat Team On")  

        if op.type == 25:
          if wait["Bot"] == True:    
            msg = op.message
            
            
            if msg.contentType == 7:
              if wait["sticker"] == True:
                msg.contentType = 0
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                zz7.sendText(msg.to, filler)
                wait["sticker"] = False
            else:
                pass              

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    zz7.sendChatChecked(msg.from_,msg.id)
                else:
                    zz7.sendChatChecked(msg.to,msg.id)
                    
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     zz7.like(url[25:58], url[66:], likeType=1005)
                     zz7.comment(url[25:58], url[66:], wait["comment"])
                     zz7.comment(url[25:58], url[66:], wait["comment1"])
                     zz7.comment(url[25:58], url[66:], wait["comment2"])
                     zz7.comment(url[25:58], url[66:], wait["comment3"])
                     zz7.comment(url[25:58], url[66:], wait["comment4"])
                     zz7.comment(url[25:58], url[66:], wait["comment5"])
                     zz7.comment(url[25:58], url[66:], wait["comment6"])
                     zz7.comment(url[25:58], url[66:], wait["comment7"])
                     zz7.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False


            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            zz7.sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            zz7.sendText(msg.to,"Ditambahkan")
		    else:
			zz7.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        zz7.sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        zz7.sendText(msg.to,"Tidak Ada Black List")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     zz7.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = zz7.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = zz7.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         zz7.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = zz7.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = zz7.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         zz7.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = zz7.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        zz7.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        zz7.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        zz7.sendText(msg.to,"Can not be used outside the group")
                    else:
                        zz7.sendText(msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': vip}
                zz7.sendMessage(msg)
		zz7.sendText(msg.to,"Itu Majikan Kami (^_^)")

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = zz7.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                zz7.sendMessage(msg)
		zz7.sendText(msg.to,"Itu Yang Buat Grup Ini")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    zz7.sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = zz7.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                zz7.findAndAddContactsByMid(target)
                                contact = zz7.getContact(target)
                                cu = zz7.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                zz7.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                zz7.sendText(msg.to,"Profile Picture " + contact.displayName)
                                zz7.sendImageWithURL(msg.to,image)
                                zz7.sendText(msg.to,"Cover " + contact.displayName)
                                zz7.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = zz7.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                zz7.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                zz7.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break

            if msg.contentType == 13:
                if wait["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = zz7.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        zz7.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                zz7.CloneContactProfile(target)
                                zz7.sendText(msg.to, "Copied (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["copy"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = zz7.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             zz7.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 zz7.findAndAddContactsByMid(target)
                                 zz7.inviteIntoGroup(msg.to,[target])
                                 zz7.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      zz7.sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["Key creator","help creator","Help creator"]:
                zz7.sendText(msg.to,creatorMessage)
                zz7.sendText(msg)

            elif msg.text in ["Key group","help group","Help group"]:
                zz7.sendText(msg.to,groupMessage)
                zz7.sendText(msg)

            elif msg.text in ["Key","help","Help"]:
                zz7.sendText(msg.to,helpMessage)
                zz7.sendText(msg)

            elif msg.text in ["Key self","help self","Help self"]:
                zz7.sendText(msg.to,selfMessage)              
                zz7.sendText(msg)

            elif msg.text in ["Key bot","help bot","Help bot"]:
                zz7.sendText(msg.to,botMessage)
                zz7.sendText(msg)

            elif msg.text in ["Key set","help set","Help set"]:
                zz7.sendText(msg.to,setMessage)
                zz7.sendText(msg)
                
            elif msg.text in ["Team","team"]:
            	zz7.sendText(msg.to,teamMessage)               
                zz7.sendText(msg.to, "MY FAMS")
                
            elif msg.text in ["Key media","help media","Help media"]:
                zz7.sendText(msg.to,mediaMessage)
                zz7.sendText(msg)
                
            elif msg.text in ["Key admin","help admin","Help admin"]:
                zz7.sendText(msg.to,adminMessage)               
                zz7.sendText(msg)
                

 
            elif msg.text in ["List group"]:
                    gid = zz7.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = zz7.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    zz7.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = zz7.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = zz7.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    zz7.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    zz7.sendText(msg.to, "Khusus Admin")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        zz7.sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +zz7.getGroup(gid).name + "\n"
                        zz7.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    zz7.sendText(msg.to, "Khusus Admin")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if zz7.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    zz7.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    zz7.sendText(msg.to, "Khusus Admin")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = zz7.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = zz7.getGroup(i).name
		            if h == ng:
		                zz7.inviteIntoGroup(i,[Creator])
			        zz7.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        zz7.sendText(msg.to,"Khusus Admin")
		except Exception as e:
		    zz7.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = zz7.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = zz7.getGroup(i).name
		        if h == ng:
			    zz7.sendText(i,"Combat Di Paksa Keluar Oleh Owner!")
		            zz7.leaveGroup(i)
			    zz7.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    zz7.sendText(msg.to,"Khusus Admin")
 
	    elif "Leave all group" == msg.text:
		gid = zz7.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			zz7.sendText("Combat Di Paksa Keluar Oleh Owner!")
		        zz7.leaveGroup(i)
		    zz7.sendText(msg.to,"Success Leave All Group")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = zz7.getGroupIdsJoined()
                for i in gid:
                    h = zz7.getGroup(i).name
                    gna = zz7.getGroup(i)
                    if h == saya:
                        zz7.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = zz7.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        zz7.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        zz7.sendText(msg.to,"Tidak Ada Yang Pending")
                else:
                    zz7.sendText(msg.to,"Tidak Bisa Digunakan Diluar Group")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = zz7.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    zz7.updateGroup(X)
                    zz7.sendText(msg.to,"Url Sudah Aktif")
                else:
                    zz7.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = zz7.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    zz7.updateGroup(X)
                    zz7.sendText(msg.to,"Url Sudah Di Nonaktifkan")

                else:
                    zz7.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    zz7.sendText(msg.to,"Auto Join Sudah Aktif")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    zz7.sendText(msg.to,"Auto Join Sudah Di Nonaktifkan")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    zz7.sendText(msg.to,"Auto Join Cancel Sudah Aktif")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    zz7.sendText(msg.to,"Auto Join Cancel Sudah Di Nonaktifkan")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")		    
		    
 
            elif msg.text in ["R1 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    zz7.sendText(msg.to,"Auto R1 Sudah Aktif")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["R1 off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    zz7.sendText(msg.to,"Auto R1 Sudah Off")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")	
		    
		    
            elif msg.text in ["R2 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    zz7.sendText(msg.to,"Auto R2 Sudah Aktif")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")
            elif msg.text in ["R2 off"]:
		if msg.from_ in admin:
                    wait["detectMention2"] = False
                    zz7.sendText(msg.to,"Auto R2 Sudah Off")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")	
		    

            elif msg.text in ["R3 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    zz7.sendText(msg.to,"Auto R3 Sudah Aktif")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["R3 off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    zz7.sendText(msg.to,"Auto R3 Sudah Off")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")	
		    
 
            elif msg.text in ["Rkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False                    
                    zz7.sendText(msg.to,"Auto R Kick Sudah Aktif")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Rkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    zz7.sendText(msg.to,"Auto R Kick Sudah Off")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")			  
		    
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                zz7.sendText(msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    zz7.sendText(msg.to,"Khusus Admin")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                zz7.sendText(msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    zz7.sendText(msg.to,"Khusus Admin")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                zz7.sendText(msg.to,"Invite Protect Sudah Aktif")
		print wait["inviteprotect"]
	     else:
		    zz7.sendText(msg.to,"Khusus Admin")		

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                zz7.sendText(msg.to,"Invite Protect Sudah Di Nonaktifkan")
		print wait["inviteprotect"]
	     else:
		    zz7.sendText(msg.to,"Khusus Admin")		    

	    elif "Qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"] = True
	    	zz7.sendText(msg.to,"QR Protect Sudah Aktif")
	     else:
		    zz7.sendText(msg.to,"Khusus Admin")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"] = False
	    	zz7.sendText(msg.to,"Qr Protect Sudah Di Nonaktifkan")
	     else:
		    zz7.sendText(msg.to,"Khusus Admin")	    	

                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     zz7.sendText(msg.to,"Auto Kick Sudah Aktif")
	     else:
	        zz7.sendText(msg.to,"Khusus Admin")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     zz7.sendText(msg.to,"Auto Kick Sudah Di Nonaktifkan")
	     else:
	        zz7.sendText(msg.to,"Khusus Admin")	     


            elif msg.text in ["Allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    zz7.sendText(msg.to,"All Protect Sudah Aktif Semua")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    zz7.sendText(msg.to,"All Protect Sudah Di Nonaktifkan Semua")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                zz7.sendText(msg.to,"Contact Sudah Aktif")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                zz7.sendText(msg.to,"Contact Sudah Di Nonaktifkan")
                

            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                zz7.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                zz7.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")                


            elif msg.text in ["Notif on"]:
                if wait["Notif"] == True:
                    if wait["lang"] == "JP":
                        zz7.sendText(msg.to,"Notif Di Aktifkanヾ(*´∀｀*)ﾉ")
                else:
                    wait["Notif"] = True
                    if wait["lang"] == "JP":
                        zz7.sendText(msg.to,"Sudah Onヽ(´▽｀)/")

            elif msg.text in ["Notif off"]:
                if wait["Notif"] == False:
                    if wait["lang"] == "JP":
                        zz7.sendText(msg.to,"Notif Di Nonaktifkan(　＾∇＾)")
                else:
                    wait["Notif"] = False
                    if wait["lang"] == "JP":
                        zz7.sendText(msg.to,"Sudah Off(p′︵‵。)")
                        
                        
            elif "Dooorrrr" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                zz7.sendText(msg.to,"Ngintip nih....!!!!!")
				
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                zz7.sendText(msg.to,"Siap Lempar Bata Si Tukang Ngintip")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    zz7.sendText(msg.to, "Cek Sider Off")
                else:
                    zz7.sendText(msg.to, "Set Dulu Boss")                         


            elif msg.text in ["Settings","Status"]:
                md = ""
		if wait["Notif"] == True: md+="┣🇮🇩━⏩✔️ Notif : On\n"
		else:md+="┣🇮🇩━⏩✖ Notif : Off\n"
		if wait["AutoJoin"] == True: md+="┣🇮🇩━⏩✔️ Auto Join : On\n"
                else: md +="┣🇮🇩━⏩✖ Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="┣🇮🇩━⏩✔️ Auto Join Cancel : On\n"
                else: md +="┣🇮🇩━⏩✖ Auto Join Cancel : Off\n"                
		if wait["Contact"] == True: md+="┣🇮🇩━⏩✔️ Info Contact : On\n"
		else: md+="┣🇮🇩━⏩✖ Info Contact : Off\n"
                if wait["AutoCancel"] == True:md+="┣🇮🇩━⏩✔️ Auto Cancel : On\n"
                else: md+= "┣🇮🇩━⏩✖ Auto Cancel : Off\n"
                if wait["inviteprotect"] == True:md+="┣🇮🇩━⏩✔️ Invite Protect : On\n"
                else: md+= "┣🇮🇩━⏩✖ Invite Protect : Off\n"                
		if wait["Qr"] == True: md+="┣🇮🇩━⏩✔️ Qr Protect : On\n"
		else:md+="┣🇮🇩━⏩✖ Qr Protect : Off\n"
		if wait["AutoKick"] == True: md+="┣🇮🇩━⏩✔️ Auto Kick : On\n"
		else:md+="┣🇮🇩━⏩✖ Auto Kick : Off\n"
		if wait["alwaysRead"] == True: md+="┣🇮🇩━⏩✔️ Always Read : On\n"
		else:md+="┣🇮🇩━⏩✖ Always Read: Off\n"
		if wait["detectMention"] == True: md+="┣🇮🇩━⏩✔️ Auto R1 : On\n"
		else:md+="┣🇮🇩━⏩✖ Auto R1 : Off\n"		
		if wait["detectMention2"] == True: md+="┣🇮🇩━⏩✔️ Auto R2 : On\n"
		else:md+="┣🇮🇩━⏩✖ Auto R2 : Off\n"	
		if wait["detectMention3"] == True: md+="┣🇮🇩━⏩✔️ Auto R3 : On\n"
		else:md+="┣🇮🇩━⏩✖ Auto R3 : Off\n"			
		if wait["kickMention"] == True: md+="┣🇮🇩━⏩✔️ Auto R Kick : On\n"
		else:md+="┣🇮🇩━⏩✖ Auto R Kick : Off\n"				
		if wait["Sider"] == True: md+="┣🇮🇩━⏩✔️ Auto Sider : On\n"
		else:md+="┣🇮🇩━⏩✖ Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="┣🇮🇩━⏩✔️ Simisimi : On\n"
		else:md+="┣🇮🇩━⏩✖ Simisimi: Off\n"		
                zz7.sendText(msg.to,"╭━━━━━━━━━━━━━━━━━━━━╮\n""│♠✴ SETTINGS ✴♠\n""│━━━━━━━━━━━━━━━━━━━━\n"+md+"╰━━━━━━━━━━━━━━━━━━━━╯")


            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                zz7.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = zz7.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    zz7.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    zz7.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = zz7.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    zz7.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    zz7.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = zz7.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    zz7.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    zz7.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = zz7.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    zz7.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    zz7.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = zz7.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    zz7.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    zz7.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = zz7.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    zz7.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    zz7.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = zz7.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    zz7.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    zz7.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = zz7.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    zz7.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    zz7.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = zz7.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    zz7.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    zz7.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = zz7.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    zz7.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    zz7.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)
                

            elif "tag all" == msg.text.lower():
                 group = zz7.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 zz7.sendMessage(cnt)
                 
            elif "tagall" == msg.text.lower():
                 group = zz7.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 zz7.sendMessage(cnt)                 


            elif msg.text in ["Setview","Setpoint","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                zz7.sendText(msg.to, "♠Checkpoint Checked♠")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Ciduk","Cyduk"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = zz7.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╭━━━━━━━━━━━━━━━━━━━━╮\n│     ♠✴ LIST VIEWERS ✴♠\n│━━━━━━━━━━━━━━━━━━━━\n┣🇮🇩━⏩"
                        grp = '\n┣🇮🇩━⏩ '.join(str(f) for f in dataResult)
                        total = '\n│━━━━━━━━━━━━━━━━━━━━\n┣🇮🇩━⏩ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╰━━━━━━━━━━━━━━━━━━━━╯"
                        zz7.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        zz7.sendText(msg.to, "♠Auto Checkpoint♠")                        
                    else:
                        zz7.sendText(msg.to, "♠Belum Ada Viewers♠")
                    print "Viewseen"


	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    zz7.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    zz7.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = zz7.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    zz7.findAndAddContactsByMids(mi_d)
		    zz7.sendText(msg.to,"Success Add all")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                zz7.sendText(msg.to,"Send Contact")
                
                

            elif msg.text in ["Autolike"]:
                wait["likeOn"] = True
                zz7.sendText(msg.to,"Sudah on")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                zz7.sendText(msg.to,"Send Contact")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                zz7.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Copycontact"]:
                wait["copy"] = True
                zz7.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Sticker on"]:
                wait["sticker"] = True
                zz7.sendText(msg.to,"Sticker ID Detect Already On.")  
                
            elif msg.text in ["Bot off"]:
                wait["Bot"] = False
                zz7.sendText(msg.to,"Bot Sudah Di Nonaktifkan.")  

	    elif "Recover" in msg.text:
		thisgroup = zz7.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		zz7.createGroup("Recover", mi_d)
		zz7.sendText(msg.to,"Success recover")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = zz7.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    zz7.updateGroup(X)
                else:
                    zz7.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    zz7.kickoutFromGroup(msg.to,[midd])
		else:
		    zz7.sendText(msg.to,"Admin Detected")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                zz7.findAndAddContactsByMid(midd)
                zz7.inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "uc889c1f8f74274f117e0a0d69ccc559c"
                zz7.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = zz7.getGroup(msg.to)
                zz7.sendText(msg.to,"Selamat Datang Di "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                zz7.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = zz7.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			zz7.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/ricco1311")
		    zz7.sendText(msg.to,"Success BC BosQ")
		else:
		    zz7.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Cancel"]:
                gid = zz7.getGroupIdsInvited()
                for i in gid:
                    zz7.rejectGroupInvitation(i)
                zz7.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = zz7.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        zz7.updateGroup(x)
                    gurl = zz7.reissueGroupTicket(msg.to)
                    zz7.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        zz7.sendText(msg.to,"Can't be used outside the group")
                    else:
                        zz7.sendText(msg.to,"Not for use less than group")


            elif msg.text in ["timeline"]:
		try:
                    url = zz7.activity(limit=5)
		    zz7.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["@bye","@Bye"]:
		    zz7.leaveGroup(msg.to)		    
		    

            elif msg.text in ["Absen"]:
		zz7.sendText(msg.to,"Hadir!!")


            elif msg.text.lower() in ["respon"]:
                zz7.sendText(msg.to,responsename)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		zz7.sendText(msg.to, "Progress...")
                zz7.sendText(msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["Speed test"]:
                start = time.time()
                zz7.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                zz7.sendText(msg.to, "%sseconds" % (elapsed_time))                
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    zz7.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    zz7.sendText(msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = zz7.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        zz7.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    zz7.sendText(msg.to,"Succes BosQ")
                                except:
                                    zz7.sendText(msg.to,"Error")
			    else:
				zz7.sendText(msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    zz7.sendText(msg.to,"Tidak Ada")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +zz7.getContact(mi_d).displayName + "\n"
                    zz7.sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = zz7.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        zz7.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                zz7.sendText(msg.to,"Succes BosQ")
                            except:
                                zz7.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    zz7.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All Success❉ ┐") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = zz7.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            zz7.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            zz7.kickoutFromGroup(msg.to,[jj])
                        zz7.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    zz7.sendText(msg.to, "Khusus creator")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = zz7.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            zz7.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                zz7.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Kickall" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = zz7.getGroup(msg.to)
                        zz7.sendText(msg.to,"Dadaaah~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            zz7.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        zz7.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        zz7.sendText(msg.to,str(e))
			    zz7.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    zz7.sendText(msg.to, "Reload Boss...")
		    restart_program()
		    print "@Restart"
		else:
		    zz7.sendText(msg.to, "No Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Crash' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "zz7,'"}
                zz7.sendMessage(msg)

 
            elif "copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = zz7.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       zz7.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               zz7.CloneContactProfile(target)
                               zz7.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Mybackup"]:
                try:
                    zz7.updateDisplayPicture(backup1.pictureStatus)
                    zz7.updateProfile(backup1)
                    zz7.sendText(msg.to, "Done (^_^)")
                except Exception as e:
                    zz7.sendText(msg.to, str(e))

 
	    elif "musik " in msg.text:
					songname = msg.text.replace("musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						zz7.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						zz7.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						zz7.sendAudioWithURL(msg.to,abc)
						zz7.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	
            elif 'lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        zz7.sendText(msg.to, hasil)
                except Exception as wak:
                        zz7.sendText(msg.to, str(wak))
             
            
            
            elif "Fancytext " in msg.text:
                    txt = msg.text.replace("Fancytext ", "")
                    zz7.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = zz7.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        zz7.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = zz7.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                zz7.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                zz7.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = zz7.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        zz7.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = zz7.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                zz7.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                zz7.sendText(msg.to,"Upload image failed.")
                                
            elif "Cpp" in msg.text:
                if msg.from_ in admin:
                    path = "zz7.jpg"
                    zz7.sendText(msg.to,"Update PP :")
                    zz7.sendImage(msg.to,path)
                    zz7.updateProfilePicture(path)                                
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = zz7.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        zz7.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = zz7.getContact(target)
                                zz7.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                zz7.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = zz7.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        zz7.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = zz7.getContact(target)
                                zz7.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                zz7.sendText(msg.to,"Upload image failed.")

            elif msg.text.lower() in ["pap owner","pap creator"]:
                                link = ["http://dl.profile.line-cdn.net/0hFR-rB8h-GX0QCzWZMOZmKixOFxBnJR81aG9eSTUNREhtOVYqJWgFSWYDR05vOwp7K2sCGTELRUVo"]
                                pilih = random.choice(link)
                                zz7.sendImageWithURL(msg.to,pilih)

 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 10
                  while(t):
                    zz7.sendText(msg.to, (bctxt))
                    t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = zz7.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      zz7.sendText(manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = zz7.getAllContactIds()
                  for manusia in orang:
                    zz7.sendText(manusia, (broadcasttxt))

 
            elif 'ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    tj = text1[0].replace("s150x150/","")
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    zz7.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    zz7.sendImageWithURL(msg.to, tj)
                except Exception as njer:
                	zz7.sendText(msg.to, str(njer))
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                zz7.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                zz7.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtube ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    zz7.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    zz7.sendText(msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        zz7.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        zz7.sendText(msg.to, "Could not find it")                    

 
            elif "Say " in msg.text:
                say = msg.text.replace("Say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                zz7.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                zz7.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                zz7.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = zz7.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                zz7.sendAudio(msg.to,"hasil.mp3")
                
            elif "lurk on" == msg.text.lower():
               #if msg.from_ in admin:
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         zz7.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     zz7.sendText(msg.to, "Set the lastseens' point (｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2


            elif "lurk off" == msg.text.lower():
               #if msg.from_ in admin:
                if msg.to not in wait2['readPoint']:
                    zz7.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    zz7.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))



                    
            elif "lurkers" == msg.text.lower():
            	#if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             zz7.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = zz7.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+ "@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          zz7.sendMessage(msg)
                          zz7.sendText(msg.to, "Jika sudah lihat sider please\ntulis lurk on lagi kak  (｀・ω・´)\n \n"  +  datetime.now().strftime('%H:%M:%S'))
                        except Exception as error:
                              print error
                        pass
               
                    else:
                        zz7.sendText(msg.to, "Lurking has not been set (｀・ω・´)\n \n"  +  datetime.now().strftime('%H:%M:%S'))    


            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    beb = "Hi Sayang 😘 " +zz7.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    zz7.sendText(msg.to,beb)



            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                zz7.sendText(msg.to,"Sedang Mencari...")
                zz7.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                zz7.sendText(msg.to,"Tuh Linknya Kak (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = zz7.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        zz7.sendText(msg.to, g.mid)
                    else:
                        pass


            elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = zz7.getProfile()
                        profile.statusMessage = string
                        zz7.updateProfile(profile)
                        zz7.sendText(msg.to,"Done")

            elif "Myname " in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = zz7.getProfile()
                        profile.displayName = string
                        zz7.updateProfile(profile)
                        zz7.sendText(msg.to,"Done")



            elif msg.text.lower() in ["mymid","myid"]:
                middd = "Name : " +zz7.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                zz7.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                zz7.sendMessage(msg)

            elif msg.text in ["Kibaran","MY FAMS"]:
                msg.contentType = 13
                fams2 = "u1dcc9fd3de21d87b9b01440039080197"
                fams3 = "uc00a7fc61069447f8db907f40233fb34"
		fams5 = "u5680d1c1857163e9d1372a40b18c587a"
                fams6 = "u99dcaf1d99afe1d62e00a211fc4e0bf1"
                fams7 = "u97ed2dd962d224b28b9265f340e6cf25"
                fams8 = "u67ef3bc0f0550e849aa2ea7f9663aa0d"
		fams9 = "u0b7a8ac8254b3014c804504b2e94eeb7"
                fams10 = "u253e095ced2a07385357925287a04c75"
                msg.contentMetadata = {'mid': vip}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': fams2}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': fams3}
                random.choice(KAC).sendMessage(msg)
		msg.contentMetadata = {'mid': fams5}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': fams6}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': fams7}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': fams8}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': fams9}
                random.choice(KAC).sendMessage(msg)
		msg.contentMetadata = {'mid': fams10}
                random.choice(KAC).sendMessage(msg)
		random.choice(KAC).sendText(msg.to,"👽LOE SONGONG BERARTI LOE ANCUR👽")
		
            elif "apakah " in msg.text:
                apk = msg.text.replace("apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                zz7.sendAudio(msg.to,"hasil.mp3")
                
            elif "hari " in msg.text:
                apk = msg.text.replace("hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                zz7.sendAudio(msg.to,"hasil.mp3")   


            elif "berapa " in msg.text:
                apk = msg.text.replace("berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                zz7.sendAudio(msg.to,"hasil.mp3")
                
            elif "berapakah " in msg.text:
                apk = msg.text.replace("berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                zz7.sendAudio(msg.to,"hasil.mp3")                

            elif "kapan " in msg.text:
                apk = msg.text.replace("kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                zz7.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                zz7.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                zz7.sendText(msg.to,"Simisimi Di Nonaktifkan")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    zz7.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtubesearch ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        zz7.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                zz7.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                zz7.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                zz7.sendText(msg.to, A)                

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                zz7.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                zz7.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                zz7.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                zz7.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = zz7.getAllContactIds()
                kontak = zz7.getContacts(contactlist)
                num=1
                msgs="━━━━━━━━━List Friend━━━━━━━━━"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n━━━━━━━━━List Friend━━━━━━━━━\n\nTotal Friend : %i" % len(kontak)
                zz7.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = zz7.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="━━━━━━━━━List Member━�����━━━━━━━-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n━━━━━━━━━List Member━━━━━━━━━\n\nTotal Members : %i" % len(group)
                zz7.sendText(msg.to, msgs)

            

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = zz7.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    zz7.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = zz7.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            zz7.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = zz7.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                zz7.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = zz7.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                zz7.sendText(msg.to,path)
 
            elif "Name" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = zz7.getContact(key1)
                cu = zz7.channel.getCover(key1)
                try:
                    zz7.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    zz7.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Profile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = zz7.getContact(key1)
                cu = zz7.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    zz7.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    zz7.sendText(msg.to,"Profile Picture " + contact.displayName)
                    zz7.sendImageWithURL(msg.to,image)
                    zz7.sendText(msg.to,"Cover " + contact.displayName)
                    zz7.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Contact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = zz7.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                zz7.sendMessage(msg)

            elif "Info" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = zz7.getContact(key1)
                cu = zz7.channel.getCover(key1)
                try:
                    zz7.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    zz7.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Bio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = zz7.getContact(key1)
                cu = zz7.channel.getCover(key1)
                try:
                    zz7.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    zz7.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                zz7.sendText(msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                zz7.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                zz7.sendText(msg.to, rst)                
                 
                
            elif "SearchID " in msg.text:
                userid = msg.text.replace("SearchID ","")
                contact = zz7.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                zz7.sendMessage(msg)
                
            elif "Searchid " in msg.text:
                userid = msg.text.replace("Searchid ","")
                contact = zz7.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                zz7.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        zz7.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        zz7.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        zz7.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto ","")
                    if gid == "":
                        zz7.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            zz7.findAndAddContactsByMid(msg.from_)
                            zz7.inviteIntoGroup(gid,[msg.from_])
                        except:
                            zz7.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                zz7.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = zz7.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "┣🇮🇩━⏩" + "%s\n" % (zz7.getGroup(i).name +" ~> ["+str(len(zz7.getGroup(i).members))+"]")
                zz7.sendText(msg.to,"╭━━━━━━━━━━━━━━━━━━━━╮\n│      ♠✴ LIST GROUPS✴♠\n│━━━━━━━━━━━━━━━━━━━━\n" + h + "│━━━━━━━━━━━━━━━━━━━━" + "\n│ Total Groups =" +" ["+str(len(gid))+"]\n╰━━━━━━━━━━━━━━━━━━━━╯")

            elif msg.text in ["Glistmid"]:   
                gruplist = zz7.getGroupIdsJoined()
                kontak = zz7.getGroups(gruplist)
                num=1
                msgs="━━━━━━━━━List GrupMid━━━━━━━━━"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n━━━━━━━━━List GrupMid━━━━━━━━━\n\nTotal Grup : %i" % len(kontak)
                zz7.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    zz7.sendText(msg.to,"Sedang Mencari...")
                    zz7.sendText(msg.to, "https://www.google.com/" + b)
                    zz7.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        zz7.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = zz7.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            zz7.sendText(msg.to,h)
                        except Exception as error:
                            zz7.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = zz7.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                zz7.rejectGroupInvitation(i)
                            except:
                                zz7.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        zz7.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        zz7.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = zz7.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = zz7.getGroup(i)
                            _list += gids.name
                            zz7.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        zz7.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        zz7.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  


            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                zz7.sendGifWithURL(msg.to,gore)
                

                
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        zz7.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        zz7.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        zz7.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        zz7.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            zz7.sendText(msg.to,"Nothing")
                        else:
                            mc = "Target Mimic User:\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+zz7.getContact(mi_d).displayName + "\n"
                            zz7.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                zz7.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                zz7.sendText(msg.to,"Mimic change to target")
                            else:
                                zz7.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        zz7.sendText(msg.to,"Reply Message on")
                    else:
                        zz7.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        zz7.sendText(msg.to,"Reply Message off")
                    else:
                        zz7.sendText(msg.to,"Sudah off")



        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = zz7.fetchOps(zz7.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(zz7.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            zz7.Poll.rev = max(zz7.Poll.rev, Op.revision)
            bot(Op)

