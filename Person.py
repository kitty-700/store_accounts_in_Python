import Site as st
import Order_filler as of

NONEXISTENT = -1


class Person(object):
    def __init__(self):
        self.sites = []
        # site count는 필요한 시점에 구하도록하자.

    def interprete_order(self, order):  # order 는 문자열들의 리스트
        otc = len(order)  # otc?  order_token_count, 즉 order 의 토큰화된 개수
        if otc == 1 and order[0] in ["add", "delete", "update"]:
            order = of.order_filler(self,order[0])
            if order is None:
                return
            otc = len(order) #명령어가 채워졌으니 다시 계산한다.
        if order[0] == "add":
            if otc == 2:
                # ["add", "naver"]
                self.add_site(order[1])
            elif otc in [4, 5]:
                # ["add", "naver", "mcdonald37", "qlalfqjsgh213123@"]
                # ["add", "naver", "mcdonald37", "qlalfqjsgh213123@", "this account is main"]
                if self.get_index_of_site_name(order[1]) == NONEXISTENT:
                    self.add_site(order[1])
                self.pass_operation_to_site(order[1], order)
            else:
                print(order, "은 add 명령에 지원되지 않는 명령어 양식입니다.")
        elif order[0] == "del":
            pass
        elif order[0] == "update":
            pass
        elif order[0] == "ls":
            self.print_site_list()
        else:
            pass
    def get_site_by_number(self, number):
        pass
    def get_site_by_site_name(self, site_name):
        pass
    def get_site_count(self):
        return len(self.sites)

    def print_site_list(self):
        i = 1
        for site in self.sites:
            account_count = site.get_account_count()
            print("[" + str(i).zfill(2) + "]", site.site_name, "    (", account_count, "계정 보유 중 )")
            i += 1

    def is_duplicated_site_name(self, site_name):
        if self.get_index_of_site_name(site_name) == NONEXISTENT:
            return False
        return True

    def get_index_of_site_name(self, site_name):  # 사이트 이름을 받아 인덱스 (없으면 -1) 반환
        try:
            return next(i for i, site in enumerate(self.sites) if site.site_name == site_name)
        except:
            return NONEXISTENT

    def add_site(self, site_name):
        if self.is_duplicated_site_name(site_name):
            # 파이썬에서는 클래스 내에 선언된 함수도 self.(함수이름)를 통해 접근
            print("이미 존재하는 사이트 이름입니다.")
            return
        new_site = st.Site()
        new_site.site_name = site_name
        self.sites.append(new_site)

    def del_site(self, site_name):
        site_index = self.get_index_of_site_name(site_name)
        if site_index == NONEXISTENT:
            print("삭제 실패! 해당하는 사이트를 찾을 수 없습니다.")
            return
        del self.sites[site_index]

    def update_site_name(self, site_name, new_site_name):
        site_index = self.get_index_of_site_name(site_name)
        if site_index == NONEXISTENT:
            print("수정 실패! 해당하는 사이트를 찾을 수 없습니다.")
            return
        if self.is_duplicated_site_name(new_site_name) == True:
            print("바꾸려는 이름은 이미 존재하는 사이트 이름입니다.")
            return
        self.sites[site_index].site_name = new_site_name

    def pass_operation_to_site(self, site_name, order):
        site_index = self.get_index_of_site_name(site_name)
        if site_index == NONEXISTENT:
            print("명령 실패! 해당하는 사이트를 찾을 수 없습니다.")
            return
        self.sites[site_index].interprete_order(order)


if __name__ == "__main__":
    print("Main.py 를 실행해주세요.")
