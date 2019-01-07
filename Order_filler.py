OUT_OF_SITE = -1
OUT_OF_SITE_MESSAGE = "그런 번호를 가진 사이트는 없습니다."


def order_filler(person, order_type):
    order = [order_type]
    thing_to_add = []
    if order_type == "add":
        thing_to_add = add_filler(person)
    elif order_type == "del":
        thing_to_add = del_filler(person)
    elif order_type == "update":
        thing_to_add = update_filler(person)
    if thing_to_add is None:
        return None
    return order + thing_to_add

def select_site_menu(person, guide, zero_selection_event):
    print(guide)
    print(zero_selection_event)
    person.print_site_list()
    select = int(input("선택 > "))
    if select > person.get_site_count() or select < 0:
        return OUT_OF_SITE
    return select


# ##### ADD #####
def add_filler(person):
    select = select_site_menu(person,
                              "계정을 추가하고자 하는 사이트의 번호를 선택해주세요.",
                              "[00] 사이트 추가")
    if select == OUT_OF_SITE:
        print(OUT_OF_SITE_MESSAGE)
        return None
    elif select == 0:
        return [add_site_filler(person)]
    else:
        site = person.get_site_by_number(select)
        return [add_account_filler(site)]

def add_site_filler(person):
    return input("새 사이트 이름 > ")
def add_account_filler(site):
    return None

def del_filler(person):
    select = select_site_menu(person,
                              "사이트 자체 혹은 계정을 삭제하고자 하는 사이트의 번호를 선택해주세요.",
                              "[00] 동작 취소")
    if select == OUT_OF_SITE:
        print(OUT_OF_SITE_MESSAGE)
        return


def update_filler(person):
    select = select_site_menu(person,
                              "사이트 이름 혹은 계정 속성을 변경하고자 하는 사이트의 번호를 선택해주세요.",
                              "[00] 동작 취소")
    if select == OUT_OF_SITE:
        print(OUT_OF_SITE_MESSAGE)
        return
