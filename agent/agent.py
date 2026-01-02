from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from agent.tools import generate_bullets, generate_cover_letter
from agent.memory import retrieve
from agent.guardrails import validate_output
from agent.scoring import fit_score

llm = ChatOpenAI(temperature=0)

tools = [generate_bullets, generate_cover_letter]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

def run_agent(query: str):
    docs = retrieve(query)
    context = "\n".join(d.page_content for d in docs)

    result = agent.run(
        f"Context:\n{context}\n\nTask:\n{query}"
    )

    validate_output(result)
    return result
