# 네이버 쇼핑목록 데이터프레임으로 
from dotenv import load_dotenv
from naverOpenai import get_naver_api_data, str_json_dataframe, ai_analysis, get_openai_news_summarize
from handleSheet import handle_init_sheet, update_now_list, save_close_file, update_now_report
import xlwings as xw

def main():
    # 1. genai_rap.xls 파일 열기
    file_path = 'genai_rpa.xlsx'
    wb = xw.Book(file_path)

    # 2~4
    handle_init_sheet(wb, file_path)
    
    # 5. 네이버 api 쇼핑목록 데이터 출력(json형태 str -> dict -> dataframe)
    df_shopping = str_json_dataframe(get_naver_api_data('shop','애완용품'))
    
    # 6. now_list 시트를 새로 받아온 데이터로 업데이트 해준다
    update_now_list(wb,df_shopping)

    # 7. 분석 보고서 업데이트
    # 쇼핑 목록 분석
    result_analysis = ai_analysis(wb)
    # 뉴스 분석
    str_news_data = get_naver_api_data('news','애완용품')
    result_summary = get_openai_news_summarize(str_news_data)
    update_now_report(wb,result_analysis,result_summary)

    # 8
    save_close_file(wb,file_path)

if __name__ == '__main__':
    main()

