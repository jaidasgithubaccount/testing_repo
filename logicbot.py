import streamlit as st
# functions:

def nlpProcess(userInput):
    from predicatelogic_nlp import preprocess, schematize, streamlitPrems
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


def regexSchema(userInput):
    from propositionlogic_regex import logic
    shortsents = '''If you liked it then you shoulda put a ring on it.'''
    if userInput.lower() == 'd' or userInput.lower() == 'demo':
        userInput = shortsents 
    splitsentences = [sent.lstrip() for sent in userInput.split('.')] # we need to clean our data
    result = logic(splitsentences) # here's our logic answer.
    result = str(result)
    st.session_state.regex_schema = result
    return


def sec25(userprems, userconcl):
    from propositionlogic_regex import section_25
    testpremises = '''If the fish is Kosher then the fish has fins and the fish has scales. If the fish has fins and the fish has scales then the fish is Kosher. If the fish has scales then the fish has fins.''' 
    testconclusion = "If the fish has scales, then the fish is Kosher."
    if userprems.lower() == 'd' or userprems.lower() == 'demo':
        userprems = testpremises
        userconcl = testconclusion
    deliverable = section_25(userprems, userconcl)
    valid = deliverable[0]
    text = deliverable[1]
    st.session_state.regex_sec25 = str(valid) + '\n' + text


def clearregex():
    st.session_state.regex_schema = ''
    st.session_state.regex_sec25 = ''
    return

def clearnlp():
    st.session_state.nlp_prems = ''
    st.session_state.nlp_output = ''
    return

# website:
st.title("LogicBot")
st.header("Argument-strength Analyzer")
st.divider()

st.header("... what's that?")
st.text("The LogicBot uses regular expressions to translate English sentences into Propositional Logic Schemata.")
st.markdown("**Propositional Logic** refers to the logical relationships between phrases that can be true or false, aka *propositions*.")

# PROJECT MOTIVES
st.header("Project Motivations:")

st.markdown('''
1. I'm a __big__ fan of [Warren Goldfarb](https://archive.org/details/deductivelogic0000gold).
2. I was _not_ a fan of having to hand-schematize arguments to check students' work back in undergrad, and less a fan of having to hand-check their proofs.
3. Computational solutions existed to [schematize](https://colab.research.google.com/github/norvig/pytudes/blob/master/ipynb/PropositionalLogic.ipynb) arguments, and to [check if they're valid or satisfiable](https://docs.sympy.org/latest/modules/logic.html), but none of the tools I'd used did _both_.
            ''')

# LOGICBOT 1.0
st.header("First Iteration: LogicBot 1.0 - Propositional Logic")
introduction, legend = st.columns(2)
with introduction:
    st.markdown("As a proof of concept, I started by integrating Peter Norvig's [regular-expression propositional logic code](https://colab.research.google.com/github/norvig/pytudes/blob/master/ipynb/PropositionalLogic.ipynb) with [SymPy](https://docs.sympy.org/latest/modules/logic.html), a Python package that can check schematized arguments for ***satisfiability***.")
    st.markdown("A proposition -- like _P & ~Q_ --  is ***satisfiable*** if there's at least one consistent truth-assignment for all the literals (variables) in the proposition. In this case, if P were True, and Q were False, then _P & ~Q_ would evaluate to True -- this assignment ***satisfies*** that schema.")
with legend:
    st.markdown("Here's a key of the logical operators you'll see on this page:")
    st.markdown("""| Operator | Symbol | Another Form |
| ---------------- | ------ | ---------- |
| NOT              | -      | ~          |
| AND              | •      | &          |
| OR               | v      | \|         |
| THEREFORE        | >      | >>         |
| BICONDITIONAL    | ≡      | << >>          |""")
st.subheader("Try the LogicBot Out:")
st.markdown("The first iteration of the logicbot can (1) 'schematize' english sentences and (2) prove whether a set of premises, as english sentences, imply a conclusion.")
st.markdown("Add your own sentences in English below, or click the 'Demo' buttons to see how the LogicBot works with the given examples!")

schema, col25 = st.columns(2)
with schema:
    # I/O
    st.subheader("Translate English to Logic")
    schemavalue = st.text_input("Input English Sentence:", key="schema_input", placeholder="Example: If you liked it, then you shoulda put a ring on it.")
    one, two, third = st.columns(3)
    with one:
        schema_button = st.button("Translate", help="Click me to schematize this sentence.", use_container_width=True)
        if schema_button:
            regexSchema(schemavalue)
    with two:
        demo_button = st.button("Demo", key="demo_schema", help="Click me to demonstrate!", use_container_width=True)
        if demo_button:
            regexSchema("demo")
    with third:
        delete_button = st.button("Clear All", key=3, help="Click me to clear all fields!", use_container_width=True)
        if delete_button:
            st.session_state.regex_schema = ''
    st.text_area(label="Schematized Sentence(s)", key="regex_schema")
with col25:
    # I/O
    st.subheader("Test if Premises imply Conclusion")
    sec25prems = st.text_area("Input Premise(s):", key="premise_input", placeholder="Example: (1) If the fish is Kosher then the fish has fins and the fish has scales. (2) If the fish has fins and the fish has scales then the fish is Kosher. (3) If the fish has scales then the fish has fins.")
    sec25concl = st.text_input("Input Conclusion:", key="conclusion_input", placeholder="If the fish has scales, then the fish is Kosher.")
    three, four, sixth = st.columns(3)
    with three:
        sec25_button = st.button("Test for Implication", help="Use Goldfarb's Method of Section 25!", use_container_width=True)
        if sec25_button:
            sec25(sec25prems, sec25concl)
    with four:
        demo_button = st.button("Demo", key="demo_sec25", help="Click me to demonstrate!", use_container_width=True)
        if demo_button:
            sec25("demo", "demo")
    with sixth:
        delete_button = st.button("Clear All", key=2, help="Click me to clear all fields!", use_container_width=True)
        if delete_button:
            st.session_state.regex_sec25 = ''
    st.text_area(label="Solved for Validity", key="regex_sec25")

# FURTHER WORK
st.subheader("Further Work: Validity and Soundness")
st.markdown("This logibot checks for vaildity, and will tell you if your arguments' premises don't necessarily imply your conclusion (and the circumstances that poke holes in your reasoning). It can't tell you if a valid argument is in any way ***sound***, or whether its premises are factual.")
st.markdown("""Here's an out-of-the box NLI way to check for soundness, if you dare:  
            1. download the relevant packages and dependencies for [Google's Gemini AI API](https://ai.google.dev/gemini-api/docs)  
            2. run a _model.generate_content()_ call with each proposition (or predicate clause) added as an input to a generic 'is X proposition true?' search query. 
            
But, that'd be computationally intense, and I'm trying to save the planet, so I'm not likely to add a 'soundness verifier' to the LogicBot anytime soon.""")

# LOGICBOT 2.0
st.header("Future Iterations: Predicate Logic (with NLP)")
st.markdown("Future iterations of the LogicBot might utilize natural language processing to determine the ***Universe of Discourse*** and ***Scope of Discourse*** for certain sentences. The Universe of Discourse refers to the kinds of things enclosed by a variable like 'x' in a schema. The Scope refers to whether one refers to *all* elements in the universe, or only *some*.")
st.markdown("Here's how a similar concept might be understood with different scopes of discourse:") 
st.markdown('''
| Type                                     | Sentence                  | Schema       |
| ---------------------------------------- | ------------------------- | ------------ |
| **Propositional Logic (named variable)** | Paul is a firefighter.    | Fp           |
| **Predicate Logic - Existential Scope**  | There is a firefighter.   | (Ǝx)(Fp)     |
| **Predicate Logic - Universal scope**    | Everyone's a firefighter. | (∀x)(x > Fx) |
            ''')
st.caption("""**LITERALS:**   
Fx = x is a Firefighter  
p= Paul""")
st.markdown("... and different universes:") 
st.markdown('''
**Sentence:** All poets in the accelerated program received an A+.

| Universe of Discourse              | Schema                  |
| ---------------------------------- | ----------------------- |
| **Everyone and Every Thing**       | (∀x)(Px ⋀ Qx ⋀ Rx > Sx) |
| **Persons**                        | (∀x)(Qx ⋀ Rx > Sx)      |
| **Poets (*assumed to be People*)** | (∀x)(Rx > Sx)           |
| **Accelerated Program Poets**      | (∀x)(x > Sx)            |          
''')
st.caption("""**LITERALS:**   
Px = x is a Person  
Qx = x is a Poet   
Rx = x is in the Accelerated Program   
Sx = x received an A+    """)
# INPUT TEXT
theysay = st.text_area("Input a sentence here using predicate logic:", placeholder="All smart farmers are either German or Hungarian. Therefore, either somebody smart is not a farmer, or everyone is either German or Hungarian.")
# BUTTONS
five, six, eighth = st.columns(3)
with five:
    schema_button = st.button("Schematize", help="Input text above, and click me to schematize!", use_container_width=True)
with six:
    demo_button = st.button("Demo", key="predicate_demo", help="Click me to demonstrate!", use_container_width=True)
with eighth:
    delete_button = st.button("Clear All", key=4, help="Click me to clear all fields!", use_container_width=True)

if schema_button:
    nlpProcess(theysay)
if delete_button:
    clearnlp()
if demo_button:
    nlpProcess("demo")
# OUTPUT SECTIONS
st.text_area(label="List of Premises and Conclusions", key="nlp_prems")
st.text_area(label="Schematized Argument (_see note_)", key="nlp_output")
st.caption("_NOTE: text has been pre-processed with NLTK's tokenizer and lemmatizer, which is why words are in their neutral/first-person/dictionary-style tense and conjugation. Helpful for future classification down the road!_")
st.markdown("A LogicBot with NLP-type classification might also be able to parse the application of general principles or logical rules as part of one's reasoning - that way, we could add schematized English text as inputs to a natural deduction proof-generator (maybe this one from [mathesis?](https://github.com/ozekik/mathesis/tree/master/mathesis/deduction/natural_deduction)).")

st.divider()

# SOURCES
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
