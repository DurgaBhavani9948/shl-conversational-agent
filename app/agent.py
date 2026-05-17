from .utils import extract_latest_user_message, format_recommendations

class ChatAgent:
    def __init__(self, retriever):
        self.retriever = retriever

    def process(self, messages):
        user_text = extract_latest_user_message(messages).strip()

        if not user_text:
            return {
                "reply": "Please describe the role you are hiring for.",
                "recommendations": [],
                "end_of_conversation": False,
            }

        lowered = user_text.lower()

        if "difference between" in lowered or "compare" in lowered:
            return {
                "reply": "Please mention the assessment names you want to compare, and I will compare them using the SHL catalog data.",
                "recommendations": [],
                "end_of_conversation": False,
            }

        vague_terms = {"assessment", "test", "hire", "hiring"}
        if lowered in vague_terms or len(user_text.split()) < 4:
            return {
                "reply": "What role are you hiring for, and what skills or seniority level are important?",
                "recommendations": [],
                "end_of_conversation": False,
            }

        results = self.retriever.search(user_text, top_k=5)
        recs = format_recommendations(results)

        if not recs:
            return {
                "reply": "I could not find matching SHL assessments in the catalog.",
                "recommendations": [],
                "end_of_conversation": True,
            }

        return {
            "reply": f"Based on your requirements, here are {len(recs)} SHL assessments that may fit.",
            "recommendations": recs,
            "end_of_conversation": True,
        }
