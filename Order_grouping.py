import string
def tokenizer(order_string, packing_char): #문자열 받아서 리스트로 잘라줌
    order_token = []
    order_string = order_string.strip()
    packing_char_count = order_string.count(packing_char)
    while 1:
        if packing_char_count <= 1:
            #1.묶을 문자 (packing_char) 끼리의 매칭이 없으면 걍 리스트로 나눠서 리턴
            order_token += order_string.split()
            return order_token 
        first_packing_char_index = order_string.index(packing_char)
        cutted_left_string = order_string[0:first_packing_char_index]
        order_token += cutted_left_string.split()
        cutted_right_string = order_string[first_packing_char_index + 1:]

        second_packing_char_index = cutted_right_string.index(packing_char)
        packed_string = cutted_right_string[0:second_packing_char_index]
        order_token += [packed_string]
            
        order_string = cutted_right_string[second_packing_char_index+1:]
        packing_char_count = order_string.count(packing_char)