import streamlit as st
import streamlit.components.v1 as components

# Show title and description.
st.title("Exploring the Culture War 🗺️")
st.page_link("culturewarftp.py", label="Back to Main Page", icon="🌎")
st.header("Graphs, Charts and other Vizualizations", divider="blue")

st.info("Next update in late January!")

# TOPIC MODELING - TABS
st.header("Topic Modeling:")
st.page_link("https://chatbot-2ogvf67n62i.streamlit.app/~/+/culturewarftp#tech-notes", label="Courtesy of BERTopic - see Tech Notes", icon="💻")
documents, explore, topwords, overtime, byclass = st.tabs(["All Comments, Clustered", "Explore Topics", "Topic Keywords", "Topics over Time", "Topics by Subreddit"])

# ALL TOPICS - ALL DOCUMENTS
with documents:
  st.subheader("Redditors' Takes on the Climate Catastrophe")
  st.link_button(label="View Fullscreen", url="https://jaidasgithubaccount.github.io/data_visualizations", help="Recommended: far less scrolling!")
  st.markdown("*This graph visualizes 30 percent of the model's documents, sorted by their semantic similarity to one another, and colored according to the Topic Clusters BERTopic determined they best fit into.*")
  st.markdown("Hover over color-coded clusters to read previews of representative comments. Nodes **near to one another** have **similar literal meanings**; nodes with the :rainbow[same color] discuss the :rainbow[same general topics]. :grey[(Grey comments are outliers!)] Click-and-drag to zoom in. Double-click any topic cluster to isolate it (and double-click the greyed-out topics to undo). Topics are sorted from most to least commonly discussed.")
  components.iframe("https://jaidasgithubaccount.github.io/data_visualizations", height=800, scrolling=True)
  

# ALL TOPICS - EXAMPLE COMMENTS
with explore:
  st.subheader("Explore Topics with Example Comments")
  st.markdown("*I use BERTopic to fit a pre-trained embedding model to a growing corpus of Reddit comments. BERTopic generates **embeddings** for each document, converting text into multi-dimensional vectors, and then runs algorithms to cluster them into 'neighborhoods' of similar topics.*")
  st.markdown("For each topic cluster, BERTopic finds three documents at its 'center:' these are the **Most Representative Documents**. Pick from a topic cluster to read an excerpted anonymous Reddit post that most accurately represents that topic.")
  eradio, docs = st.columns([0.3, 0.7])
  ops = {
  "Economic and Social Collapse": ["""[...] going to Reddit for world news (specifically climate change) is the equivalent of using WebMD to diagnose yourself. There is a lot of truth on there, but all you are going to do is make yourself more anxious by looking at it. What I recommend is looking up reputable sources even if a little bias (BBC, IPCC, etc..) if you are really interested. Do what you can to help and vote for who will help the situation but don't let yourself get caught up in the 'mad max in 30 years' scenario. These scenarios are based on a worst case scenario (and even then its fishy asf) where we don't use technology to help what we have and also assumes we burn the maximum amount of fuels. As the U.S. and other countries make transitions to cleaner energy other developing countries will still be using coal and fuels. It is very likely we will not phase all fuels out in time, but we are also developing technology to help it out. All that's left is for us to vote and stick it to the people who are against green policies. As long as you do what you can rest assured worst case scenarios will be avoided (assuming nothing absolutely crazy irrational happens.) And I'm not saying this to make you complacent, I URGE you to make strides not only to improve yourselves but the world for us and the next generation. Humanity has so much potential, anyone saying it's already lost is lying to themselves. Hopefully I helped someone out with this, I struggled with this for the past 2 or 3 weeks[...]""", "Labor critiques + (anti-) capitalist (predictive) analysis."],
  "Geopolitics": ["""Donald Trump skirted into office by the skin of his teeth and proceeded to spend four years demonstrating to the people who voted for him why that was a fucking terrible idea. A not-unsubstantial number of people that voted for him regretted it. Those that survived the COVID and gave him a second chance regretted even more on Jan 6. And that was before the FBI pulled NUCLEAR SECRETS OUT OF A BATHROOM IN MAR A LAGO.  It took a remarkably effective Russian Psy-Op campaign and an absurdly ill-timed FBI investigation to inch Trump over the finish line in 2016. He lost Congress in 2018, lost re-election in 2020, and is largely responsible for turning the "red wave" of 2022 into more of a sad puddle. He is a loser and has proven track record of being election poison.  The last vestiges of classic establishment Republicans are bailing out of Congress, and intentionally doing so in a way to fuck over the MAGA Republicans as hard as possible. There is a non-zero chance that the GOP will lose control of the house BEFORE the election. Either way,, they're going to have to run campaigns in more districts than they were anticipating.  And now the GOP has given Trump control over the RNC piggybank, which he is using to pay lawyers to keep him out of prison. State level parties in multiple swing states are already crumbling internally as the incompetent MAGA-faithful take control, and now they don't have any money either.  Oh... and Florida just put abortion rights on the ballot. Cause if there's one thing Donald Trump needs right now, it's 30 Electoral votes on the line in the same ballot as the single most effective Democratic turnout issue in the country.""", "(Left-wing) analysis of international relations and the international political economy."],
  "Finances and Economics": ["""I think what people don't get is that billionaires' and even millionaires' money is not in the form of cash in the bank.  It is mainly in the form of mutual funds, stocks, bonds and other financial devices that are traded on Wall Street or internationally.  These are not the same as currency really, except cyptocurrency I guess.  A lot of the value of shares is pure exchange value and is not realized until it is sold.  It should be thought of as imaginary or hypothetical money until it is sold, then it becomes real and is taxed, similar to chips at a casino.    The only reason why people like Bezos can be so rich is because of the stock market.  His fortune is essentially a very large pool of hypothetical money.  If he wants to cash out then all he does is think about how to pay as little tax as possible, then materialize an appropriate amount of money for whatever he wants to do.      The deregulation of Wall Street has led to this obscene 'wealth' and to the financialization of everything in life.  There is virtually no connection between companies' share value and their actual worth as a business as the GameStop bs illustrates. [...] the budgets of city and state governments are made up of financial investment vehicles like municipal bonds that are also publicly traded. The endowments of colleges and universities are also in the form of investments.    Everything in our society is being bought and paid for with chips in a giant casino. Billionaires are a symptom.  Not the cause. Occupy Wall Street was right.""", "How to afford life under climate catastrophe: Users discuss their personal and (inter)national economies."], 
  "Support and Collective Action": ["""Thank you for doing this and sharing this so that when the time comes for the rest of us, we'll remember to have the courage and sense to do the same.""", "Rallying together against the problem."], 
  "Prepper Tools": ["""[…] a 12 year old boy was out galivanting with his friends and put his hand through the window of a building, cutting his wrist down to the tendons and absolutely convincing the kiddo he was about to die. I used my prepped bandaging kit and Most Massively Useful towel (both always in my car) to apply pressure as I calmed him down and waited for paramedics to arrive. ([For what it's worth]: at this point, this TWELVE year old became fixated on how much it was going to cost for the emergency services and hospital visit.) Within ten minutes of coming to his aid, I was back on with my evening, one towel down and a big lump in my throat, thinking how much some kind-hearted leadership is a healing salve in this chaotic, hurting world. I hope this story helps demonstrate how imperative it is to train for high-stress incidents and creative problem-solving--whether passively through "bad" teevee, listening to experts that encourage a RATIONAL, THOUGHTFUL prepping mindset, or taking skill-building courses to improve your programmed response to chaotic conditions... These are instincts which may not come naturally to us. They need developing and continuous honing to be of best use to ourselves and our community.""", "Weapons, first-aid, canned food, and more: tools to prep for collapse."], 
  "Homesteading and Farming": ["""[...] If you genuinely believe that ranchers and farmers are not collapse aware, you are a complete fool. We live the land and we see it and feel it. We are trapped in an imploding system. Just so you are aware, we are also struggling to fill the fridge and pantry. We are not rich. We are not even well off.   Those commenters who chose to be nasty, get a grip. We are all going down. The whole globe is suffering. Don't be such a dick. I'm only someone who shared their experience, I'm not fucking Elon Musk.""", "What to eat: Trad- and anti-trad ideologies clash, but both agree Big Agriculture is evil."], 
  "Collapse Meta-Analysis": ["""Recently there's been a lot of posting about arming up for the collapse of civilization, storing years of food and water, and how to communicate when the cell network goes down.  I don't know who needs to hear this, but that's not necessarily what prepping is really all about. You can try to prepare for all that if you want to, and plenty of folk do. And then they generally end up with years of supplies that they never use, get forgotten about, or get inherited by kids who decide that dad must have been a little overly-anxious towards the end.  I worry that people will come here, see all the talk of guns and bunkers and collapse, and decide that prepping isn't for them. And prepping should be for everyone. So this is a pitch for prepping for Tuesday, not Doomsday, as we say around here.  What's prepping? Having supplies and skills to deal with problems that life throws at you. That's it. That's what being prepped means[...]""", "What causes collapse? How do we save ourselves (and others)? Users discuss."], 
  "Existential Dread": ["""I had a conversation about collapse with a friend. She said “I have no doubt that what you are saying is true, but I'm going to keep living my life the way I am anyways and if we all die, then we die.” It really surprised me at the time and I couldn't understand this attitude.   Now I realize that mental collapse has long since already happened, like decades ago. Most people are hanging on to their lives by a fucking thread. Video games, pornography, television, mindless consumption and social media are literally the only things that keep us going. We're like drug addicts that decided to kill ourselves but figured doing Meth until we OD is more fun than just shooting ourselves. There is no life for the vast majority of people, there is only delayed suicide.  Somewhere in there, I think people realize this. We can't imagine society being any other way than it is. And no one will fight to protect this society because no one truly wants to live in it. We are just enjoying our technological treats while we can. Long since given up on any deeper meaning to our lives. And if we all die, then we die. People don't care and deny collapse because they really and genuinely have no sense at all that their lives are important anymore.""", "Users explore and support one another through the feelings of collapse."], 
  "Medical Prep": ["""I've seen a lot of posts talking about prepping for dentistry / tools to perform procedures / etc.   I want to be frank with you, you really can't treat dental issues on your own- and here's why.   Let's say you have a cavity- you're just going to drill it out and fill it, right?  How will you know when you've gotten all of the decay?  It's often 1/2 a millimeter from the nerve, and if you hit the nerve, the tooth will become infected.  Think about how small 1/2 a millimeter is.  If you leave decay, the tooth becomes infected.    If you don't properly seal the filling, the tooth becomes infected.  How will you fill cavities between teeth without bonding them together?  Drilling a tooth without lots of water will heat it and kill the nerve- the tooth becomes infected.    Try accomplishing all of the above, with water, and without having the patient choke or move.  Ok, so fillings are out- what about an infected tooth?  How are you going to remove it without breaking it?  If you leave a root, it will become infected and never heal.  How will you even know if you got all the roots?  What will you do when it breaks off at the gumline and is encased in solid bone?  I could go on and on.  **My point in all of this is to illustrate that you can't really treat dental issues without the proper training and equipment.  IMO it's a waste of time and money to prep for this.**  [...] In conclusion, just do the annoying shit dentists have been telling you to do your whole life, and try to find a dentist if you can in a SHTF situation.""", "Prepper tools for the next big virus, and medical tips for when the doctors retreat to their bunkers."], 
  "Religion": ["""Good read.  I've been reading a book "Opus" recently, which is a recently released dive into Opus Dei and how that organization grew and spread.  Summary articles like this sometimes miss elements of how the Catholic element of the far right has both been a growing force, and also has been a cornerstone for decades of enduring far right money and influence.  Checking the supreme court, they’re supermajority catholic (including the regressive justices), the push to ban abortion was and is spearheaded by catholics, j d vance is a catholic convert of this strain, there's generally a web of far right catholics at or near the peak of a lot of the political elements of the far right these days, even though most of the laypeople in the movement are protestant.  It's a curious thing, and if they get what they want, I'd imagine the doctrinal differences will matter less - as people like vance clearly show, it's the aesthetics, the connections, and the traditional values these people really value, and in that they have many bedfellows happy to accept them despite significant on paper scriptural differences.""", "Discussion of religion - typically critical of conservative Christianity."], 
  "Abortion, Birth, and Women": ["""This actually has a real answer, and it's a much more interesting answer that I think most people here realize.  It's the same reason why, If you ask a pro-choice American to explain why abortion should be legal, the answer you're going to most likely get will be related to the concept of "**bodily autonomy**," but ask a pro-choice non-American the same thing, and their answer will most likely revolve around the concept of "**family planning**."  First, just to be clear before I say this, I am 100% pro-choice, in all cases and circumstance, prior to birth, I am only trying to communicate a reality here. If you are an average pro-choicer and, let's say, *frequent enjoyer* of social media, you're most likely in a subtle echo-chamber and don't realize that, while access to abortion *in some form* is generally extremely popular among the vast majority of Americans, the idea of using abortion **as a form of birth control** is a waaaay more controversial concept in the US than you think it is. If you don't believe me, ask some pro-choice people you know in real life if they have any circumstances where they do think abortion is immoral. Depending on who you know, you may be very surprised.  For many abortion advocate agencies in the US, it's extremely important to de-emphasize this idea because of how it the idea dampens general support for the right to choose even among liberals. For example, [it's one of the first myth's "debunked" by prochoice.org](https://prochoice.org/wp-content/uploads/women_who_have_abortions.pdf), even though, let's be real, abortion LITERALLY IS, by definition, a form of birth control. and people outside the US and unfamiliar with this controversy are probably scratching their heads at this, because it makes no sense to anyone who isn't super familiar with how weird abortion is for American politics.  TL:DR, because, in the American mainstream, your argument would boil down to "women can just go out and bang a bunch of dudes and then get abortions instead of taking birth control" and that would dampen pro-choice sentiment even among liberals and left leaning voters.   God bless America, amirite?""", "Should you have kids under collapse? Should you even have a say? Users focus on pro-choice and pro-women narratives."], 
  "(Micro)plastics": ["""Sometimes records must be broken.  One area of collapse has been pollution and the accumulation of garbage all over the planet.  There were many that do this, but one that stands out from the rest.  It wasn't Pepsi or Mountain Dew.  Article argues that Coca Cola for the fifth time in the world has been named the worst plastic polluter on the planet.  The results come from Break Free From Plastic National Audit and Coca Cola took the top spot.  There were over 200,000 scientists that came together, looking at beaches and elsewhere around the world to prove these findings.  The United Nations Environment Agency was discussing trying to curb this from last March.  As of now, nothing has really happened in the area of coming to fruition. The New Plastics Economy Global Commitment progress report in 2022 said that its targets set for 2025 will “almost certainly” not be met.  Coca-Cola will continue to greenwash its own image and won't be held accountable.  Coca-Cola itself has yet to respond to this monumental accomplishment.""", "Climate-Redditors know that plastics are the bane of our existence."], 
  "Information-Sharing": [""" [...] [This gigantic resource](https://www.ifixit.org/) of how to fix things is now [available](https://library.kiwix.org/?category=iFixit&q=&lang=eng) for download and offline use, which I think is pretty relevant to preppers.  The current schedule is for quarterly updates. A few categories may be still missing, but that will be fixed over time (if you *do* see something, you are encouraged to report it on the [github repo](https://github.com/openzim/ifixit/issues)).  A huge thank to the people who made this possible, either with their coding skills or their [donations](https://support.kiwix.org/) (because servers run as much on electricity as talent, and Kiwix is a non-profit).  Don't forget also to subscribe to r/Kiwix for other updates (I'm only posting those that seem relevant for prepping here but there's a couple more announcements in the pipe).""", "Users translate documents for one another and share links to one another, bypassing paywalls, firewalls and language barriers."], 
  "Education and Childrearing": ["""Please allow me to illustrate [...] a humorous hypothetical!   For easy math, let's pretend there are exactly 150 students and 300 parents.   Scenario: Cyber attack on the US, power grids and cell networks. The only electronics alive are devices with batteries or attached to a generator, but there's no GPS, wifi, cellular data, or communication at all unless you're a ham radio operator with backup power. (You do you, Jim Bob, mad props.) Even the radio stations are all silent.  **Option 1:** 300 parents know where their kids are. This is the *only* thing they know for sure at this point. Mom and dad may be in different places, but they both know where lil Johnny and Suzie are and go to the school. School is chaotic, but manageable as parents show up, check the roll call of who is present and who was picked up by whom with a listed destination. [...]  **Option 2:** Grid goes down, the school enacts Protocol Yeet your Kids. They run through the drill getting into groups and literally scatter to the the 4 corners of the globe. 300 parents show up at the school and go absolutely fucking batshit because you tell them their kid left with Misses Donahue 2 hours ago and she can barely find her car in the parking lot, much less her way through a newly apocalyptic world with 17 confused and frightened children. But let's say there are 20 teachers, and you have to direct the correct parent for the correct child along each route. Then the spouse shows up and you need to direct them along the correct route for the correct spouse for the correct child. [...] Please, for the love of all things 2022, do not yeet your kids into the wilderness.  *Edit: or worse, the city.*""", "Users discuss the state of the youth; that is, educational policy and childcare during collapse."], 
  "The Caribbean": ["""Someone made a post about testing preps in Haiti [...] I strongly do not recommend or encourage visiting there to test your, “prep.” That is a disgusting and callous thing to say. Innocent people are dying there in greater numbers than before. It is not a place to, “test” your preps. People are starving and desperate. This should not be a place for adventure tourism. Especially since the country speaks Haitian Creole (and depending on where you go from Port au Prince to Jacmel the dialects vary greatly)… and French in and around cities or with the bourgeois. There is no real government there at the moment. Criminal gangs are exploiting the vacuum of government - the gangs of Cité Soleil run rampant. If anybody does not know where that says, it is right near the port, but a collection of hovels controlled by gangs. Any foreigner going there at best would be a hostage for ransom. Again, I strongly do not recommend or encourage visiting there to test your, “prep.” Dear heavens, if someone even went to even Cap Hatien right now talking about preps , they probably would simply kill you because they know you have food.There is a Haitian proverb, 'the full stomach, says this mango has worms, the empty stomach says, *let me see.*'""", "Discussion of environmental and political collapse in the Caribbean. Cuba and Haiti, specifically - two alleged examples of 'collapsed' states."], 
  "'This is Fine'": ["""Don't worry man. I heard on tv from a guy who heard from a company that this is 'fine.'""", "Most of the time they're kidding; other times users are really, truly, going to be okay."], 
  "'Don't Look Up'": ["""It's literally Don't look up. A disaster is about to happen and all we do is fight over who gets to mine it.""", "Remember that movie “Don't Look Up”? Real life is **just** like that."], 
  "Industrial Work": ["""That excavator is still 10 times the size of the reality.""", "Precise measurements in imperial and metric units. Excavators galore. If Bob the Builder cares, it's in this topic."], 
  "After the Power Grid": ["""Allowing people to believe that a clay pot is “magic” and can save your life in a pinch is irresponsible and could literally get somebody killed.  Everything in the universe follows the laws of thermodynamics.  There is no way to “magnify” heat.  Baring a legit miracle, it is just impossible.  A burning candle produces around 80-ish BTU.  A Mr. Heater Buddy produces 9,000 BTU on high.  (Total side note: a sleeping human produces around 360 BTUs.)  So yeah, if you light up 120 candles, you can heat a 200 sq ft room. It will be dangerous as hell, and as a happy side benefit they would absolutely produce enough carbon monoxide to kill you.  Ignoring all the numbers for a moment…  Not everything in science is obvious, but some things can rely on common sense.  Stepping back from the problem for a minute, imagine two rooms… one heated by a candle and the other heated by a single log in a fireplace.  Which one is warmer?  The moral of the story is that if you have no power and it is cold, put on warm clothes, don't forget a hat and socks, and get in bed with blankets. [...] Edit 2: I said you can't heat a room.  But yes, a candle and a pot could make a nice hand warmer.""", "Lighting and Heating without access to the grid. Lots of candles!"],
}
  with eradio:
    selection = st.radio(label="**Topic Clusters**, most to least common", options=ops.keys(), index=None)
  with docs:
    if selection == None:
      selected = "**Pick a Topic Cluster** to view one of the Most Representative Documents in the cluster!"
      subtitle = "..."
    else:
      selected = ops[selection][0]
      subtitle = ops[selection][1]
    st.write("**Topic:** :blue[**{}**]".format(str(selection)))
    st.write("**What users discuss**: *{}*".format(subtitle))
    st.write("**For example:** :gray-background[{}]".format(selected))

# ALL TOPICS - TOP WORDS
with topwords:
  st.subheader("Most Frequent Words in Each Topic")
  st.link_button(label="View Fullscreen", url="https://jaidasgithubaccount.github.io/data_visualizations/topicterms.html", help="Recommended: far less scrolling!")
  st.markdown("*BERTopic also derives the ten most common words in each topic cluster.*")
  st.markdown("Analysis of this data doesn't illuminate much - though this may change in time.")
  components.iframe("https://jaidasgithubaccount.github.io/data_visualizations/topicterms.html", height=500, scrolling=True)

# ALL TOPICS - OVER TIME
with overtime:
  st.subheader("Evolving Discourse - Topics over Time")
  st.link_button(label="View Fullscreen", url="https://jaidasgithubaccount.github.io/data_visualizations/timetopics.html", help="Recommended: far less scrolling!")
  st.markdown("*With the help of Reddit comment timestamps, BERTopic can show the development of different topics over time.*")
  st.markdown("Double-click any topic cluster to isolate it (and double-click the greyed-out topics to undo). Topics are sorted from most to least commonly discussed - mind the scroll bar on the far right, which shows more Topic options.")
  components.iframe("https://jaidasgithubaccount.github.io/data_visualizations/timetopics.html", height=500, scrolling=True)

# TOP TOPICS - BY CLASS
with byclass:
  st.subheader("Comparative Analysis - Topics by Subreddit")
  st.link_button(label="View Fullscreen", url="https://jaidasgithubaccount.github.io/data_visualizations/classtopics.html", help="Recommended: far less scrolling!")
  st.markdown("*We can also bin the Topic clusters by any metric the BERTopic programmers consider a 'class' - in our case, the subreddit the comment came from - for comparative analysis. This graph shows how often each subreddit discusses a given topic compared to the others.*")
  st.markdown("Double-click any topic cluster to isolate it (and double-click the greyed-out topics to undo). Topics are sorted from most to least commonly discussed: all the subreddits talk about :orange[Economic and Social Collapse], but only the r/preppers seem interested in heating their homes via candlelight :red[After the Power Grid]. Go figure.")
  components.iframe("https://jaidasgithubaccount.github.io/data_visualizations/classtopics.html", height=900, scrolling=True)

st.divider()

# TEXT CLASSIFICATIONS
st.header("Text Classification:")

st.markdown("*stay tuned for more visualizations!*")