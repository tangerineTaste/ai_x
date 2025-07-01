# 네이버 쇼핑목록 데이터프레임으로 
from dotenv import load_dotenv
from naverOpenai import get_naver_api_data, str_json_dataframe
from handleSheet import handle_init_sheet, update_now_list, save_close_file
import xlwings as xw

def main():
    # 1. genai_rap.xls 파일 열기
    file_path = 'genai_rpa.xlsx'
    wb = xw.Book(file_path)

    # 2~4
    handle_init_sheet(wb, file_path)
    
    # 5. 네이버 api 쇼핑목록 데이터 출력(json형태 str -> dict -> dataframe)
    df_shopping = str_json_dataframe(get_naver_api_data('shop','포켄스'))
    
    # 6
    update_now_list(wb,df_shopping)

    # 7
    save_close_file(wb,file_path)

if __name__ == '__main__':
    main()

load_dotenv()

