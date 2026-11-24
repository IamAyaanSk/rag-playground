from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

from utils.document_loaders import load_pdf

model = init_chat_model(
    model="thinkingmachines/inkling-2-mini",
    model_provider="openai",
    use_responses_api=True,
)


def main():
    print("Hello from rag!")
    # response = model.invoke("How are you?")
    # print(response)

    result = load_pdf("hello.pdf")

    print(result)


if __name__ == "__main__":
    main()
