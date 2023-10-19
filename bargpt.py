import requests
class Client():
	def __init__(self):
		self.api="https://www.bargpt.app/api"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def search_cocktails(self,q):
		return requests.get(f"{self.api}/searchcocktails?search={q}",headers=self.headers).json()
	def search_ingredient_list(self,q):
		return requests.get(f"{self.api}/searchingredientlist?search={q}",headers=self.headers).json()
	def like_recipe(self,cid):
		return requests.get(f"{self.api}/likerecipe?cid={cid}",headers=self.headers).json()
	def get_featured_cocktails(self):
		return requests.get(f"{self.api}/getfeaturedcocktails",headers=self.headers).json()
	def get_cocktail_count(self):
		return requests.get(f"{self.api}/getcocktailcount",headers=self.headers).json()
	def get_credits_for_user(self):
		return  requests.get(f"{self.api}/getcreditsforuser",headers=self.headers).json()