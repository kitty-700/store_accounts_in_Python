import Site as st
NONEXISTENT = -1

class Person(object):
    def __init__(self):
        self.sites = []
        #Site count는 필요한 시점에 구하도록하자.

    def interprete_order(self,order): #order 는 문자열들의 리스트
        pass
    "add naver das7177 asdasdinr12 none_add"
    "add naver"

    def print_site_list(self):
        for site in self.sites:
            print(site.site_name)

    def is_duplicated_site_name(self, site_name):
        if self.get_index_of_site_name(site_name) == NONEXISTENT:
            return False
        return True

    def get_index_of_site_name(self, site_name):
        try:
            return next(i for i, site in enumerate(self.sites) if site.site_name == site_name)
        except:
            return -1

    def add_site(self, site_name):
        if (self.is_duplicated_site_name(site_name)) == True: 
            #파이썬에서는 클래스 내에 선언된 함수도 self.(함수이름)를 통해 접근
            print("이미 존재하는 사이트 이름입니다.")
            return
        temp_site = st.Site()
        temp_site.site_name = site_name
        self.sites.append(temp_site)

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
