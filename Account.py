class Account(object):
    def __init__(self):
        self.ID = "§_uninit_ID"
        self.PW = "§_uninit_PW"
        self.update_time = "§_uninit_update_time"
        self.memo = ""

    def tell_itself(self):
        print("ID : "+self.ID)
        print("PW : "+self.ID)
        print("UD : "+self.update_time)
        print("MM : "+self.memo)

if __name__ == "__main__":
    print("Main.py 를 실행해주세요.")
