from transformers import pipeline

summarizer = pipeline('summarization')

article = """Senate Majority Leader Chuck Schumer’s attempt to give Democrats more opportunities to pass legislation with a simple majority of votes has been granted by the Senate parliamentarian, according to his office.

The favorable ruling by Elizabeth MacDonough, who oversees Senate procedure, means the New York Democrat will have an extra chance to pass a bill with 51 votes this year. The ruling is good news for Democrats’ agenda, much of which faces fierce GOP opposition. 

“This confirms the Leader’s interpretation of the Budget Act and allows Democrats additional tools to improve the lives of Americans if Republican obstruction continues,” a Schumer spokesperson said in a statement. “While no decisions have been made on a legislative path forward ... and some parameters still need to be worked out, the Parliamentarian’s opinion is an important step forward that this key pathway is available to Democrats if needed.”

Schumer’s aides argued last week that the budget reconciliation process Democrats used to pass their $1.9 trillion coronavirus relief bill unilaterally last month allows for additional opportunities to advance their agenda. Their argument hinged on a provision in the Congressional Budget Act that allows Congress to “revise” its most recently passed budget resolution.

With the favorable ruling, Democrats can potentially pass multiple spending bills with a simple majority, allowing them to circumvent Republicans on other issues that affect the federal budget such as climate, health care and taxes. 

"""

print(summarizer(article, max_length=130, min_length=10, do_sample=False))



