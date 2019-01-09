import Site as st
import Order_filler as of

NONEXISTENT = -1
CANCEL = "*(!CANCLE!)*"
POS_OT = 0  # position of order type


class Person(object):
    def __init__(self):
        self.sites = []

    def interprete_order(self, order):  # order 는 문자열들의 리스트
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

    def get_site_by_number(self, number):
        return self.sites[number - 1]

    def get_site_by_site_name(self, site_name):
        return self.sites[self.get_index_of_site_name(site_name)]

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

    """ 
    Person이 갖고 있는 Site 객체 자체를 추가/삭제/이름변경하는건 중복 확인 등의 문제때문에 Person 클래스에서 구현하지만 
    Site 내에 있는 Account 객체에 대해서는 Site 클래스에서 구현한다.
    Learn. 그리고 이처럼 여러 줄 주석 처리할 때에도 들여쓰기는 지켜야 한다.
    """

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

    # 나머지 작업은 Site 클래스에 넘긴다.#
    def pass_operation_to_site(self, order):
        site_index = self.get_index_of_site_name(order[1])
        if site_index == NONEXISTENT:
            print("명령 실패! 해당하는 사이트를 찾을 수 없습니다.")
            return
        self.sites[site_index].interprete_order(order)


if __name__ == "__main__":
    print("Main.py 를 실행해주세요.")
