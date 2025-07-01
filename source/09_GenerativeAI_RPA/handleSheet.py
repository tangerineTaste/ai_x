import datetime
import shutil 
import os
import xlwings as xw

def handle_init_sheet(wb, file_path):
    # 2. 백업(파일명 : genai_rap2507011258.xls)
    timestamp = datetime.datetime.now().strftime('%y%m%d%H%M')
    backupfilename = f'genai_rpa{timestamp}.xlsx'
    shutil.copy(file_path, backupfilename)
    print('백업파일 생성 완료')

    # 3. 'prev_list' 시트를 삭제
    sheet_names = [s.name for s in wb.sheets]
    if 'prev_list' in sheet_names:
        wb.sheets['prev_list'].delete()
        print('prev_list 삭제 완료')
    else:
        print('prev_list가 존재하지 않습니다')

    # 4. 'now_list' 시트를 'prev_list'시트로 이름변경
    if 'now_list' in sheet_names:
        now_sheet = wb.sheets['now_list']
        prev_sheet = now_sheet.copy(after=now_sheet)
        prev_sheet.name = 'prev_list'
        print('now_list시트 prev_list시트로 복사 완료')
    else:
        print('now_list가 존재하지 않습니다.')
        return 
    
def update_now_list(wb, df_shopping):    
    # 6. 'now_list' 시트의 모든 내용을 클리어하고, df_shopping내용('A1'셀)을 업데이트
    now_sheet = wb.sheets['now_list']
    now_sheet.clear()
    now_sheet.range('A1').value = df_shopping
    print('now_list 내용 업데이트 완료')

def save_close_file(wb, file_path):
     # 7. 파일 저장 및 
    wb.save(file_path)
    print('workbook 저장완료')

def update_now_report(wb , analysis, summary):
    sheet_names = [s.name for s in wb.sheets]
    if 'prev_report' in sheet_names:
        wb.sheets['prev_report'].delete()
        print('prev_report 시트 삭제 완료')
    else:
        print('prev_report가 존재하지 않습니다')

    if 'now_report' in sheet_names:
        now_sheet = wb.sheets['now_report']
        prev_sheet = now_sheet.copy(after=now_sheet)
        prev_sheet.name = 'prev_report'
        print('now_report시트 prev_report시트로 복사 완료')
    else:
        print('now_report가 존재하지 않습니다.')
        return

    # 시간 넣기
    current_dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    now_sheet.range('A3').value = current_dt + '기준' # 오른쪽 정렬
    now_sheet.range('A3').api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight

    # 오픈마켓 검색 결과 변동 넣기
    now_sheet.range('A5').value = analysis
    now_sheet.range('A5').api.WrapText = True # 내용이 셀보다 길면 자동 줄바꿈

    now_sheet.range('A8').value = summary
    now_sheet.range('A8').api.WrapText = True 

    print('now_report 내용 업데이트 완료')

    # now_sheet 를 pdf파일로 생성(genai_rpa_2507011655.pdf)
    timestamp = datetime.datetime.now().strftime('%y%m%d%H%M')
    file_name = f'C:/ai_x/source/09_GenerativeAI_RPA/genai_rpa_{timestamp}.pdf'
    now_sheet.api.ExportAsFixedFormat(0, file_name)

    
    
    