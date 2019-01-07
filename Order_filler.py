import Person as pr

def order_filler(person, order_type):
	if order[0] == "add":
		add_filler(person)
	elif order[0] == "del":
		del_filler(person)
	elif order[0] == "update":
		pass
	
def select_site_menu(person, guide, zero_selection_event):
	print(guide)
	print(zero_selection_event)
	person.print_site_list()
	select = input("선택")
	return select

def add_filler(person):
	select = select_site_menu(person,
		"계정을 추가하고자 하는 사이트의 번호를 선택해주세요.",
		"[00] 사이트 추가")
def del_filler(person):
	select = select_site_menu(person,
		"사이트 자체 혹은 계정을 삭제하고자 하는 사이트의 번호를 선택해주세요.",
		"[00] 동작 취소")
def update_filler(person):
	select = select_site_menu(person,
		"사이트 이름 혹은 계정 속성을 변경하고자 하는 사이트의 번호를 선택해주세요.",
		"[00] 동작 취소")

