from predict import predict_apt_price, loaded_model
import xlwings as xw

def main():
    file_path = '../data/ex3_xlwing.xlsx'
    wb = xw.Book(file_path)
    ws = wb.sheets.active

    for line in range(2,5):
        year = ws.range('B' + str(line)).value
        square = ws.range('C' + str(line)).value
        floor = ws.range('D' + str(line)).value
        pred = predict_apt_price(year, square, floor)
        ws.range('E' + str(line)).value = pred
    wb.save(file_path)
    wb.close()

if __name__ == '__main__':
    main()