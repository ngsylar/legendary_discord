from replit import db
import re

# banco de dados do servidor
class GuildDB:
  def __init__(self):
    self.whoami = 'Think of me as Yoda, only instead of being little and green, I\'m a bot and I\'m awesome. I\'m your bro: I\'m Broda!'
    self.challenge = 'Challenge accepted!'
    self.sorry = 'I\'m sorry, I can\'t hear you over the sound of how awesome I am.'
    self.sometimes = 'Sometimes we search for one thing but discover another.'
    self.awesome = 'challenge accepted!'
    self.legendary = [
      'believe it or not, you was not always as awesome as you are today.',
      'you poor thing. Having to grow up in the Insula, with the Palace right there.',
      'to succeed you have to stop to be ordinary and be legen — wait for it — dary! Legendary!',
      'when you get sad, just stop being sad and be awesome instead.',
      'if you have a crazy story, I was there. It\'s just a law of the universe.',
      'I believe you and I met for a reason. It\'s like the universe was saying, \"Hey Legendary, there\'s this dude, he\'s pretty cool, but it is your job to make him awesome\".',
      'without me, it’s just aweso.'
    ]

  def update_sch(self, guild_id, msg):
    if guild_id not in db.keys():
      db[guild_id] = {}
    guild_db = db[guild_id]

    msg_has_channel = re.match('legen!sch[ ]+<#[0-9]{18}>[ ]*$', msg)
    
    if msg_has_channel:
      secret_channel_id = msg.split('<#',1)[1].split('>',1)[0]
      
      guild_db['sch'] = secret_channel_id
      db[guild_id] = guild_db
      self.operationStatus = self.challenge
    
    elif 'sch' in guild_db:
      self.operationStatus = '<#'+guild_db['sch']+'> \u27F5 The Secret Channel'
    else:
      self.operationStatus = self.sorry

  def delete_sch(self, guild_id):
    if guild_id in db.keys():
      guild_db = db[guild_id]
      
      if 'sch' in guild_db:
        del guild_db['sch']
        db[guild_id] = guild_db
        self.operationStatus = self.challenge
      
      else:
        self.operationStatus = self.sorry
    else:
      self.operationStatus = self.sorry
