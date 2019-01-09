import Account as ac

NONEXISTENT = -1
class Site(object):
    def __init__(self):
        self.site_name = "§_uninit_Site_name"
        self.accounts = []
    def interprete_order(self,order):
        pass
    def get_account_by_number(self, number):
        return self.accounts[number]
    def get_account_by_ID(self, ID):
        return self.accounts[self.get_index_of_site_name(ID)]
    def get_account_count(self):
        return len(self.accounts)

    def print_account_list(self):
        i = 1
        for account in self.accounts:
            print("[" + str(i).zfill(2) + "] ID : ", account.ID)
            i += 1

    def is_duplicated_ID(self, ID):
        if self.get_index_of_ID(ID) == NONEXISTENT:
            return False
        return True

    def get_index_of_ID(self, ID):  # 사이트 이름을 받아 인덱스 (없으면 -1) 반환
        try:
            return next(i for i, account in enumerate(self.accounts) if account.ID == ID)
        except:
            return NONEXISTENT

if __name__ == "__main__":
    print("Main.py 를 실행해주세요.")
