#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @ Time     : 19-3-13 下午7:37
  @ Author   : Vodka
  @ File     : ShallowParse.py
  @ Software : PyCharm
"""
from practnlptools.tools import Annotator
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class ShallowParser:
    def __init__(self):
        print "ShallowParser Initializing..."
        self.annotator = Annotator()
        self.stop_words = ["a", "as", "able", "about", "above", "according", "accordingly", "across", "actually",
                           "after", "afterwards", "again", "against", "aint", "all", "allow", "allows", "almost",
                           "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "an",
                           "and", "another", "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways",
                           "anywhere", "apart", "appear", "appreciate", "appropriate", "are", "arent", "around", "as",
                           "aside", "ask", "asking", "associated", "at", "available", "away", "awfully", "be", "became",
                           "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind",
                           "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond",
                           "both", "brief", "but", "by", "cmon", "cs", "came", "can", "cant", "cannot", "cant", "cause",
                           "causes", "certain", "certainly", "changes", "clearly", "co", "com", "come", "comes",
                           "concerning", "consequently", "consider", "considering", "contain", "containing", "contains",
                           "corresponding", "could", "couldnt", "course", "currently", "definitely", "described",
                           "despite", "did", "didnt", "different", "do", "does", "doesnt", "doing", "dont", "done",
                           "down", "downwards", "during", "each", "edu", "eg", "eight", "either", "else", "elsewhere",
                           "enough", "entirely", "especially", "et", "etc", "even", "ever", "every", "everybody",
                           "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "far", "few",
                           "ff", "fifth", "first", "five", "followed", "following", "follows", "for", "former",
                           "formerly", "forth", "four", "from", "further", "furthermore", "get", "gets", "getting",
                           "given", "gives", "go", "goes", "going", "gone", "got", "gotten", "greetings", "had",
                           "hadnt", "happens", "hardly", "has", "hasnt", "have", "havent", "having", "he", "hes",
                           "hello", "help", "hence", "her", "here", "heres", "hereafter", "hereby", "herein",
                           "hereupon", "hers", "herself", "hi", "him", "himself", "his", "hither", "hopefully", "how",
                           "howbeit", "however", "i", "id", "ill", "im", "ive", "ie", "if", "ignored", "immediate",
                           "in", "inasmuch", "inc", "indeed", "indicate", "indicated", "indicates", "inner", "insofar",
                           "instead", "into", "inward", "is", "isnt", "it", "itd", "itll", "its", "its", "itself",
                           "just", "keep", "keeps", "kept", "know", "knows", "known", "last", "lately", "later",
                           "latter", "latterly", "least", "less", "lest", "let", "lets", "like", "liked", "list",
                           "likely", "little", "look", "looking", "looks", "ltd", "mainly", "many", "may", "maybe",
                           "me", "mean", "meanwhile", "merely", "might", "more", "moreover", "most", "mostly", "much",
                           "must", "my", "myself", "name", "namely", "nd", "near", "nearly", "necessary", "need",
                           "needs", "neither", "never", "nevertheless", "new", "next", "nine", "no", "nobody", "non",
                           "none", "noone", "nor", "normally", "not", "nothing", "novel", "now", "nowhere", "obviously",
                           "of", "off", "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "only", "onto",
                           "or", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside",
                           "over", "overall", "own", "particular", "particularly", "per", "perhaps", "placed", "please",
                           "plus", "possible", "presumably", "probably", "provides", "que", "quite", "qv", "rather",
                           "rd", "re", "really", "reasonably", "regarding", "regardless", "regards", "relatively",
                           "respectively", "right", "said", "same", "saw", "say", "saying", "says", "second",
                           "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves",
                           "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "she", "should",
                           "shouldnt", "since", "six", "so", "some", "somebody", "somehow", "someone", "something",
                           "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify",
                           "specifying", "still", "sub", "such", "sup", "sure", "ts", "take", "taken", "tell", "tends",
                           "th", "than", "thank", "thanks", "thanx", "that", "thats", "thats", "the", "their", "theirs",
                           "them", "themselves", "then", "thence", "there", "theres", "thereafter", "thereby",
                           "therefore", "therein", "theres", "thereupon", "these", "they", "theyd", "theyll", "theyre",
                           "theyve", "think", "third", "this", "thorough", "thoroughly", "those", "though", "three",
                           "through", "throughout", "thru", "thus", "to", "together", "too", "took", "toward",
                           "towards", "tried", "tries", "truly", "try", "trying", "twice", "two", "un", "under",
                           "unfortunately", "unless", "unlikely", "until", "unto", "up", "upon", "us", "use", "used",
                           "useful", "uses", "using", "usually", "value", "various", "very", "via", "viz", "vs", "want",
                           "wants", "was", "wasnt", "way", "we", "wed", "well", "were", "weve", "welcome", "well",
                           "went", "were", "werent", "what", "whats", "whatever", "when", "whence", "whenever", "where",
                           "wheres", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether",
                           "which", "while", "whither", "who", "whos", "whoever", "whole", "whom", "whose", "why",
                           "will", "willing", "wish", "with", "within", "without", "wont", "wonder", "would", "would",
                           "wouldnt", "yes", "yet", "you", "youd", "youll", "youre", "youve", "your", "yours",
                           "yourself", "yourselves", "zero", "whose", "which", "is", ", ", "\\\\", "?", "\\"]
        print "ShallowParser Initialized"

    def shallowParse(self, text):
        """
        :param text: Natural Language Question
        :return: Key chunks with position infomation
        """
        # Get the chunks of one sentence using Senna
        if '?' not in text:
            text += '?'
        result = self.annotator.getAnnotations(text)['chunk']
        # print result

        # Get every word's start position and length
        chunk_with_position = []
        pos_index = 0
        for pair_item in result:
            position = text.find(pair_item[0], pos_index)
            pos_index = position + 1
            length = len(pair_item[0])
            chunk_with_position.append((pair_item[0], pair_item[1], position, length))
        # print chunk_with_position

        # Get the key words filtering those not belongs to NP or VP
        NP_set = []
        VP_set = []
        temp_pharse_NP = []
        temp_pharse_VP = []
        for item in chunk_with_position:
            if item[1] == 'S-NP':
                NP_set.append([item])
            elif item[1] == 'B-NP' or item[1] == 'I-NP':
                temp_pharse_NP.append(item)
            elif item[1] == 'E-NP':
                temp_pharse_NP.append(item)
                NP_set.append(temp_pharse_NP)
                temp_pharse_NP = []
            elif item[1] == 'S-VP':
                VP_set.append([item])
            elif item[1] == 'B-VP' or item[1] == 'I-VP':
                temp_pharse_VP.append(item)
            elif item[1] == 'E-VP':
                temp_pharse_VP.append(item)
                NP_set.append(temp_pharse_VP)
                temp_pharse_VP = []
        # print 1,NP_set,VP_set

        # Get chunks without stop words
        all_element_set = []
        result_key_chunks = []
        for i in NP_set:
            all_element_set.append(i)
        for i in VP_set:
            all_element_set.append(i)
        for np_phrase in all_element_set:
            chunk_without_stopword = []
            for item in np_phrase:
                if item[0].lower() not in self.stop_words:
                    chunk_without_stopword.append(item)
            if len(chunk_without_stopword) > 0:
                result_key_chunks.append(chunk_without_stopword)
        return result_key_chunks

        # Get chunks
        # for np_phrase in all_element_set:
        #     chunk_without_stopword = []
        #     for item in np_phrase:
        #         chunk_without_stopword.append(item)
        #     if len(chunk_without_stopword) > 0:
        #         chunks.append(chunk_without_stopword)
        # return result_key_chunks,chunks

if __name__ == '__main__':
    s = ShallowParser()
    print s.shallowParse('Who is the parent organisation of Barack Obama?')
    # Result is [[('parent', 'I-NP', 11, 6), ('organisation', 'E-NP', 18, 12)], [('Barack', 'B-NP', 34, 6), ('Obama', 'E-NP', 41, 5)]]
