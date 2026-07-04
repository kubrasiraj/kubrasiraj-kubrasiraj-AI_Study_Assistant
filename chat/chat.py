from prompts.main_prompt import get_prompt

def ask_question(question, mode, retriever, model):

  

    docs = retriever.invoke(question)

    

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

   

    prompt = get_prompt(mode)



    final_prompt = prompt.invoke({
        "context": context,
        "question": question
    })

    

    result = model.invoke(final_prompt)

 

    return result.content