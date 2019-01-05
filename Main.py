import sys
import Order_grouping as og
import Account as ac
import Site as st
import Person as pr

order_argument = sys.argv
#C++에서 했던것처럼 모든 파라미터를 모아두는 곳을 따로 만들지말고
#클래스 하나를 OSI 7 레이어처럼 계층으로 나눠버리는건? 
#헤더 떼가면서 페이로드만 줏어가고 각 계층마다 파싱하고
if __name__ == "__main__":
    order = ""
    kitty = pr.Person()
    if len(order_argument) != 1:
        for each in order_argument[1:]:
            order += each + " "
        print("인자로 전달된 명령은",order)
    while order != "exit" :
        if order != "":
            order = input("> ")
        kitty.interprete_order(og.tokenizer(order,"'"))
