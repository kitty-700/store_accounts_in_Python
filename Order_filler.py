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
	select = input("����")
	return select

def add_filler(person):
	select = select_site_menu(person,
		"������ �߰��ϰ��� �ϴ� ����Ʈ�� ��ȣ�� �������ּ���.",
		"[00] ����Ʈ �߰�")
def del_filler(person):
	select = select_site_menu(person,
		"����Ʈ ��ü Ȥ�� ������ �����ϰ��� �ϴ� ����Ʈ�� ��ȣ�� �������ּ���.",
		"[00] ���� ���")
def update_filler(person):
	select = select_site_menu(person,
		"����Ʈ �̸� Ȥ�� ���� �Ӽ��� �����ϰ��� �ϴ� ����Ʈ�� ��ȣ�� �������ּ���.",
		"[00] ���� ���")

