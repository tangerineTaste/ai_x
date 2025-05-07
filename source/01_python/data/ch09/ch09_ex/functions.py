from customer import Customer
import csv

def fn1_insert_customer_info():
    '''
    사용자로부터 name, phone, email, age, grade, etc를 입력받아 Customer형 객체 반환
    '''
    import re
    name = input('이름 :')
    name_pattern = r'[가-힣]{2,}'
    while not re.search(name_pattern, name):
        print('이름을 제대로 입력하세요(한글 2글자 이상)')
        name = input('이름 :')
    phone = input('전화 :')
    email = input('메일 :')
    while True:
        try:
            age = int(input('나이 :'))
            if (age<0) or (age>130) :
                raise Exception('나이 범위 이상')
            break 
        except:
            print('올바른 나이를 입력하세요')
    try:
        grade = int(input('등급(1~5) : '))
        # grade = 1 if grade < 1 else 5 if grade>5 else grade
        if grade < 1:
            grade = 1
        if grade > 5:
            grade = 5
    except:
        print('유효하지 않은 등급 입력시 1등급으로 초기화')
        grade = 1
    etc = input('기타 정보 :')
    return Customer(name, phone, email, age, grade, etc)

def fn2_print_customers(customer_list):
    'customer_list를 출력(pdf 40page 스타일)'
    print('='*70)
    print('{:^70}'.format('고객 정보'))
    print('-'*70)
    print("{:>5}\t{:3}\t{:13}\t{:10}\t{:3}\t{}".format("GRADE", "이름", "전화",
                                                      "메일","나이","기타"))
    print('-'*70)
    for customer in customer_list:
        print(customer)

def fn3_delete_customer(customer_list):
    '''삭제하고자 하는 고객이름을 input으로 받아
    매개변수로 들어온 customer_list에서 삭제하고 "삭제했음/삭제못했음"을 메세지로 출력'''
    delete_name = input('삭제할 고객 이름은?')
    delete_idx = [] # 삭제할 인덱스를 저장하는 용도
    for idx, customer in enumerate(customer_list):
        if customer.name == delete_name:
            delete_idx.append(idx)
    if delete_idx:
        for idx in delete_idx[::-1]: # [1,0]
            print(customer_list[idx], '지우시겠습니까?', end='')
            answer = input('(Y/N)')
            if answer.upper() == 'Y':
                print('요청하신 {}({})님 삭제 완료'.format(delete_name,
                                                 customer_list[idx].phone))
                del customer_list[idx]
    else:
        print('{}님 데이터가 존재하지 않습니다'.format(delete_name))

def fn4_search_customer(customer_list):
    '''찾고자 하는 이름을 input으로 받아, customer_list에서 검색하여 
    같은 이름이 있으면 search_list에 append한 후 search_list를 출력
    같은 이름이 없으면 없다고 출력'''
    search_name = input('검색할 이름은?')
    search_idx = []
    for idx, customer in enumerate(customer_list):
        if customer.name == search_name:
            search_idx.append(idx)
    if search_idx:
        print('='*70)
        print('{:^70}'.format('고객 정보'))
        print('-'*70)
        print("{:>5}\t{:3}\t{:13}\t{:10}\t{:3}\t{}".format("GRADE", "이름", "전화",
                                                          "메일","나이","기타"))
        print('-'*70)
        for idx in search_idx:
            print(customer_list[idx])
    else:
        print("{}님 데이터는 존재하지 않습니다".format(search_name))

def fn5_save_customer_csv(customer_list):
    customer_dic_list = []
    for customer in customer_list:
        customer_dic_list.append(customer.as_dic())
    fieldnames = list(customer_dic_list[0].keys())
    filename = input('저장할 csv 파일명은?')
    with open('data/{}.csv'.format(filename), 'w', encoding='utf-8',newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
        dict_writer.writeheader() #헤더
        dict_writer.writerows(customer_dic_list)
        print(f'data/{filename}.csv 내보내기 완료')

def fn9_save_customer_txt(customer_list):
    '''
    customer_list를 to_list_style()를 이용해서 
    ch09_customers.txt.로 백업
    '''
    customer_txt_list = []
    for customer in customer_list:
        customer_txt_list.append(customer.to_list_style() + '\n')
    with open('data/ch09_customers.txt', 'w', encoding='utf-8') as f:
        f.writelines(customer_txt_list)