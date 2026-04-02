import language_tool_python
import contractions

tool = language_tool_python.LanguageTool('en-US')

def correct_grammar(text):

    # expand contractions
    text = contractions.fix(text)

    # grammar correction
    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)

    return corrected