from config import price
from peewee import *
import datetime
 


db = SqliteDatabase('db.sqlite3')

class BaseModel(Model):
	class Meta:
		database = db

class Routing(BaseModel):
	btn 	 	= TextField(unique = True) 
	action		= TextField(null = True)

	@staticmethod
	def clear_table():
		Routing.create_table(fail_silently = True)
		q = Routing.delete()
		q.execute()


class Btn():
	def __init__(self):
		self.free_signals 		= "🗣Переговорная🗣"
		self.vip_signals		= "👑Подписка👑"
		self.balance_and_wallet	= "💰Мой кошелёк 🏦"
		self.referal 			= "🔄💰 Реферальная программа 🔄💳"
		self.three_days 		= "3 дня за {} Btc".format(price['3_days'])
		self.one_week 			= "1 неделя за {} Btc".format(price['1_week'])
		self.two_weeks 			= "2 недели за {} Btc".format(price['2_weeks'])
		self.one_month 			= "1 месяц за {} Btc".format(price['1_month'])
		self.back 				= "Назад"

		self.set_routing()

	def set_routing(self):
		btns = self.__dict__
		Routing.clear_table()
		for b in btns:
			r = Routing.create(btn = btns[b], action = b)



#	BUTTONS



# CALLBACKS
# free_signals_clbck 	= "free_signals"
# vip_signals_clbck	= "vip_signals"
# my_balance_clbck	= "my_balance"
# my_wallet_clbck		= "my_wallet"
# one_day_clbck		= "one_day"
# three_days_clbck	= "three_days"	
# one_week_clbck		= "one_week"
# one_month_clbck		= "one_month"


class Msg():
	def __init__(self):
		self.start = '''
		Прекрасно! 
		Вы переходите на канал сигналов с биржи Bittrex. Данный канал ведет биржевой аналитик @mihail, 
		который ежедневно делится своим мнением о ситуации на рынке, и дает рекомендации по разным валютам.
		Здесь подскажут на чем заработать.
		'''

		self.balance_and_wallet = '''
		Адрес вашего кошелька {}.
		Переведите необходимую сумму btc на этот кошелек. 
		ВНИМАНИЕ! Средства зачисляются спустя 3 подтверждения сети. 
		После получения подтверждений на вашем балансе отобразятся перечисленные средства. 
		Вам остается лишь выбрать необходимый период доступа к сервису! Ссылка придет автоматически!

		Ваш баланс составляет {} BTC.
		Скидка на следующую подписку составит {}%.
		'''

		self.wallet_address = '```{}```'	

		self.free_signals = '''
		Ознакомьтесь с результатами игры по сигналам группы за прошлый месяц:
		NXC 80%; BRK 107%; SNRG 70%; HKG 70%; GLD 70%; NEO168%; DAR 91%; QWARK 176%; XCP 85%; GCR 60%; THC 53%; XRP 62%; FLDC 77%; LSK 157%; QTUM 67%; MCO 102%; XVG 78%; KORE 330%; OMG 102%; PTOY 76%; NEO 73%; IOP 54%; ZEC 101%; ADX 117%; XLM 83%
		Присоединяйтесь к группе Профессионалов и наращивайте количество Биткойна на своем счету. 
			
		Ссылка: https://t.me/pump_inside 
		'''

		self.vip_signals = '''
		Добро пожаловать!
   
		Рады сообщить вам, что начиная с Октября 2017г. в нашем канале публикуется информация от очень сильных Источников, от Китов мира криптовалюты.. 
		Все сигналы высоко-профитные, но результативность зависит от многих факторов, в том числе от опыта пользователя.
		ВНИМАНИЕ!!! Администрация канала не несет ответственности за возможные убытки пользователей. Все действия пользователи осуществляют на свой страх и риск и по своему личному усмотрению.
		Желаем Профитов!
		'''

		self.access_to_chat = '''
		Пополните свой баланс на необходимое количество BTC и Вы получите доступ в чат
		'''

		self.repare = 'Оплата пока на ремонте. Скоро всё будет'

		self.access_granted = '''Оплата произведена. Теперь чат доступен для Вас по ссылке https://t.me/vip_signal_Bittrex
		Доступ оплачен до {} {}, {}
		'''

		self.not_enough_money = '''Оплата не произведена. На Вашем счёте недостаточно средств.'''

		self.select_action = 'Выберите действие:'

		self.subscription_ended = 'Подписка на канал VIP сигналов истекла. Чтобы продлить подписку пополните счёт и выберите срок подписки.'

		self.referal_manual = '''
      	Приглашайте друзей, получайте скидки!! Просто перешлите следующее сообщение человеку, которого хотите пригласить и как только он купит подписку — вам начислится скидка.
		Чем больше приглашённых — тем выше скидка. Например, за одного человека Вы получите скидку 3%, за 2-ух — 5%, за 5-ых — 10% и так далее.

		Заработайте себе бесплатный доступ - приглашая друзей!
		'''

		self.referal_message = '''
		Приглашаем воспользоваться нашим ботом @bittrex_official_bot
		Перешлите это сообщение боту и получите скидку 5% на следующую подписку.
		Пригласивший Вас человек тоже получит скидку как только Вы активируете подписку.

		Реферальный токен: \n {}
		'''

		self.your_invited_user = '''
		Вы были приглашены пользователем @{}. Вам была начислена скидка 5%.
		'''

		self.already_invited = '''
		Вам уже начислялся пригласительный бонус за приглашение пользователем @{}
		'''



class Message(BaseModel):
	sender		= IntegerField()
	text 		= TextField()
	msg_type	= TextField()
	timestamp	= DateTimeField(default = datetime.datetime.utcnow)

class Error(BaseModel):
	message 	= TextField()
	state		= TextField()
	exception 	= TextField()
	timestamp	= DateTimeField(default = datetime.datetime.utcnow)