# ctrl+shift+p : 인터프리터 선택
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def askGPT(prompt):
    "매개뱐수로 받은 prompt를 3줄로 요약"
    client = OpenAI()
    response = client.chat.completions.create(
        model='gpt-4.1-nano',
        messages=[
            {'role':'system', 'content':'당신은 한국어 텍스트를 훌륭하게 요약하는 전문 어시스턴트입니다'},
            {'role':'user', 'content':prompt},
            ]
    )
    return  response.choices[0].message.content

def main():
    result = askGPT("""아래의 글을 20자로 요약해주세요
                    텍스트:최근 인천 지역 수돗물에서 흙과 곰팡이 냄새가 심하게 난다는 주민들의 민원이 제기돼 인천시가 진화에 나섰다.
                    26일 인천시 상수도사업본부에 따르면 지난 24일부터 이날 오전까지 수돗물에서 냄새가 난다는 민원 80여건이 접수됐다. 냄새가 나는 주요 지역은 미추홀구, 남동구, 연수구 등이다.
                    A씨는 지난 24일부터 수돗물에서 “녹물 같은 냄새가 난다”며 “양치하거나 손을 씻을 때 느껴진다”고 말했다. 송도 지역 온라인 커뮤니티에는 이날 오전 ‘혹시 수돗물에서 흙+곰팡이 맛 느끼신 분?’이라는 글이 올라오기도 했다.
                    시 상수도사업본부는 수도권 상수원인 팔당 원수(源水) 취수장에서 맛·냄새 유발 물질인 2-메틸이소보르네올(2-MIB)이 평소보다 많아져 수돗물에서 냄새가 난 것으로 보고 있다. 고수온으로 인한 녹조 원인이 되는 유해 남조류 세포 수가 일시적으로 많아졌기 때문이다.  이 세포들은 대사할 때 ‘2-MIB’물질을 내뿜는다.
                    팔당 원수 취수장에서는 지난 24∼25일 2-MIB 성분이 1ℓ당 최고 80ng(나노그램)이 검출돼 먹는 물 수질 감시기준인 20ng을 초과했다. 2-MIB은 인체에는 무해하며 열을 가하면 쉽게 휘발되는 특성이 있어 3분 이상 끓이면 냄새가 사라진다. 시 상수도사업본부는 분말 활성탄을 추가 투입해 맛·냄새 유발 물질을 저감시키는 등 정수처리 공정을 강화했다.
                    """)
    print(result)

if __name__ == '__main__':
    main()