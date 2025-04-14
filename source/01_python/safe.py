def safe_index(lst,item):
    '''
    lst안에 item 요소가 있으면 아이템 요소의 index를 반환하고, 없다면 -1반환. 
    lst : 나열 가능한 데이터
    item : 찾을 데이터
    '''
#    if item in lst:
#        return lst.index(n)s
#    else:
#        return -1
    return lst.index(item) if item in lst else -1