from backend.src.llm import MemoryLLM
from backend.src.chroma_client import ChromaClient
from backend.src.utils import logging

enable_logging = True

class LLMAgent():
    def __init__(
        self, 
        llm: MemoryLLM = None, 
        chroma: ChromaClient = None, 
    ) -> None:
        self.llm = llm
        self.chroma = chroma
        # self.similarity_threshold = 0.5 # [0; 1]


    @logging(enable_logging, message = "[Adding to memory]")
    def add(self, request):
        self.chroma.add(request) if request != "" else None

        response = self.llm.response(request)

        return response

    @logging(enable_logging, message = "[Querying memory]")
    def memory_response(self, request, collection_name = "default", n_results = 3, memory_access_threshold = 1.5):
        memory_queries_data = self.chroma.query(request, n_results = n_results, return_text = False, collection_name = collection_name)
        memory_queries = memory_queries_data['documents'][0]
        memory_queries_distances = memory_queries_data['distances'][0]

        acceptable_memory_queries = []

        for query, distance in list(zip(memory_queries, memory_queries_distances)):
            # print(f"Query: {query}, Distance: {distance}")
            if distance < memory_access_threshold:
            # if (1 - distance) >= self.similarity_threshold:
                acceptable_memory_queries.append(query)

        if len(acceptable_memory_queries) > 0:
            response = self.llm.memory_response(request, acceptable_memory_queries)
        else:
            response = self.llm.response(request) #TODO: add another solution

        return response

    @logging(enable_logging, message = "[Response]")
    def response(self, request: str):
        return self.llm.response(request)
