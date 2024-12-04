import streamlit as st
from predicatelogic_nlp import preprocess, schematize, streamlitPrems

# functions:

@st.dialog("Example Schema", width="small")
def demo():
    validexample = "All smart farmers are either German or Hungarian. Therefore, either somebody smart is not a farmer, or everyone is either German or Hungarian."
    st.write("okay, let's do a quick demo.\nOur demo argument is: " + validexample + "\n(spoiler alert, this one is logically valid)!")

def nlpProcess(userInput):
    # first, reset everything:
    text = ''
    validexample = "All smart farmers are either German or Hungarian. Therefore, either somebody smart is not a farmer, or everyone is either German or Hungarian."
    if userInput.lower() == 'd' or userInput.lower() == 'demo':
        userInput = validexample
    premises = streamlitPrems(userInput) # listing the premises
    st.session_state.nlp_prems = premises

    text = preprocess(userInput) #creates a new data structure with pre-processed text in the right format <3
    text = schematize(text)
    text = str(text)
    schematized_argument = text
    st.session_state.nlp_output = schematized_argument
    return

def clearText():
    st.session_state.nlp_prems = ''
    st.session_state.nlp_output = ''
    return
# the actual website page:

# Show title and description.
st.title("LogicBot")
st.header("Argument-strength Analyzer")
st.divider()

st.header("... what's that?")
st.text("The LogicBot uses regular expressions to translate English sentences into Propositional Logic Schemata.")
st.markdown("**Propositional Logic** refers to the logical relationships between phrases that can be true or false, aka *propositions*.")

st.header("Project Motivations:")

st.markdown('''
1. I'm a __big__ fan of [Warren Goldfarb](https://archive.org/details/deductivelogic0000gold).
2. I was _not_ a fan of having to hand-schematize arguments to check students' work back in undergrad, and less a fan of having to hand-check their proofs.
3. Computational solutions existed to [schematize](https://colab.research.google.com/github/norvig/pytudes/blob/master/ipynb/PropositionalLogic.ipynb) arguments, and to [check if they're valid or satisfiable](https://docs.sympy.org/latest/modules/logic.html), but none of the tools I'd used did _both_.
            ''')

st.header("Current Iteration: LogicBot 1.0 - Propositional Logic")
st.markdown("")

st.subheader("Further Work: Validity and Soundness")
st.markdown("")

st.header("Future Iterations: Predicate Logic (with NLP)")
st.markdown("Future iterations of the LogicBot might utilize natural language processing to determine the ***Universe of Discourse*** and ***Scope of Discourse*** for certain sentences. The Universe of Discourse refers to the kinds of things enclosed by a variable like 'x' in a schema. The Scope refers to whether one refers to *all* elements in the universe, or only *some*.")
st.markdown("Here's how a similar concept might be understood with different universes and scopes of discourse:") 

st.text("to better schematize them according to Predicate Logic, rather than the Propositional Logic implementation above. Here's an example of what that schematization might look like:")

theysay = st.text_area("Input a sentence here using predicate logic, or type 'demo' to see how this works:")
schema_button = st.button("Schematize", help="Input text above, and click me to schematize!")
if schema_button:
    nlpProcess(theysay)
delete_button = st.button("Clear", help="Click me to clear fields!")
if delete_button:
    clearText()

st.text_area(label="List of Premises and Conclusions", key="nlp_prems")
st.text_area(label="Schematized Argument (_see note_)", key="nlp_output")
st.caption("_NOTE: text has been pre-processed with NLTK's tokenizer and lemmatizer, which is why words are in their neutral/first-person/dictionary-style tense and conjugation. Helpful for future classification down the road!_")
st.markdown("A LogicBot with NLP-type classification might also be able to parse the application of general principles or logical rules as part of one's reasoning - that way, we could add schematized English text as inputs to SymPy's .")

st.divider()
st.header("Sources and Attributions")

st.markdown("### Propositional LogicBot:")
st.markdown("""**Propositional Logic Jupyter Notebook**  
            [GitHub](https://github.com/norvig/pytudes/blob/main/ipynb/PropositionalLogic.ipynb) | [Google Colab](https://colab.research.google.com/github/norvig/pytudes/blob/master/ipynb/PropositionalLogic.ipynb)  
            _Copyright (c) 2010-2017 Peter Norvig_""")
st.markdown("""**SymPy: Python Library for Symbolic Mathematics**  
            [GitHub](https://github.com/sympy/sympy)   
            Meurer A, Smith CP, Paprocki M, Čertík O, Kirpichev SB, Rocklin M, Kumar A, Ivanov S, Moore JK, Singh S, Rathnayake T, Vig S, Granger BE, Muller RP, Bonazzi F, Gupta H, Vats S, Johansson F, Pedregosa F, Curry MJ, Terrel AR, Roučka Š, Saboo A, Fernando I, Kulal S, Cimrman R, Scopatz A. (2017) SymPy: symbolic computing in Python. _PeerJ Computer Science_ 3:e103 [https://doi.org/10.7717/peerj-cs.103](https://doi.org/10.7717/peerj-cs.103)   
            _Copyright (c) 2006-2023 SymPy Development Team_""")

st.markdown("### Predicate LogicBot 2.0")
st.markdown("""**Natural Language Toolkit (NLTK)**:  
            [GitHub](https://github.com/nltk/nltk)  
            Bird, Steven, Edward Loper and Ewan Klein (2009).
Natural Language Processing with Python.  O'Reilly Media Inc.   
            _Copyright (C) 2001-2024 NLTK Project_""")
