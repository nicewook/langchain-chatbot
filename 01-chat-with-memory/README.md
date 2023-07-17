# Chat with memory

LangChain, OpenAI, Memory를 활용한 챗봇 구현

## 설명
- OpenAI 모델은 디폴트가 `gpt-3.5-turbo`
- 대화를 요약하여 기억하는 메모리이다. 
  - 요약을 위해서 LLM을 사용하여야 하니 메모리 설정시 `ChatOpenAI()` 를 명시한 것을 알 수 있다.
  - 이러한 요약을 넣어줄 기억(?)의 용량을  2048로 설정하였다. 