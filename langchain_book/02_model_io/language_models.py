from langchain.chat_models import ChatOpenAI  #← 모듈 가져오기
from langchain.schema import HumanMessage  #← 사용자의 메시지인 HumanMessage 가져오기

chat = ChatOpenAI(  #← 클라이언트를 만들고 chat에 저장
    model="gpt-3.5-turbo",  #← 호출할 모델 지정
)

result = chat( #← 실행하기
    [
        HumanMessage(content="계란찜 만드는 법을 알려줘!"),
        HumanMessage(content="{ChatModel의 답변인 계란찜 만드는 법}"),
        HumanMessage(content="영어로 번역해줘"),

    ]
)
print(result.content)
