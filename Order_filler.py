import Person as pr
import Site as st

OUT_OF_SITE = -1
OUT_OF_SITE_MESSAGE = "그런 번호를 가진 사이트는 없습니다."
OUT_OF_ACCOUNT = -2
OUT_OF_ACCOUNT_MESSAGE = "그런 번호를 가진 계정는 없습니다."
OUT_OF_INT_STRING = -3
OUT_OF_INT_STRING_MESSAGE = "문자열에 숫자 외의 문자가 포함되어있습니다."
CANCEL_INT = -4
CANCEL = "*(!CANCLE!)*"
CANCEL_MESSAGE = "동작을 취소합니다."

POS_OT = 0  # position of order type

def fill_the_order_if_unfilled(person, order):
    otc = len(order)  # otc?  order_token_count, 즉 order 의 토큰화된 개수
    if otc == 1 and order[POS_OT] in ["add", "delete", "update"]:
        order = order_filler(person, order[POS_OT])
        if CANCEL in order:
            return (CANCEL, CANCEL_INT)
        otc = len(order)
        return (order,otc)
    else:
        return (order, otc)
def order_filler(person, order_type):
    order = [order_type]
    additional_order = []
    if order_type == "add":
        additional_order = add_filler(person)
    elif order_type == "del":
        additional_order = del_filler(person)
    elif order_type == "update":
        additional_order = update_filler(person)
    else:
        assert ()
    return order + additional_order


def select_menu(object, guide, zero_selection_event):
    print(guide)
    print(zero_selection_event)
    if type(object) is pr.Person:
        object.print_site_list()
    elif type(object) is st.Site:
        object.print_account_list()
    else:
        print(type(object))
        assert ()

    select_str = input("선택 > ")
    try:
        select = int(select_str)
    except ValueError:
        print(OUT_OF_INT_STRING_MESSAGE)
        return OUT_OF_INT_STRING

    if type(object) is pr.Person:
        if select > object.get_site_count() or select < 0:
            return OUT_OF_SITE
    elif type(object) is st.Site:
        if select > object.get_account_count() or select < 0:
            return OUT_OF_ACCOUNT
    return select


# ##### ADD ##### #
def add_filler(person):
    select = select_menu(person,
                         "계정을 추가하고자 하는 사이트의 번호를 선택해주세요.",
                         "[00] 사이트 추가")
    if select == OUT_OF_SITE:
        print(OUT_OF_SITE_MESSAGE)
        return [] + [CANCEL]
    elif select == 0:
        return [] + add_site_filler(person)
    else:
        site = person.get_site_by_number(select)
        return [] + [site.site_name] + add_account_filler(site)


def add_site_filler(person):
    return [input("새 사이트 이름 > ")]


def add_account_filler(site):
    site.print_account_list()
    return [input("새 계정의 ID > "), input("새 계정의 PW > "), input("새 계정에 대한 메모 > ")]


# del
def del_filler(person):
    select = select_menu(person,
                         "사이트 자체 혹은 계정을 삭제하고자 하는 사이트의 번호를 선택해주세요.",
                         "[00] 동작 취소")
    if select == OUT_OF_SITE:
        print(OUT_OF_SITE_MESSAGE)
        return []
    elif select == 0:
        print(CANCEL_MESSAGE)
        return [CANCEL]
    else:
        site = person.get_site_by_number(select)
        return [site.site_name] + del_site_or_account_filler(person, site)


def del_site_or_account_filler(site):
    select = select_menu(site,
                         "삭제할 계정의 번호를 선택해주세요.",
                         "[00]", site.site_name, "사이트 삭제")
    if select == OUT_OF_ACCOUNT:
        print(OUT_OF_SITE_MESSAGE)
        return [CANCEL]
    elif select == 0:
        return []
    else:
        account = site.get_account_by_number(select)
        return [account.ID]


# update
def update_filler(person):
    select = select_menu(person,
                         "사이트 이름 혹은 계정 속성을 변경하고자 하는 사이트의 번호를 선택해주세요.",
                         "[00] 동작 취소")
    if select == OUT_OF_SITE:
        print(OUT_OF_SITE_MESSAGE)
        return
