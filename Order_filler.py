import Person as pr
import Site as st

CODE_POS = 0
MSG_POS = 1
CTRL_POS = 2
index = {  # error list index
    "OUT_OF_SITE": 0,
    "OUT_OF_ACCOUNT": 1,
    "OUT_OF_INT": 2,
    "CANCEL": 3,
    "OUT_OF_RANGE": 4,
    "NO_INPUT": 5
}
error = [
    # 에러의 명칭 : (에러코드, 에러 설명 메시지, 컨트롤 심볼(optional))
    (-1, "그런 번호를 가진 사이트는 없습니다.", ""),
    (-2, "그런 번호를 가진 계정는 없습니다.", ""),
    (-3, "문자열에 숫자 외의 문자가 포함되어있습니다.", ""),
    (-4, "동작을 취소합니다.", "*(\=\=!CANCLE!=\=\)*"),
    (-5, "범위를 벗어납니다.", ""),
    (-6, "입력이 없으므로 취소합니다.", "")
]

TYPE = 0  # position of order type

attribute = {1: "ID", 2: "PW", 3: "memo"}


def fill_the_order_if_unfilled(person, order):
    otc = len(order)  # otc?  order_token_count, 즉 order 의 토큰화된 개수
    if otc == 1 and order[TYPE] in ["add", "delete", "update"]:
        order = order_filler(person, order[TYPE])
        if error[index["CANCEL"]][CTRL_POS] in order:
            return ([], -1, error[index["CANCEL"]][CTRL_POS])
        otc = len(order)
        return order, otc, "no problem"
    else:
        return order, otc, "no problem"


def order_filler(person, order_type):
    if order_type == "add":
        additional_order = add_filler(person)
    elif order_type == "del":
        additional_order = del_filler(person)
    elif order_type == "update":
        additional_order = update_filler(person)
    else:
        assert ()
    return [order_type] + additional_order


def select_attribute():
    print("[1] ID")
    print("[2] PW")
    print("[3] memo")
    select_str = input("선택 > ")
    if select_str == "":
        print(error[index["NO_INPUT"]][MSG_POS])
        return error[index["NO_INPUT"]][CODE_POS]
    try:
        select = int(select_str)
    except ValueError:
        print(error[index["OUT_OF_INT"]][MSG_POS])
        return error[index["OUT_OF_INT"]][CODE_POS]
    if select > 1 or select < 3:
        print(error[index["OUT_OF_RANGE"]][MSG_POS])
        return error[index["OUT_OF_RANGE"]][CODE_POS]

    return select


def select_menu(object, guide, zero_selection_event):
    print(guide)
    print(zero_selection_event)
    if type(object) is pr.Person:
        object.print_site_list()
    elif type(object) is st.Site:
        object.print_account_list()
    else:
        print(type(object), "은 허가되지 않은 클래스")
        assert ()

    select_str = input("선택 > ")
    if select_str == "":
        print(error[index["NO_INPUT"]][MSG_POS])
        return error[index["NO_INPUT"]][CODE_POS]
    try:
        select = int(select_str)
    except ValueError:
        print(error["OUT_OF_INT"][MSG_POS])
        return error["OUT_OF_INT"][CODE_POS]

    if type(object) is pr.Person:
        if select > object.get_site_count() or select < 0:
            print(error[index["OUT_OF_SITE"]][MSG_POS])
            return error[index["OUT_OF_SITE"]][CODE_POS]
    elif type(object) is st.Site:
        if select > object.get_account_count() or select < 0:
            print(error[index["OUT_OF_ACCOUNT"]][MSG_POS])
            return error[index["OUT_OF_ACCOUNT"]][CODE_POS]
    return select


def is_error_occurence(select):
    try:
        er = next(er for er in enumerate(error) if er[CODE_POS] == select)
        print(er[MSG_POS])
        return True
    except:
        return False


# ##### ADD ##### #
def add_filler(person):
    select = select_menu(person,
                         "계정을 추가하고자 하는 사이트의 번호를 선택해주세요.",
                         "[00] 사이트 추가")
    if is_error_occurence(select):
        return [error[index["CANCEL"]][CTRL_POS]]
    if select == 0:
        return [] + add_site_filler(person)
    else:
        site = person.get_site_by_number(select)
        return [] + [site.site_name] + add_account_filler(site)


def add_site_filler():
    return [input("새 사이트 이름 > ")]


def add_account_filler(site):
    site.print_account_list()
    return [input("새 계정의 ID > "), input("새 계정의 PW > "), input("새 계정에 대한 메모 > ")]


# del
def del_filler(person):
    select = select_menu(person,
                         "사이트 자체 혹은 계정을 삭제하고자 하는 사이트의 번호를 선택해주세요.",
                         "[00] 동작 취소")
    if is_error_occurence(select):
        return [error[index["CANCEL"]][CTRL_POS]]
    elif select == 0:
        print(error[index["CANCEL"]][MSG_POS])
        return [error[index["CANCEL"]][CTRL_POS]]
    else:
        site = person.get_site_by_number(select)
        return [site.site_name] + del_site_or_account_filler(person, site)


def del_site_or_account_filler(site):
    select = select_menu(site,
                         "삭제할 계정의 번호를 선택해주세요.",
                         "[00]", site.site_name, "사이트 삭제")
    if is_error_occurence(select):
        return [error[index["CANCEL"]][CTRL_POS]]
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
    if is_error_occurence(select):
        return [error[index["CANCEL"]][CTRL_POS]]
    elif select == 0:
        print(error[index["CANCEL"]][MSG_POS])
        return [error[index["CANCEL"]][CTRL_POS]]
    else:
        site = person.get_site_by_number(select)
        return [site.site_name] + update_filler_account(site)


def update_filler_account(site):
    select = select_menu(site,
                         "사이트 이름을 변경할 경우 0번을 선택하고,\n사이트 내 계정의 속성을 변경할 경우 계정의 번호를 선택해주세요.",
                         "[00]", site.site_name, "사이트 이름 변경")
    if is_error_occurence(select):
        return [error[index["CANCEL"]][CTRL_POS]]
    elif select == 0:
        return [input("사이트의 새 이름 입력 > ")]
    else:
        account = site.get_account_by_number(select)
        return [account.ID] + update_filler_what_type_changed(account)


def update_filler_what_type_changed(account):
    account.tell_itself()
    select = select_attribute()
    if is_error_occurence(select):
        return [error[index["CANCEL"]][CTRL_POS]]
    else:
        return attribute[select] + update_filler_new_value(account)
    pass


def update_filler_new_value(account, attr):
    msg = account.ID, "의 ", attribute[attr], "를 "
    if attribute[attr] == "ID":
        msg += account.ID
    elif attribute[attr] == "PW":
        msg += account.PW
    elif attribute[attr] == "memo":
        msg += account.memo
    msg += " 에서 무엇으로 바꿀까요? > "
    return [input(msg)]
