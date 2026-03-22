import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def correct_grammar(text):

    matches = tool.check(text)

    corrected = language_tool_python.utils.correct(text, matches)

    return corrected