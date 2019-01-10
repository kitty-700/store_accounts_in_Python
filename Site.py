import Account as ac

POS_OT = 0  # position of order type
NONEXISTENT = -1
class Site(object):
    def __init__(self):
        self.site_name = "§_uninit_Site_name"
        self.accounts = []
    def interprete_order(self,order):
        otc = len(order)  # otc?  order_token_count, 즉 order 의 토큰화된 개수
        if otc == 1 and order[POS_OT] in ["add", "delete", "update"]:
            order = of.order_filler(self, order[POS_OT])
            if CANCEL in order:
                return
            otc = len(order)  # 명령어가 채워졌으니 다시 계산한다.
            print("order will be excuted is", order)

        # add
        if order[0] == "add":
            if otc in [2]:
                # ["add", "naver"]
                self.add_site(order[1])
            elif otc in [4, 5]:
                # ["add", "naver", "mcdonald37", "qlalfqjsgh213123@"]
                # ["add", "naver", "mcdonald37", "qlalfqjsgh213123@", "this account is main"]
                if self.get_index_of_site_name(order[1]) == NONEXISTENT:
                    # 추가하려는 계정의 사이트가 없으면 굳이 번거롭게 에러띄워서 다시 명령하게 만들지말고 아예 추가해주자.
                    self.add_site(order[1])
                self.pass_operation_to_site(order)
            else:
                print(order, "은 add 명령에 지원되지 않는 명령어 양식입니다.")

        # del
        elif order[0] == "del":
            if otc in [2]:
                # ["del", "naver"] (사이트 naver 삭제)
                self.del_site(order[1])
            elif otc in [3]:
                # ["del", "naver", "mcdonald37"] (계정 mcdonald37 삭제)
                self.pass_operation_to_site(order)
            else:
                print(order, "은 del 명령에 지원되지 않는 명령어 양식입니다.")
        # update
        elif order[0] == "update":
            if otc in [3]:
                # ["update", "naver", "Naver"] (사이트 naver의 이름을 Naver로 변경)
                self.update_site_name(order[1], order[2])
            elif otc in [5]:
                # ["update", "naver", "mcdonald37","id","mcdonald36"] (계정 mcdonald37의 id를 mcdonald36으로 변경)
                self.pass_operation_to_site(order)
            else:
                print(order, "은 add 명령에 지원되지 않는 명령어 양식입니다.")
        # show list
        elif order[0] == "ls":
            if len(self.sites) == 0:
                print("아무 사이트도 등록되어있지 않습니다.")
            else:
                self.print_site_list()
        else:
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
