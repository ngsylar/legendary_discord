from replit import db

# banco de dados do servidor
class GuildDB:
  def get_gid_gdb_sch (self, msg, bot=None):
    self.gid = str(msg.guild.id)
    self.sch = None

    if self.gid not in db.keys():
      db[self.gid] = {}
    self.gdb = db[self.gid]

    if bot and ('sch' in self.gdb):
      self.sch = bot.get_channel(int(self.gdb['sch']))

  def update_sch (self, msg, cmd):
    self.get_gid_gdb_sch(msg)
    msg_contains_channel = cmd.match(r'<#[0-9]{18}>', msg, cmd.AND_DESCRIPTION)

    if msg_contains_channel:
      secret_channel_id = msg.content.split('<#',1)[1].split('>',1)[0]      
      self.gdb['sch'] = secret_channel_id
      db[self.gid] = self.gdb
    
    if 'sch' in self.gdb:
      self.queryResult = self.gdb['sch']
    else:
      self.queryResult = None

  def remove_record (self, msg, cmd):
    self.op_was_successful = False
    
    self.get_gid_gdb_sch(msg)
    msg_contains_sch = cmd.match('sch', msg, cmd.AND_DESCRIPTION)

    if msg_contains_sch:
      if 'sch' in self.gdb:
        del self.gdb['sch']
        db[self.gid] = self.gdb
        self.op_was_successful = True