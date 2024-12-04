"""
Natural Language Processor - This will harness the nltk stuff. Takes different files, returns their information.
by Jaida Hodge-Adams @jaidasgithubaccount
Under Construction - Streamlit Integration is minimal. Sorry for the mess!
"""
# EXTERNAL IMPORTS - this is the dummy <3
import nltk
nltk.donwload('wordnet')
nltk.download('punkt_tab')
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from nltk.tokenize import sent_tokenize
from collections import defaultdict #no keyerrors!

import time

#sample text for debugging
longexample = "If a farmer who owns cows sells milk then he either does not drink it or he takes a loss."
example = "If I go to the movies, I'll bring home popcorn."
validexample = "All smart farmers are either german or hungarian. Therefore, either somebody is not a farmer, or everyone is either german or hungarian."

tag_map = defaultdict(lambda: wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

#global variables (bc idk where to put them yet.)
lemmatizer = WordNetLemmatizer()
multipleSentences = False #used in preprocess function
pargument = [] #processed argument: list of lists. see uses and returns below:
trackerdict = {"eitheror" : 0} #misc. tracking. used in schematize function.
globalsentence = [] # ONLY USED FOR THE WEB-APP.
"""
pargument uses:
preprocess function - pargument is returned as a list of sentences, each themselves a list of words.
schematize function - pargument is returned as a list of premises, each themselves a list of variables and operators.
updateparg - line by line
trickysolve - logic meat.
"""
#
# Getter-and-Setter for Streamlit Integration
#
def getglobalsentence():
    return globalsentence

def setglobalsentence(list):
    globalsentence = list
    return globalsentence 

#
# Actual Functions
#
def preprocess(document):
    document = document.lower()
    "Cleans the document (one string) and returns the cleaned document in our final datastructure" 
    sentences = sent_tokenize(document)
    print("here are this argument's premises in plain english:")
    listPremises(sentences)
    print(sentences)
    for sent in sentences:
        tokens = word_tokenize(sent)
        partsofspeech = pos_tag(tokens)
        psent = [] #each sentence is an array of strings
        for word,tag in partsofspeech:
            lemma = lemmatizer.lemmatize(word, tag_map[tag[0]])
            psent.append(lemma)

        pargument.append(psent) #each document is an array of arrays of strings  
    print("and here's the argument lemmatized:")
    print(pargument)
    
    return pargument 

def listPremises(prems):
    "Quick print to screen - reads off the premises as sentences!"
    tn = len(prems) # this is the index after the final sentence of the argument list.
    header = "" #default.
    count = 0
    if tn != 1:
        multipleSentences = True
        for sent in prems:
            count += 1
            header = 'P' + str(count) if count < tn else 'C' # this will print Premise numbers by each line, and treats the final line as a conclusion.
            print(header + ". " + sent)
    if tn == 1:
        print('P.', prems[0])

#takes an algorithmic approach to schematization: this first one goes sentence by sentence to start.
def schematize(argument):
    # making schemas for a sentence don't require (too much) information from previous sentences. let's have the system start by iterating...
    for i in range(len(argument)): # for each of the sentences in the argument:
        sent = argument[i] # the sentence for the argument
        symbolized = addSymbols(i, sent)
        # add logic to each sentence:
        #schematized = addlogic(i, sent) #adds logic to sentence. has a sub-function for handling tricky logic.
        # then post-process the sentence:
        #postprocessed = postprocess(i, sent) #determines grouping for adding variables
        #print(schematized) #db
        #marked = addvars(i, sent) #adds variables
        #let's see changes!
        #updateparg(i, schematized)
        globalsentence = symbolized
        setglobalsentence(symbolized)
    return globalsentence

def addSymbols(index, sentence):
    # this will work if we get some kind of container for all the indexing information we'll need. let's make a dictionary here:
    metadata = { 'sentence_index':index, 'tricky':False, 'personUD':True, 'scope':False}

    # okay, now we can run our multi-pass process, and we've got a way to pass info through!
    print("simple symbol pass for this sentence:")
    simple = simpleSymbols(sentence, metadata)
    print(simple)

    #if metadata['tricky']:
        #print("going back for trickier logic - complicated conditionals and disjunctions")
        #tricky = trickyLogic(simple, metadata)
    #if metadata['scope']:
        #print("doing a sweep-pass for scope")
       # scope = scopePass(tricky, metadata)
    
    return sentence

def simpleSymbols(sentence, metadata):
    # simplest pass possible.
    # before we do ANYTHING, we gotta check for the the tricky or scope words:
    ezlogic= {
    #conjunctions:
    'and' : ' • ',
    'but' : ' • ',
    '&' : ' • ',
    'because' : ' • ',
    'who' : ' • ',
    #SIMPLE disjunctions (no either-or):
    'or' : ' v ', 
    #not:
    'not' : '-',
    }
    #tricky words that we need to deal with later:
    tricks = ['if', 'only', 'either', 'neither', 'nor'] #if statements need to be evaluated. anything with only needs to be eval-ed as well.
    scopes = ['all', 'everyone', 'every one', 'everybody', 'every', 'some', 'at least one', 'somebody', 'there exists', 'there is'] 
    drop = ['a', 'an', 'do', 'also']

    #some final conditions for sentences:
    scope_open = '' #we need to close a scope before we move to our next sentence.

    # okay, now for each word in the sentence:
    for x in range(len(sentence)):
            #drop unnecessary words:
            if sentence[x] in drop:
                sentence[x] = 'X'
            #substitute easy words:
            if sentence[x] in ezlogic:
                sentence[x] = ezlogic[sentence[x]]
            # mark tricky words:
            if sentence[x] in tricks:
                #print("needs a tricky solve for " + sentence[x]) 
                metadata['tricky'] = True # update this metadata.
            # mark scope words:
            if sentence[x] in scopes:
                #print("needs a scope-pass for " + sentence[x])
                metadata['scope'] = True
            
    return sentence

def trickyLogic(sentence, meta):

    return

def scopePass(sentence, meta):
    #universal and existential scopes:
    uniscope = {
    'all' : '(∀x)(', 'everyone' : '(∀x)(', 'every one' :'(∀x)(', 'everybody' : '(∀x)(', 'every' : '(∀x)(', # universal
    }
    exiscope = {
    'some' : '(Ǝx)(', 'at least one' : '(Ǝx)(', 'somebody' : '(Ǝx)(', 'someone' : '(Ǝx)(', 'there exists' : '(Ǝx)(', 'there is' : '(Ǝx)(' #existential
    }
    #tricky words that we need to deal with later:
    tricks = ['if', 'only', 'either', 'neither', 'nor'] #if statements need to be evaluated. anything with only needs to be eval-ed as well.
    scopes = ['all', 'everyone', 'every one', 'everybody', 'every', 'some', 'at least one', 'somebody', 'someone', 'there exists', 'there is'] 
    drop = ['a', 'an', 'do', 'also']

    #some final conditions for sentences:
    scope_open = '' #if scope, we need to close a scope before we move to our next sentence.
    
    tricky = False #if tricky, we've got conditionals to handle.
    personUD = False #if the universe of discourse is persons, words like everyone and everybody are handled differently

    # okay, now for each word in the sentence:
    for x in range(len(sentence)):
            #first check for universal scope
            if sentence[x] in uniscope:
                if sentence[x] == 'everyone' or sentence[x] == 'everybody': # universal persons UD
                    personUD = True
                scope_open = 'uni'
                sentence[x] = uniscope[sentence[x]]
            #then check for existential scope:
            elif sentence[x] == 'there':
                if sentence[x + 1] == 'be':
                    scope_open = 'exi'
                    sentence[x] = '(Ǝx)('
            #secondary check
            elif sentence[x] in exiscope:
                if sentence[x] == 'someone' or sentence[x] == 'somebody': # existential persons UD
                    personUD = True
                scope_open = 'exi'
                sentence[x] = exiscope[sentence[x]]
            #handle definite articles: COMMENTED OUT
            # elif sent[x] in defiscope:
            #     sent[x] = defiscope[sent[x]]
            #     scope_open = 'def'
            #drop unnecessary words:
    return

def addlogic(i, sentence):
    #operators:
    ezlogic= {
    #conjunctions:
    'and' : ' • ',
    'but' : ' • ',
    '&' : ' • ',
    'because' : ' • ',
    'who' : ' • ',
    #disjunctions:
    'or' : ' v ', 
    #not:
    'not' : '-',
    }
    #universal and Existential, and Definite Scope variables:
    uniscope = {
    'all' : '(∀x)(', 'everyone' : '(∀x)(', 'every one' :'(∀x)(', 'everybody' : '(∀x)(', 'every' : '(∀x)(', # universal
    }
    exiscope = {
    'some' : '(Ǝx)(', 'at least one' : '(Ǝx)(', 'somebody' : '(Ǝx)(', 'there exists' : '(Ǝx)(', 'there is' : '(Ǝx)(' #existential
    }
    # reversals
    #TODO: definite article support: needs to be fleshed out.
    defiscope = {
        'the' : '(λx)('
    }
    #tricky words that we need to deal with later:
    tricks = ['if', 'only', 'either', 'neither', 'nor'] #if statements need to be evaluated. anything with only needs to be eval-ed as well.
    #a list of words that get immediately dropped.
    drop = ['a', 'an', 'do', 'also'] 

    #some final conditions for sentences:
    scope_open = '' #we need to close a scope before we move to our next sentence.
    trickinfo = [] #we've got a weird either-of situation to handle
    tricky = False #we've got conditionals to handle.
    personUD = False #if the universe of discourse is persons, words like everyone and everybody are handled differently

    for x in range(len(sentence)):
            #first check for universal scope
            if sentence[x] in uniscope:
                if sentence[x] == 'everyone' or sentence[x] == 'everybody':
                    personUD = True
                scope_open = 'uni'
                sentence[x] = uniscope[sentence[x]]
            #then check for existential scope:
            elif sentence[x] == 'there':
                if sentence[x + 1] == 'be':
                    scope_open = 'exi'
                    sentence[x] = '(Ǝx)('
            #secondary check
            elif sentence[x] in exiscope:
                scope_open = 'exi'
                sentence[x] = exiscope[sentence[x]]
            #handle definite articles: COMMENTED OUT
            # elif sent[x] in defiscope:
            #     sent[x] = defiscope[sent[x]]
            #     scope_open = 'def'
            #drop unnecessary words:
            if sentence[x] in drop:
                sentence[x] = 'X'
            #then check for easy logical words
            if sentence[x] in ezlogic:
                sentence[x] = ezlogic[sentence[x]]
            # then solve for trickier logical words:
            if sentence[x] in tricks:
                #print("needs a tricky solve for " + sent[x]) #db
                tricky = True
                trickinfo.append([sentence[x], i, x]) #add a list to the list - word, index of sentence, index of word.
            #if we're within a scope, we need to close it.
            #TODO simplify this.
            if scope_open == 'uni':
                #to be --> conditional
                if sentence[x] == 'be':
                    if personUD:
                        sentence[x] = 'X'
                    if not personUD:
                        sentence[x] = ' > '
                #close the scope
                if sentence[x] in exiscope:
                    sentence[x] += ')'
                    scope_open == '' #reset. close that scope
            elif scope_open == 'exi':
                # to be --> ignore
                if sentence[x] == 'be':
                    sentence[x] = 'X'
                if sentence[x] in uniscope:
                    sentence[x] += ')'
                    scope_open == '' #reset. close that scope
            elif scope_open == 'def':
                close = ['be', 'then'] #TODO: means test. is this a comprehensive list?
                if sentence[x] in close: 
                    sentence[x] == ') • '

    #end of sentence: final housekeeping
    if scope_open:
        sentence[-1] = ')'
    if tricky:
        trickysolve(trickinfo) #sends along a dictionary of all the tricky words in this sentence and their place.

    return sentence

#updates a line of the argument. returns the previous version for debugging
def updateparg(index, updated):
    old = pargument[index]
    pargument[index] = updated
    return old

#making this too complicated. simplify, please <3
#debug print statments tagged #db 
def trickysolve(trickinfo):
    sindex = 0 # i = the index of the sentence within the full argument
    windex = 0 # x = the index of the word within the sentence
    #get new indices
    #for each mention of a tricky word:
    for trick in trickinfo:
        trickyword = trick[0]
        sindex = trick[1]
        windex = trick[2]
        sentence = pargument[sindex]
        word = sentence[windex]
        # print(sentence) #db
        # print("because we found the word " + trick[0])
        startofSentence = True if windex == 0 else False


        #if that tricky word is either:
        if trickyword == 'either':
            #either x or y --> (x) v (y) 
            sc_open = False
            openpars = False
            #parens check:
            dist = -1
            if sentence[windex + 1] == '(Ǝx)(' or sentence[windex + 1] == '(∀x)(' or sentence[windex + 1] == '(λx)(':
                        #print('found a scope: ' + sentence[windex + 1]) #db
                        sc_open = True
            for idx in range(windex, len(sentence)): #for each literal after the first mention of either in the sentence - 
                #first stopping criteria - we find our ending point:
                #print("evaling " + sentence[idx]) #db
                if sentence[idx] == ' v ' or sentence[idx] == 'or':
                    #print('stopping. dist between ' + sentence[windex] + " and " + sentence[idx] +  " is still " + str(dist)) #db
                    #if we've got enough clauses:
                    if dist >= 3:
                        #check for these starting symbols - if none, then add open parens:
                        if not sc_open:
                            ender = sentence[windex + 1]
                            sentence[windex + 1] = '(' + ender
                            #print('added open parens.') #db
                            openpars = True
                        else:
                            continue
                            #print('no need to add open parens.') #db
                        #close the parens at the endpoint:
                        if sentence[idx + 1] == '(Ǝx)(':
                            sentence[idx] = ') v'
                        elif sentence[windex + 1] == '(∀x)(':
                            sentence[idx] = ') v'
                        elif sentence[windex + 1] == '(λx)(':
                            sentence[idx] = ') v'
                        elif sc_open:
                            sentence[idx] = ') v ('
                        else:
                            sentence[idx] = ') v ('
                        #delete the pesky 'either':
                        sentence[windex] = 'X'
                        dist = -1 #reset distance counter.
                    #if we need to close the scope here.
                    elif sc_open:
                        sentence[idx] = ') v'
                    #if we didn't have enough clauses, nor a scope to handle:
                    elif not sc_open:
                        #print('no parentheses opened') #db
                        sentence[windex] = 'X'
                        #print(sentence) #db
                    #print("next tricky word") #db
                    break
            if sentence[idx] == '.':
                if openpars:
                    sentence[idx] = ')'  
            #no stop - iterate on distance.
            elif sentence[idx] != 'X' and sentence[idx] != '-' and sentence[idx] != ',': #ignoring non-literals
                dist +=1
                #print('dist between ' + sentence[windex] + " and " + sentence[idx] +  " == " + str(dist)) #db
           
            #at sentence end, regardless: replace the mention of either with an X.
            sentence[windex] = 'X'

            #either of:
            #either of you two.... will...
            mark1 = -300
            mark2 = -200
            for idx in range(windex, len(sentence)):
                if sentence[idx] == 'of':
                    #mark this starting point:
                    mark1 = idx
                    #print('marking from ' + mark1) #db
                    continue
                #triggers for figuring out who the "either of" group is.
                if sentence[idx] == 'be' or sentence[idx] == 'will':
                    mark2 = idx
                    #print('marking until ' + mark2) #db
            #print these strings:
            if mark1 > 0 and mark2 > 0:
                for idx in range(mark1, mark2 + 1):
                    #print(idx, sentence[idx]) #db
                    text = ' '.join(sentence[idx])
                #print("should need to handle:", text) #db

        #handling if:
        #TODO: need to copy parentheses structure from above. also maybe we need a way to bundle/package the string so we can move clauses around
        if trickyword == 'if':
            if startofSentence:
                #look for a then or a comma:
                for then in range(windex, len(sentence)):
                    if sentence[then] == 'then' or sentence[then] == ',':
                        sentence[windex] = 'X'
                        sentence[then] = ' > '
            else: #not the start of the sentence
                #check if previous word is only:
                if sentence[windex - 1] == 'only':
                    continue #this is only if. we'll handle it below.

        #handling only:
        if trickyword == 'only':
            if startofSentence:
                #only if x then(will/does) y --> y only if x --> y then x
                startx = 0
                endx = 0
                nextindex = windex + 1
                if sentence[nextindex] == 'if':
                    startx = nextindex #start of the x statement
                    for idx in range(nextindex, len(sentence)):
                        if sentence[idx] == 'then':
                            endx = idx
                    x = []
                    curr = startx - 1
                    while curr <= endx:
                        x.append(sentence[curr])
                    #print(x) #db
                    #take all the words between the start and end point here for x, switch them with the words for y, and then put the conditional.

                #only x are y --> if y then x 


    return

def postprocess(i, sent):
    sentenceindex = i
    #sent is a list of terms
    post = [] #post-processeed list.
    text = '' #intermediate text
    #make the text by removing all unwanted characters:
    for sym in sent:
        if sym != 'X' and sym != ',' and sym != '.':
            text += sym + ' '
    newl = text.split()
    print(text)
    openparens = ['(', '(Ǝx)(', '(∀x)(', '(λx)(']
    closeparens = ')'
    operators = ['v', '•', '≡', '>', '-']

    #init tagger:
    tagged = nltk.pos_tag(newl) #tuple of words and their tags.
    #update tagger:
    for x in range(len(tagged)):
        if tagged[x][0] in openparens:
            tagged[x] = (tagged[x][0], 'OPEN')
        if tagged[x][0] == closeparens:
            tagged[x] = (tagged[x][0], 'CLOSE')
        if tagged[x][0] in operators:
            tagged[x] = (tagged[x][0], 'LOG')
    print(tagged)
    nounphrase = ("NP: {<DT>?<JJ>*<NN>}")
    #grouping rules:
    return

def addvars(i, sent):
    sentenceindex = i
    #sent is now a well-grouped list of terms
    final = []
    finalstring = ""


