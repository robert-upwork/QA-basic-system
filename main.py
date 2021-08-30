import spacy
from question_processor import QuestionProcessor
from text_extractor import TextExtractor
from text_extractor_pipe import TextExtractorPipe
from context_retriever import ContextRetriever
from answer_retriever import AnswerRetriever

# textExtractor1 = TextExtractor("London", "Q84")
# textExtractor1.extract()
# textExtractor2 = TextExtractor("Berlin", "Q64")
# textExtractor2.extract()
# textExtractor3 = TextExtractor("Bucharest", "Q19660")
# textExtractor3.extract()

textExtractor1 = TextExtractor("London", "Q84")
textExtractor2 = TextExtractor("Berlin", "Q64")
textExtractor3 = TextExtractor("Bucharest", "Q19660")

textExtractorPipe = TextExtractorPipe()
textExtractorPipe.addTextExtractor(textExtractor1)
textExtractorPipe.addTextExtractor(textExtractor2)
textExtractorPipe.addTextExtractor(textExtractor3)

nlp = spacy.load('en_core_web_sm')

# nlp.add_pipe(nlp.create_pipe('sentencizer'))
nlp.add_pipe('sentencizer')
doc = nlp(textExtractorPipe.extract())
sentences = [sent.text.strip() for sent in doc.sents]
questionProcessor = QuestionProcessor(nlp)
contextRetriever = ContextRetriever(nlp, 10)
answerRetriever = AnswerRetriever()

originalQuestion = "What is the capital city of Romania?"
questionContext = contextRetriever.getContext(sentences, questionProcessor.process(originalQuestion))
# print(questionContext)
print(questionProcessor.process(originalQuestion))
answer = answerRetriever.getAnswer(originalQuestion, questionContext)
print (answer)