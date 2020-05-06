import discord
from discord.ext import commands

def pluginLoaded(pl):
    async def predicate(ctx):
        return pl in bot[str(ctx.guild.id)]["loadedPlugins"]["ids"]
    return commands.check(predicate)

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
  bot[str(guildId)]["loadedPlugins"][plugin] = data

def getPlugin(guildId,plugin,bot):
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
  

class team():
  def __init__(self,guildId,team,bot):
    self.team = bot[str(guildId)]["teams"][team]
    self.points = self.team["points"]