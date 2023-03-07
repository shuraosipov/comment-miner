
import os
import sys
import openai
import json
from tqdm import tqdm
import itertools
from collections import defaultdict

from comments_in_batches import comments
#from comments_in_batches_small import comments


# Set up OpenAI API credentials
openai.api_key = os.environ.get("OPENAI_API_KEY")


def analyze_comments_v2(comments: str) -> str:
     insights = []
     completion = openai.ChatCompletion.create(
        
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant, you are responsible for analysis of the comments for the latest YouTube video from Lex Fridman channel, discovering insigths and providing insteresting information.",
            },
            {
                "role": "user",
                "content": f"""
                Please analyse commments below and provide insights.
                Ensure insights are unique and they are not duplicated in multiple sections.
                
                Your response should be in JSON format, value should be a list of strings like this ['comment1', 'comment2']:
                             
                "feedback_and_constructive_criticism": []
                "engagement_and_interaction": []
                "ideas_and_suggestions": []
                "textual_summary_of_all_comments": []
                "most_positive_comments": []
                "most_negative_comments": []
                "suggesstion_for_new_guests": []
                "insights": []
                "fun_comments": []

                {comments}""",
            },
        ],
        )
     return json.loads(completion["choices"][0]["message"]["content"])


#comments = """['I figured in 2007 that I should hire for curiosity and learning skills. Nothing else matters. Good to see that others getting it. 14:54', '❤🤓 An inspiring podcast! Lex always brings around great personalities across diverse backgrounds! Look forward to more social, political, scientific, biotechnology fields topics coverage! I worked at IBM India - Mumbai for some years! A great organisation with work ethics, innovative leadership, and good culture team! I learnt a lot in the industry! 😊👍', 'my dad was essentially laid off after 23 years at ibm because they were  bringing in cheap labour from india', 'Emotionally , intellectually moving - Lex F. landies and gentlemen. \n\n\n\n\nThank you for shining a light on this rare shiny that I have added to my pokedex Lex.', 'As a female engineer and manager I am very thankful, that you provide such a variety of interviewpartners. I learn about people I would otherwise never have and being able to listen to them in such a longform and with you always being so genuinly interested and gentle in your dialogue is incredibly enriching to me. Thank you.', 'B team podcast when?', '36:52 "Paralyzation"\n1:36:22 "Remindful"', "What happened to the liquid computer system IBM was working on.\n\nFor some reason I can't get any more information on that system IBM built", 'This was a good one. I listened to the whole thing twice', "So beautiful...., Thank you so much for you're transparnty, openess, love, honesty....questions and answers but most off all  intentions. This intention❤ you create everytime. It's magical. Thank you so much.Bless you.", 'Why is it that he asks the question “what’s the meaning of life” to some people and not to others?', 'How do i double-thumbs up?', 'This lady really knows how to talk herself up. You would think the world would collapse of it wasn’t for her', 'Best sentence in this podcast for every leader: "Just because you can point out something doesn\'t mean you should"\nWorst sentence in this podcast: "Do you think a man would have said that they need to think about getting that promotion" \n\nGinni, you have no idea about how many men are insecure in their jobs. How many talks I had with folks I wanted to promote to the next level because I know they can do it who told me they do not want it because they are insecure. This is a human problem, not a woman problem.', "*What a great video 👏!*\n*😊$60, 200 returns from my $7,000 investment every 14days, I can't keep my mouth shut*", '"You did a lovely job". She\'s not going to hire him.😅', 'She’s phenomenal & wonderful.', 'Can we get Jordan Maxwell on this Podcast, please 🐱', 'such a fantastic podcast and a powerful conversation thankyou', 'Love everything about this discussion. Only thing I take issue with is accepting the excuse of “it’s just a really hard problem” for negligence.', 'Business stuff is so boring and depressing to me.', 'Very beautiful, to both of you! And, I thank you for shedding light to those of us that tether tenaciously to the hope in seeing the light in the darkest of times. Know that you both have been, are, and continue to be my light in this physical world. May you always be blessed by the entire universe. Again, thank you, from the bottom of MY heart. ❤🌈.', 'Am I the only one hearing very annoying audio dropouts here then?', '“All-in” community is waiting for you to invite Friedberg and Sachs. \n\nPlease do. They are great characters', 'I only 15 mins in and can’t believe all the misinformation and incorrect statements.     I won’t say lies,   But cut management levels in half.  No way.   2 in 10 had skills for the future.  In who’s opinion?   IBM wouldn’t have know what the skills were needed.      All the software at IBM is cloud and AI.   NO way.', 'Great interview, but my sense is Lex didn’t enjoyed it. She is a very strong character and “my way or highway “ type of person. A lot of push and pull. Great interview.', 'Wow.  You need some quality control, lex.  I’m ex-ibm and know the company’s history really well.  With the possible exception of Lou Gerstner they haven’t had a decent ceo since Watson jr.   rometty was one of a long line of mediocrities.  The company circled the drain while she ran it and was no better when she left than it had been when she was handed the keys.  You and your producer need to do some more research on your guests.', 'Female presidential candidate.', 'lex hair is a mess, did he sleep in the studio again?', 'Boring and unrelateable. Speaking in corporate-ese .just hours of empty boss speak.', 'Saddest words I will say:  Lex - du  bist .', 'Very inspiring and came at a perfect time for me, thank you ❤️', 'Does IBM ever hire people who are not from India?', 'Excellent interview!', 'Thank you', '😆', 'This person is a criminal.. Ibm biggest scammers going', 'Love your interviews. This was one of your best. You are the thinking persons Michael Parkinson !!', 'Really enjoyed this ❤', "Amazing podcast! I've worked at IBM for 10 years and she's really inspiring! And you always know how to extract the best of each person! Thanks for doing it!", "One of the greatest conversations I've listened to in my life. Thank you Lex, you give the right people the right platform.", 'Wow, such an enlightened person Ginni Rometty is, not in a spiritual sense but in a practical sense. I really enjoyed listening/watching her talking. So inspiring, thank you for this Lex. "In the beginner\'s mind there are many possibilities, in the expert\'s mind there are few." - Shunryu Suzuki (a Zen Master)', 'Great podcast! Would love to see more insights from various CEOs on their philosophies.', 'The best of the best. She is asking him questions to get to say what she thinks needs to be said. Both true professionals teaching and learning together everyday all day.', 'Lex contact me when you get a chance', 'Wonderful Interview.  Lots to take away in how we think about management and AI.', '1:39:38 as bayrakları as 🦃🦃🦃', "Can you imagine Ginny's black book contact list, some gal. Lex played to her softer side which created a soft flowing interview, with some great gold nuggets thrown in. And yet there is steel inside both of you, power does not have to look one way, comes in many ways. If you ever want a CEO job Lex you are not short of contacts. But would you want it? Truly.", '@Lex Fridman \nAre you okay? I saw your message on Twitter but have been locked out (for various reoccurring reasons). What happened?\nHoping you are well & happy. Sending ❤️ your way.']"""


number_of_batches = len(comments)
num_comments_per_batch = [len(batch) for batch in comments]
total_num_comments = sum(num_comments_per_batch)

# print(number_of_batches)
# print(num_comments_per_batch)
# print(total_num_comments)


# run analysis for first batch
# dicts = [
#     {'feedback_and_constructive_criticism': [], 'engagement_and_interaction': [], 'ideas_and_suggestions': [], 'appreciation_and_encouragement': [], 'opportunities_for_collaboration_or_partnerships': [], 'textual_summary_of_all_comments': "The comments cover some diverse topics such as engineering, power and responsibility, and IBM's support for Nazi Germany.", 'most_positive_comments': [], 'most_negative_comments': [], 'suggesstion_for_new_guests': [], 'insights': 'The comments suggest that several viewers have conflicting opinions about IBM, with one viewer citing its support for Nazi Germany, while another viewer seems to be defending the company. The comments also highlight the importance of responsibility in positions of power.', 'fun_comments': []},
#     {'feedback_and_constructive_criticism': [], 'engagement_and_interaction': ["Almost no commenter here judges women CEOs on merit. It's 2023 people.", 'Check your comment for gender inequality please.'], 'ideas_and_suggestions': [], 'appreciation_and_encouragement': [], 'opportunities_for_collaboration_or_partnerships': [], 'textual_summary_of_all_comments': 'The comments mainly discussed the dangers of AI systems and the potential negative consequences of not properly regulating them. There were also comments addressing gender inequality in the workplace and the advantages of hiring younger employees.', 'most_positive_comments': [], 'most_negative_comments': [], 'suggesstion_for_new_guests': [], 'insights': ['One of the main insights from these comments is the concern people have regarding the development of AI systems and the need for proper regulation to avoid potential negative consequences in the future.', 'The comments also highlight the importance of addressing gender inequality in the workplace and judging individuals on their merit, rather than their gender.', 'Additionally, there is a perception that younger employees may be more flexible and able to adapt to changes in the workplace.'], 'fun_comments': []},
#     {'feedback_and_constructive_criticism': [], 'engagement_and_interaction': [], 'ideas_and_suggestions': [], 'appreciation_and_encouragement': ["Such an enlightening interview and quite inspiring. AI (Congnitive ) Technology; giving a chance to third world countries to people who are willing to learn, teaching skills , having humility and walking the talk. Hard work is rewarding in that it changes one's future, teaching principle to life, navigating tensions all because of service to others whilst having passion and perseverance. I love how you stress on the point of transparency, it's such an honour to listen to this interview, using AI to help others to THINK. Gini Rometty and Lex Fridman thank you."], 'opportunities_for_collaboration_or_partnerships': [], 'textual_summary_of_all_comments': "The comments section is generally positive and admiring towards the interview and the interviewees. There is a link shared to Gini Rometty's page and a comment that is critical of her history with IBM.", 'most_positive_comments': ["Such an enlightening interview and quite inspiring. AI (Congnitive ) Technology; giving a chance to third world countries to people who are willing to learn, teaching skills , having humility and walking the talk. Hard work is rewarding in that it changes one's future, teaching principle to life, navigating tensions all because of service to others whilst having passion and perseverance. I love how you stress on the point of transparency, it's such an honour to listen to this interview, using AI to help others to THINK. Gini Rometty and Lex Fridman thank you."], 'most_negative_comments': ['Rometty’s reign included one stretch of 22 straight quarters of declining revenue. That run finally ended in the fourth quarter of 2017, but the company’s annual results continued to be dismal. Year-to-year revenue growth was negative in 2015, 2016 and 2017 but eked out a 1% gain in 2018. She collected about $137 million in compensation over the first seven years of her CEO-ship (her pay for 2019 hasn’t yet been disclosed).'], 'suggesstion_for_new_guests': [], 'insights': "The viewers are very appreciative of the interview and the insights shared by the guests, both towards AI and in general about their experience with it. The negative comment is critical of Gini Rometty's performance as CEO of IBM.", 'fun_comments': []}
# ]


dicts = []
for comment in tqdm(comments, total=len(comments)):
    try:
        result = analyze_comments_v2(comment)
        #print(t)
        # result = json.loads(t)
        #print(result.keys())
        dicts.append(result)
        #print(result, flush=True)
    except Exception as e:
        print(e, file=sys.stderr)
        


def merge_dicts(dicts):
    result_dict = defaultdict(list)
    for d in dicts:
        for key, value in d.items():
            result_dict[key].extend(value)
    return dict(result_dict)

r = merge_dicts(dicts)
print(r)
