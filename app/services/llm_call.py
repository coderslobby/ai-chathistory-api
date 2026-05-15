from groq import Groq, APIConnectionError, APIStatusError
from fastapi.exceptions import HTTPException
from app.settings import settings

client = Groq(api_key=settings.GROQ_API_KEY)

def chat_request(question: str)-> str:
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    'role':'system',
                    'content':'''You are a helpful AI assistant.
                                Answer the user's question clearly and concisely.'''
                },
                {
                    'role':'user',
                    'content':f'{question}'
                }
            ],
            model=settings.language_model,
            max_tokens=settings.max_llm_tokens
        )
        answer = response.choices[0].message.content
        return str(answer)
    
    except APIConnectionError:
        raise HTTPException(status_code=503,
                            detail='Cannot reach Groq API — network may be blocking it!')
    except APIStatusError as e:
        raise HTTPException(status_code=e.status_code,
                            detail=f'Groq API error {e.message}')
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=f'Unexpected error')