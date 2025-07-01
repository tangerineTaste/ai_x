import xlwings as xw

# 현재 열린 엑셀 파일 데이터 가져옴

wb = xw.apps.active.books.active # type: ignore
sheet = wb.sheets.active
print('데이터를 가져와 연산 수행')
b1 = sheet.range('B1').value
b2 = sheet.range('B2').value

sheet.range('B3').value = b1 - b2 # type: ignore
print('연산 결과 쓰기 완료')
