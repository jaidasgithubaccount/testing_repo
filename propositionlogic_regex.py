"""
Propositional Logic Bot - this is the container file with the streamlit integration and also will send information to other modules!

ATTRIBUTIONS
Propositional Logic Functions and Methods - Copyright (c) 2010-2017 Peter Norvig
Sympy - Copyright (c) 2006-2023 SymPy Development Team
"""
# EXTERNAL IMPORTS - if my predlogic one is to be believed, this is the one that's driving the boat
import sympy
from sympy import Symbol # for making your own symbols out of strings (transforms strings into Symbol class instances)
from sympy.logic import And, Or, Not, Implies
from sympy.logic.inference import satisfiable # this is really the only thing we're checking for.
import re # regular expressions - PropLogic.ipynb import
import textwrap
from sympy.parsing.sympy_parser import parse_expr

# TEXT BLOBS - TO BE PROCESSED
shortsents = '''
If you liked it then you shoulda put a ring on it.
Either Danny didn't come to the party or Virgil didn't come to the party.
A ham sandwich is better than nothing 
  and nothing is better than eternal happiness
  therefore a ham sandwich is better than eternal happiness.
'''

peters_sentences = '''
Polkadots and Moonbeams.
If you liked it then you shoulda put a ring on it.
If you build it, he will come.
It don't mean a thing, if it ain't got that swing.
If loving you is wrong, I don't want to be right.
Should I stay or should I go.
I shouldn't go and I shouldn't not go.
If I fell in love with you,
  would you promise to be true
  and help me understand.
I could while away the hours
  conferrin' with the flowers,
  consulting with the rain
  and my head I'd be a scratchin'
  while my thoughts are busy hatchin'
  if I only had a brain.
There's a federal tax, and a state tax, and a city tax, and a street tax, and a sewer tax.
A ham sandwich is better than nothing 
  and nothing is better than eternal happiness
  therefore a ham sandwich is better than eternal happiness.
If I were a carpenter
  and you were a lady,
  would you marry me anyway?
  and would you have my baby.
Either Danny didn't come to the party or Virgil didn't come to the party.
Either Wotan will triumph and Valhalla will be saved or else he won't and Alberic will have 
  the final word.
Sieglinde will survive, and either her son will gain the Ring and Wotan’s plan 
  will be fulfilled or else Valhalla will be destroyed.
Wotan will intervene and cause Siegmund's death unless either Fricka relents 
  or Brunnhilde has her way.
Figaro and Susanna will wed provided that either Antonio or Figaro pays and Bartolo is satisfied 
  or else Marcellina’s contract is voided and the Countess does not act rashly.
If the Kaiser neither prevents Bismarck from resigning nor supports the Liberals, 
  then the military will be in control and either Moltke's plan will be executed 
  or else the people will revolt and the Reich will not survive'''.split('.')

pitfallpremises = '''
If a fish is Kosher then the fish has fins and the fish has scales.
If a fish has fins and the fish has scales then the fish is Kosher.
If a fish has scales then a fish doesn't not have fins. '''
pitfallconclusion = "If a fish has scales, then the fish is Kosher."

testpremises = '''
If the fish is Kosher then the fish has fins and the fish has scales.
If the fish has fins and the fish has scales then the fish is Kosher.
If the fish has scales then the fish has fins. ''' 
testconclusion = "If the fish has scales, then the fish is Kosher."

# FUNCTIONS 
"""
Excerpted from PropositionalLogic.ipynb (MIT License Copyright (c) 2010-2017 Peter Norvig). Many Thanks to Peter for his brain. I did make two changes to the Rules/Regex - changing the symbols for AND (&), OR (|), and NOT(~), and I modified his 'logic' module for the main driver of the sympy code. 
"""

def Rule(output, *patterns):
    "A rule that produces `output` if the entire input matches any one of the `patterns`." 
    return (output, [name_group(pat) + '$' for pat in patterns])

def name_group(pat):
    "Replace '{Q}' with '(?P<Q>.+?)', which means 'match 1 or more characters, and call it Q'"
    return re.sub('{(.)}', r'(?P<\1>.+?)', pat)
            
def word(w):
    "Return a regex that matches w as a complete word (not letters inside a word)."
    return r'\b' + w + r'\b' # '\b' matches at word boundary

rules = [
    Rule('{P} >> {Q}',         'if {P} then {Q}', 'if {P}, {Q}'),
    Rule('{P} | {Q}',          'either {P} or else {Q}', 'either {P} or {Q}'),
    Rule('{P} & {Q}',          'both {P} and {Q}'),
    Rule('~{P} & ~{Q}',       'neither {P} nor {Q}'),
    Rule('~{A}{P} & ~{A}{Q}', '{A} neither {P} nor {Q}'), # The Kaiser neither ...
    Rule('~{Q} >> {P}',        '{P} unless {Q}'),
    Rule('{P} >> {Q}',          '{Q} provided that {P}', '{Q} whenever {P}', 
                               '{P} implies {Q}', '{P} therefore {Q}', 
                               '{Q}, if {P}', '{Q} if {P}', '{P} only if {Q}'),
    Rule('{P} & {Q}',          '{P} and {Q}', '{P} but {Q}'),
    Rule('{P} | {Q}',          '{P} or else {Q}', '{P} or {Q}'),
    ]

negations = [
    (word("not"), ""),
    (word("cannot"), "can"),
    (word("can't"), "can"),
    (word("won't"), "will"),
    (word("ain't"), "is"),
    ("n't", ""), # matches as part of a word: didn't, couldn't, etc.
    ]

def match_rules(sentence, rules, defs):
    """Match sentence against all the rules, accepting the first match; or else make it an atom.
    Return two values: the Logic translation and a dict of {P: 'english'} definitions."""
    sentence = clean(sentence)
    for rule in rules:
        result = match_rule(sentence, rule, defs)
        if result: 
            return result
    return match_literal(sentence, negations, defs)
        
def match_rule(sentence, rule, defs):
    "Match rule, returning the logic translation and the dict of definitions if the match succeeds."
    output, patterns = rule
    for pat in patterns:
        match = re.match(pat, sentence, flags=re.I)
        if match:
            groups = match.groupdict()
            for P in sorted(groups): # Recursively apply rules to each of the matching groups
                groups[P] = match_rules(groups[P], rules, defs)[0]
            return '(' + output.format(**groups) + ')', defs
        
def match_literal(sentence, negations, defs):
    "No rule matched; sentence is an atom. Add new proposition to defs. Handle negation."
    polarity = ''
    for (neg, pos) in negations:
        (sentence, n) = re.subn(neg, pos, sentence, flags=re.I)
        polarity += n * '~'
    sentence = clean(sentence)
    P = proposition_name(sentence, defs)
    defs[P] = sentence
    return polarity + P, defs
    
def proposition_name(sentence, defs, names='PQRSTUVWXYZBCDEFGHJKLMN'):
    "Return the old name for this sentence, if used before, or a new, unused name."
    inverted = {defs[P]: P for P in defs}
    if sentence in inverted:
        return inverted[sentence]                      # Find previously-used name
    else:
        return next(P for P in names if P not in defs) # Use a new unused name
    
def clean(text): 
    "Remove redundant whitespace; handle curly apostrophe and trailing comma/period."
    return ' '.join(text.split()).replace("’", "'").rstrip('.').rstrip(',')

"""
MIT License

Copyright (c) 2010-2017 Peter Norvig

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


"""
My work: Method of Section 25 (checking for satisfiability of premises and negated conclusion)
"""

parsehelp = { # so sympy can recognize the boolean algebra when it attempts to parse my text.
    "&" : Symbol("&"), # AND
    "|" : Symbol("|"), # OR
    '~' : Symbol('~'), # NOT
    "Q" : Symbol("Q"), # Q is a special character ?
    "S" : Symbol("S"), # I fear S is, too.
}

# basic implementation of Goldfarb's method. returns True or False if valid/invalid, and an assignment that proves invalidity if so.
def section_25(premises, conclusion):
    deliverable = [] # easy passing through diff python files
    defs = {} # local variable so that we can keep track of our definitions
    valid = False
    printoff = "" # text with the info!
    # these lists will host Sympy Symbol and String lists of all of the clauses (premises + conclusion).
    sec25 = []
    string25 = []
    # input sentences must be separated by periods. And let's leave IFF out of it. see the Demo for more:
    splitpremises = [sent.lstrip() for sent in premises.split('.')] # list of all cleaned sentences

    # might need to check for some blank elements (in the case that there's only 1 premise)
    for x in splitpremises:
        if x == "" or x == " ":
            splitpremises.remove(x) # we literally do not need that drama.
    # first, we schematize all of our premises:
    for sentence in splitpremises:
        logic, defs = match_rules(sentence, rules, defs)
        parsed = parse_expr(logic, local_dict=parsehelp) # parse as sympy
        sympy_premise = sympy.logic.boolalg.to_nnf(parsed)# turn into nnf (easier!)
        # add parsing to list:
        #sec25 += (sympy_premise,)
        sec25.append(sympy_premise)

    # and we'll do the same for our conclusion, except section 25 calls for us to negate it:
    conclogic, defs = match_rules(conclusion, rules, defs)
    parsedconcl = parse_expr(conclogic, local_dict=parsehelp) # parse as sympy
    sympy_conclusion = sympy.logic.boolalg.to_nnf(parsedconcl)
    # add to the list:
    negated_conclusion = Not(sympy_conclusion)
    sec25.append(negated_conclusion)
    
    # we need to cast the literals as a string, concatenate them wtih he ampersand &, and then parse that string 
    # as an equation in order to access sympy's satisfiable() method without the command line 
    # (another solution would implement the os python package!)
    for clause in sec25:
        string25.append("({})".format(str(clause)))
    # we're connecting the clauses byt the & operation, and then parsing  ' & ' situation to our string:
    string25 = ' & '.join(string25)
    parsed_sec25 = parse_expr(string25, local_dict=parsehelp)
    test = satisfiable(parsed_sec25) # this is our method test. thank you sympy!!

    if test:  # if P & -Q is satisfiable, then P > Q is not valid:
        valid = False
        print(test)
        # now print off the schema:
        if test == {True: True}:
            printoff = "Schema is unsatisfiable."
        # under most conditions:
        else:  
            rip = "Schema is invalid. Under these conditions, the Premise(s) do(es) not imply the Conclusion:\n" # print statement
            for key, value in test.items(): # assuming this is allowed...
                fulltext = defs[str(key)] # check the definitions dictionary for the full English text of this literal.
                rip += "[{}] {} : {}\n".format(key, fulltext, value)
            printoff = rip

    elif not test:  # if P & -Q is unsatisfiable, then P > Q is valid:
        valid = True
        printoff = "Schema is valid."
    
    deliverable = [valid, printoff]
    return deliverable

# This is modified from Peter Norvig's implementation of the schematizer. Copyright (c) 2010-2017 Peter Norvig!!
def logic(sentences):
    defs = {} 
    total = ""
    "Match the rules against each sentence in text, and print each result."
    for s in sentences:
        if s == '.' or s == '':
            continue
        logic, defs = match_rules(s, rules, defs)
        sentence = "\nEnglish: " + s + "." + "\nLogic: " + logic
        for P in sorted(defs):
            sentence += "\n{}: {}".format(P, defs[P])
        total += sentence
    return total


def getpremises_conclusion():
    both = [testpremises, testconclusion]
    return both