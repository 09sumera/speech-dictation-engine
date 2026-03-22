import language_tool_python

tool = language_tool_python.LanguageToolPublicAPI('en-US')

def correct_grammar(text):
    matches = tool.check(text)
    return language_tool_python.utils.correct(text, matches)