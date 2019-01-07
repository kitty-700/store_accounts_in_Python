import Account as ac
class Site(object):
    def __init__(self):
        self.site_name = "§_uninit_Site_name"
        self.accounts = []
        #Account count는 필요한 시점에 구하도록하자.
    def interprete_order(self,order):
        pass
    def get_account_count(self):
        i = 0
        for site in self.accounts:
            i+=1
        return i
if __name__ == "__main__":
    print("Main.py 를 실행해주세요.")
