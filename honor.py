import hashlib

import willie

def setup(bot):
    if not bot.memory.contains('honor'):
        bot.memory['honor'] = willie.tools.WillieMemory()
        bot.memory['honor'] = [ 'bacon', 'sweet tea', 'worfbot', 'god', 'mogh', 'gimli', 'moghbot', 'william riker', 'mstark', 'namer98', 'i can', 'aragorn, son of arathorn', 'captain picard', 'jean luc picard', 'jesus', 'gimli, son of gloin', 'blood wine', 'worf', 'commander riker', 'sweetened iced tea', 'st. thomas aquinas', 'aragorn', 'jesus christ' ]
    if not bot.memory.contains('dishonor'):
        bot.memory['dishonor'] = willie.tools.WillieMemory()
        bot.memory['dishonor'] = [ 'eclipse', 'wasp', 'romulans', 'wasps', 'optimum', 'cheating', 'dishonor', 'lucifer', 'satan', 'deanna troi', 'quark', 'house of durasbot', 'house of duras', 'duras', 'com', 'lwaxana troi', 'durasbot' ]

@willie.module.commands('honor')
@willie.module.example('.honor')
def honor(bot, trigger):
    '''Check whether something (or someone) is honorable'''
    if not trigger.group(2):
        topic = trigger.nick
    else:
        topic = trigger.group(2)
    say_honor(bot, topic.lower().strip())

def say_honor(bot, topic):
    if topic in bot.memory['honor']:
        bot.say(topic + ' has honor')
    elif topic in bot.memory['dishonor']:
        bot.say(topic + ' is without honor')
    else:
        hasher = hashlib.md5()
        hasher.update(topic)
        if hasher.hexdigest()[-1] in ['0', '1', '2', '3', '4', '5', '6', '7']:
            bot.say(topic + ' has honor')
        else:
            bot.say(topic + ' is without honor')

@willie.module.commands('add')
@willie.module.example('.add Worf:honorable')
@willie.module.example('.add Worf and his family:Honorable')
def add_phrase(bot, trigger):
    ''' Specifies whether a phrase is honorable or not. This command may only be run by an admin!'''
    if not trigger.admin:
        return
    args = trigger.group(2).split(':')
    if len(args) != 2:
        return
    phrase = args[0].strip().lower()
    value = args[1].strip().lower()
    if value == 'honorable':
        if phrase not in bot.memory['honor']:
            bot.memory['honor'].append(phrase)
        if phrase in bot.memory['dishonor']:
            bot.memory['dishonor'].remove(phrase)
        bot.say('Got it: ' + args[0] + ' is honorable.')
    elif value == 'dishonorable':
        if phrase not in bot.memory['dishonor']:
            bot.memory['dishonor'].append(phrase)
        if phrase in bot.memory['honor']:
            bot.memory['honor'].remove(phrase)
        bot.say('Got it: ' + args[0] + ' is dishonorable.')
