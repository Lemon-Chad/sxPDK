import discord
from discord.ext import commands

def pluginLoaded(pl,bot):
    async def predicate(ctx):
        if 'loadedPlugins' not in bot[str(ctx.guild.id)]:
            bot[str(ctx.guild.id)]['loadedPlugins'] = {'ids': []}
        return pl in bot[str(ctx.guild.id)]["loadedPlugins"]["ids"]
    return commands.check(predicate)

def eventPluginLoaded(pl,bot,guild):
  if 'loadedPlugins' not in bot[str(guild)]:
      bot[str(guild)]['loadedPlugins'] = {'ids': []}
  return pl in bot[str(guild)]["loadedPlugins"]["ids"]

class achievement():
  def __init__(self,guildId,bot,aid):
    self.achievement = bot[str(guildId)]["achievements"][aid]
    self.action = self.achievement["action"]
    self.subaction = self.achievement["subaction"]
    self.goal = self.achievement["goal"]
    self.description = self.achievement["description"]
    self.reward = self.achievement["reward"]
    self.title = self.achievement["title"]
    self.rewardCount = self.achievement["rewardCount"]

def createPluginData(guildId,plugin,bot,data={}):
  if 'loadedPlugins' not in bot[str(guildId)]:
      bot[str(guildId)]['loadedPlugins'] = {'ids': []}
  bot[str(guildId)]["loadedPlugins"][plugin] = data

def getPlugin(guildId,plugin,bot):
  if 'loadedPlugins' not in bot[str(guildId)]:
      bot[str(guildId)]['loadedPlugins'] = {'ids': []}
  return bot[str(guildId)]["loadedPlugins"][plugin]

def getAchievements(guildId,bot):
  return bot[str(guildId)]["achievements"]["ids"]

def getTeams(guildId,bot):
  return bot[str(guildId)]["teamids"]

class user():
  def __init__(self,guildId,userId,bot):
    self.id=userId
    self.user = bot[str(guildId)][str(userId)]

    self.bits = self.user["bits"]

    self.team = self.user["team"]

    self.xp = self.user["xp"]
    self.level = self.user["level"]

    self.inventory = self.user["inventory"]
    self.itemIds = self.inventory["ids"]
    self.items = self.inventory["items"]
    self.consumables = self.inventory["consumables"]

    self.achievements = self.user["achievements"]

  def addData(self,name,data):
    self.user[name] = data
    d = self.user[name]
    setattr(self, name, d)
    

  def getItem(self,iid):
    return self.items[iid]

  def addItem(self,iid,category=["none"],count=1,consumable=False,consumableTrait="none"):
    self.itemIds.append(iid)
    if isinstance(category,list):
      self.items[iid] = {"count":count,"category":category}
    else:
      self.items[iid] = {"count":count,"category":[category]}
    if consumable == True and consumableTrait != "none":
      self.consumables[iid] = consumableTrait

  def removeItem(self,iid,count=1):
    target = self.items[iid]
    if target["count"] <= count:
      self.itemIds.remove(iid)
      del self.items[iid]
    else:
      target["count"] -= count

  
  def getAchievement(self, aid):
    return self.achievements[aid]
  
  def progressAchievement(self, aid, amount=1):
    self.achievements[aid]["progress"] += amount

def newAchievement(guildId,bot,achievementId,action,subaction,goal,reward,rewardCount,title,description=""):
  bot[str(guildId)]['achievements'][achievementId] = {'action':action,'subaction':subaction,'goal':goal,'description':description,'reward':reward,'title':title,'rewardcount':rewardCount}
  bot[str(guildId)]['achievements']['ids'].append(achievementId)

class team():
  def __init__(self,guildId,team,bot):
    self.team = bot[str(guildId)]["teams"][team]
    self.points = self.team["points"]
    self.leader = None if not self.team['captain_id'] else user(str(guildId), self.team['captain_id'], bot)
    self.worth = 0
    self.role = self.team["role_needed"]
    self.members = [user(str(guildId), member, bot) for member in self.team["members"]]
    for member in self.members: 
        self.worth += member.bits
