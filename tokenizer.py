# from blingfire import text_to_sentences
# from summarizer import Summarizer

# summariser = Summarizer()

# def summarise(article: str, num_sentences=None, *args, **kwargs) -> list[str]:
#     if num_sentences is None:
#         num_sentences = min(article.count('\n'), 10)
#     summary = summariser(article, num_sentences=num_sentences, *args, **kwargs)
#     summaries = text_to_sentences(summary)
#     return summaries.split('\n')

# if __name__ == '__main__':
    # s = '''
    #    Welcome to the second lecture on topic four, Third Normal Form. This presentation is presented by Dr. Ng. This presentation is copyright property of NTU. It is intended for students of CZ 2007 only. In this lecture, we will continue our discussion on third normal form decomposition process using the concept of minimal basis. We will go through an exercise and then we will look at properties of tables that satisfy the third normal form. So let's look at one exercise on converting a set of functional dependencies into minimal basis. So we are given a functional dependency S which contains A determines C, AC determines D and AB and AD determines B. So the first step is to transform the functional dependency to ensure that the right hand side of every FD has only one attribute. The second step is to see if any FD can be derived from other FDs and these are the redundant ones and we will remove them and the third step is to check if we can remove any attribute from the left hand side of any FD and yet not introduce a new FD. So these attributes are redundant attributes. So first step is to make sure the right hand side has one attribute. Second step, remove redundant FDs. Third step, remove redundant left hand side attributes. So let's look at the first step. Transform the FDs to ensure that the right hand side of each FD has only one attribute. And is it the case? Well yes. So it's automatically done and we denote this new set as M to stand for minimal basis. Second step is to remove redundant FDs and for that we have to look at each one of them. Let's look at A determines C first. If A determines C is removed, then the ones left would be AC determines D and AD determines B. We want to check if A determines C is inferable from the remaining FDs. How do we do that? Well, we will take the closure of the left hand side which is A and the closure of the left hand side is just A itself using the remaining FDs. Since A closure does not contain C, therefore A determines C cannot be derived from the remaining two FDs. Which means that we should not remove A determines C because it is not redundant. Next AC determines D. Again we removed it and the remaining ones are A determines C and AD determines B. We want to see if AC determines D is inferable from the remaining two. How? We are looking at the closure of the left hand side AC which is still AC. So therefore it doesn't contain D and therefore AC determines D cannot be derived from the remaining FDs meaning that we should not remove it otherwise we will lose information. So AC determines D is not redundant. The last one AD determines B. If we removed it, the remaining ones are these two FDs. We look at AD closure which is still AD which does not contains B. So therefore AD determines B cannot be derived from the remaining FDs. It is not redundant so therefore we should keep it. So after doing step 2, we have the same set of M. So now we are ready to do step 3 which is to remove redundant left hand side attributes if any. So there are. There are two FDs AC determines D and AD determines B which have more than one attribute on the left hand side. So we need to try 4 times. So let's try to remove A from AC determines D. We get C determines D. Can C determines D be derived from M? Let's see. Well C closure is just C so therefore not derivable. Meaning that C determines D will be a new function dependency introduced if we removed A and we should not do that. So therefore A in this FD AC determines D is not redundant and we should not remove it. Now check C. If we remove C from AC determines D we get A determines D. Can it be inferred from the remaining FDs? Let's see. So A closure is ABCD which contains D. So therefore A determines D can be inferred from the remaining set of FDs meaning that it is all the while hidden there. And therefore we can simply remove C and the remaining FD AD determines D is still there. So therefore C is redundant and can be removed. And our set M so far is now this. The second FD has been simplified to A determines D. Now let's check the redundant attributes for the third FD. Okay let's try to remove A from AD determines B resulting in D determines B. Is D determines B inferable from M? Look at the closure. Closure is just D. It doesn't contain B. So therefore D determines B cannot be inferred from M and we should not introduce D determines B into the system by removing A. So therefore A is not redundant and should not be removed from AD determines B. Now the last check. Okay try to remove D. We get A determines B. Is it derivable from M? Well A closure is ABCD so therefore it contains B. So therefore we know that A determines B can be inferred from M. All along it has been there. It is hidden there. So therefore we can remove D because it is redundant. By removing D we get A determines B which all along has been there. So therefore the final set of minimal bases is A determines C, A determines D and A determines B. So suppose this set of functional dependencies form the minimal bases then how do we go from here? Well the first step is to combine those FDs with the same left hand side. There are two. So therefore we have this set A determines BC and C determines D. Step 2 is to form a table from each one of them. We have R1 containing ABC and R2 containing CD. Step 3 is to remove redundant tables if any. There isn't tables where one is a subset of another. And sometimes we may also need to add an additional table if none of the tables contains the key. Let's see. So the minimal bases suppose is A determines B and C determines D. Again we combine the left hand side, still the same. Step 2 is to create a table. So we have AB and CD in R1 and R2. Remove redundant tables, none. However R1 and R2 they are unable to do a lossless join. Why? Well because there are just no common attributes between them. So we should add a table that contains a key of the original table. Suppose the original table the key is A and C. So therefore we should add R3, A and C so that the three tables can be losslessly reconstructed back. So the final result is R1, R2 and R3 where R3 is introduced. And the last step is to remove redundant tables which there isn't. So from table R which contains A, B, C, D we obtain minimal bases and from minimal bases we constructed smaller tables and technically all the smaller tables should satisfy the third normal form and we will see why in the next few slides. So we have discussed and gone through the exercise on 3NF decomposition. We would like to now study the tables that are formed from this process. Are they in third normal form? Well let's see. Why does the 3NF decomposition process produce tables which are in 3NF? So the 3NF decomposition process as we have seen consists of these 5 steps. And the key really is in step 3 where we create a table for each function dependency in a minimal basis. So if you recall this was an example on table R where the key is A and then the two function dependencies A determines B is fine but then B determines C is not fine. It's violating 3NF because the left hand side B does not contain a key and the right hand side C is not contained in a key. But in using the 3NF decomposition process, these two function dependencies will go into two different tables R1 containing AB and R2 containing BC. And BC in R2 is fine because the function dependency B determines C in R2 will have B as a key in R2. So therefore BC now becomes OK in R2. So by creating a table for each function dependency, we manage to eliminate some of the violations and with smaller tables, all the violations are now fine. So therefore the 3NF decomposition process produce tables which are in 3NF. The next thing we notice that the minimal basis is not always unique. For example, if we have a table R containing ABC and then there are many function dependencies depending on the order in which we perform the three steps to derive the minimal basis, we may get different sets of minimal basis. So minimal basis is not unique. Now let's compare the Boyce-Codd normal form and the 3rd normal form. In the Boyce-Codd normal form, we say that for any non-trivial FD in a table, its left-hand side is a super-key. Of course, the left-hand side may also be a key. But if all the function dependencies are such that the left-hand side is a super-key, it means that whatever attributes that depend on them, whatever attributes, meaning whichever right-hand side are the attributes in the functional dependencies, whether the right-hand side attributes are key attributes or non-key attributes, all attributes are dependent on an entire key or a super-key. In a case of 3NF, well, the condition where its left-hand side is a super-key is essentially the Boyce-Codd normal form. In case the table is not in the Boyce-Codd normal form, the 3rd NF still requires that the right-hand side attribute appear in a key. The right-hand side attribute appear in a key. What this means is that the right-hand side attribute depends on a key. Quite clearly, the Boyce-Codd normal form is stricter than the 3rd normal form. Therefore, a table that satisfies the Boyce-Codd normal form must satisfy 3rd NF, but not the other way around. And a table that violates 3rd NF must definitely violate BCNF, and not the other way around. Let us compare the tables formed from Boyce-Codd normal form and 3rd NF decomposition processes. Tables which are formed from Boyce-Codd normal form decomposition will have no anomalies, so all the anomalies will be gone. Most redundancies are eliminated except for multi-attribute keys. However, the tables may not preserve functional dependencies as we have seen earlier. For 3rd NF, tables also have no anomalies, however, there may be a little bit more redundancy than Boyce-Codd normal form. Why is this the case? In Boyce-Codd normal form, when an FD is not violating, a new table is not formed. But in 3rd NF, whether an FD is violating or not violating, each one of them will become a new table. So therefore, you may have attributes repeated in more than one table, which is why we say that there is a little bit more redundancy than tables produced using Boyce-Codd normal form. However, the good thing is, all the tables in 3rd NF decomposition process preserve all the FDs, as we will see in the next slide. So between the Boyce-Codd normal form and the 3rd NF, which one do we use? Our logical approach is to go for the strictest criteria first, which is the Boyce-Codd normal form. If all the FDs are preserved in the tables produced from the BCNF decomposition, then that's good. We are done. Otherwise, we will relax a little bit and go for 3rd NF decomposition instead. Let us now see why tables produced using the 3rd NF decomposition process preserve all the functional dependencies in the original table. Well this is the 5 steps that we have gone through. In the first step, minimal basis, we notice that the minimal basis preserves all the functional dependencies as much as possible, except the redundant ones. And in step 3, for each of the functional dependencies that is preserved, we create a table. So therefore, this guarantees that no original functional dependencies are lost, except those which are redundant. So we have finished our discussion on the 3rd NF, and that's for topic 4. The next lecture, we will discuss topic 5, relational algebra. Have a nice day! 
    # '''
#     result = summarise(s)
#     print(result)



import re
import nltk
from nltk.tokenize import sent_tokenize
from summarizer import Summarizer

summarizer = Summarizer()


# Download NLTK resources (run only once)
nltk.download('punkt')


s = '''
       Welcome to the second lecture on topic four, Third Normal Form. This presentation is presented by Dr. Ng. This presentation is copyright property of NTU. It is intended for students of CZ 2007 only. In this lecture, we will continue our discussion on third normal form decomposition process using the concept of minimal basis. We will go through an exercise and then we will look at properties of tables that satisfy the third normal form. So let's look at one exercise on converting a set of functional dependencies into minimal basis. So we are given a functional dependency S which contains A determines C, AC determines D and AB and AD determines B. So the first step is to transform the functional dependency to ensure that the right hand side of every FD has only one attribute. The second step is to see if any FD can be derived from other FDs and these are the redundant ones and we will remove them and the third step is to check if we can remove any attribute from the left hand side of any FD and yet not introduce a new FD. So these attributes are redundant attributes. So first step is to make sure the right hand side has one attribute. Second step, remove redundant FDs. Third step, remove redundant left hand side attributes. So let's look at the first step. Transform the FDs to ensure that the right hand side of each FD has only one attribute. And is it the case? Well yes. So it's automatically done and we denote this new set as M to stand for minimal basis. Second step is to remove redundant FDs and for that we have to look at each one of them. Let's look at A determines C first. If A determines C is removed, then the ones left would be AC determines D and AD determines B. We want to check if A determines C is inferable from the remaining FDs. How do we do that? Well, we will take the closure of the left hand side which is A and the closure of the left hand side is just A itself using the remaining FDs. Since A closure does not contain C, therefore A determines C cannot be derived from the remaining two FDs. Which means that we should not remove A determines C because it is not redundant. Next AC determines D. Again we removed it and the remaining ones are A determines C and AD determines B. We want to see if AC determines D is inferable from the remaining two. How? We are looking at the closure of the left hand side AC which is still AC. So therefore it doesn't contain D and therefore AC determines D cannot be derived from the remaining FDs meaning that we should not remove it otherwise we will lose information. So AC determines D is not redundant. The last one AD determines B. If we removed it, the remaining ones are these two FDs. We look at AD closure which is still AD which does not contains B. So therefore AD determines B cannot be derived from the remaining FDs. It is not redundant so therefore we should keep it. So after doing step 2, we have the same set of M. So now we are ready to do step 3 which is to remove redundant left hand side attributes if any. So there are. There are two FDs AC determines D and AD determines B which have more than one attribute on the left hand side. So we need to try 4 times. So let's try to remove A from AC determines D. We get C determines D. Can C determines D be derived from M? Let's see. Well C closure is just C so therefore not derivable. Meaning that C determines D will be a new function dependency introduced if we removed A and we should not do that. So therefore A in this FD AC determines D is not redundant and we should not remove it. Now check C. If we remove C from AC determines D we get A determines D. Can it be inferred from the remaining FDs? Let's see. So A closure is ABCD which contains D. So therefore A determines D can be inferred from the remaining set of FDs meaning that it is all the while hidden there. And therefore we can simply remove C and the remaining FD AD determines D is still there. So therefore C is redundant and can be removed. And our set M so far is now this. The second FD has been simplified to A determines D. Now let's check the redundant attributes for the third FD. Okay let's try to remove A from AD determines B resulting in D determines B. Is D determines B inferable from M? Look at the closure. Closure is just D. It doesn't contain B. So therefore D determines B cannot be inferred from M and we should not introduce D determines B into the system by removing A. So therefore A is not redundant and should not be removed from AD determines B. Now the last check. Okay try to remove D. We get A determines B. Is it derivable from M? Well A closure is ABCD so therefore it contains B. So therefore we know that A determines B can be inferred from M. All along it has been there. It is hidden there. So therefore we can remove D because it is redundant. By removing D we get A determines B which all along has been there. So therefore the final set of minimal bases is A determines C, A determines D and A determines B. So suppose this set of functional dependencies form the minimal bases then how do we go from here? Well the first step is to combine those FDs with the same left hand side. There are two. So therefore we have this set A determines BC and C determines D. Step 2 is to form a table from each one of them. We have R1 containing ABC and R2 containing CD. Step 3 is to remove redundant tables if any. There isn't tables where one is a subset of another. And sometimes we may also need to add an additional table if none of the tables contains the key. Let's see. So the minimal bases suppose is A determines B and C determines D. Again we combine the left hand side, still the same. Step 2 is to create a table. So we have AB and CD in R1 and R2. Remove redundant tables, none. However R1 and R2 they are unable to do a lossless join. Why? Well because there are just no common attributes between them. So we should add a table that contains a key of the original table. Suppose the original table the key is A and C. So therefore we should add R3, A and C so that the three tables can be losslessly reconstructed back. So the final result is R1, R2 and R3 where R3 is introduced. And the last step is to remove redundant tables which there isn't. So from table R which contains A, B, C, D we obtain minimal bases and from minimal bases we constructed smaller tables and technically all the smaller tables should satisfy the third normal form and we will see why in the next few slides. So we have discussed and gone through the exercise on 3NF decomposition. We would like to now study the tables that are formed from this process. Are they in third normal form? Well let's see. Why does the 3NF decomposition process produce tables which are in 3NF? So the 3NF decomposition process as we have seen consists of these 5 steps. And the key really is in step 3 where we create a table for each function dependency in a minimal basis. So if you recall this was an example on table R where the key is A and then the two function dependencies A determines B is fine but then B determines C is not fine. It's violating 3NF because the left hand side B does not contain a key and the right hand side C is not contained in a key. But in using the 3NF decomposition process, these two function dependencies will go into two different tables R1 containing AB and R2 containing BC. And BC in R2 is fine because the function dependency B determines C in R2 will have B as a key in R2. So therefore BC now becomes OK in R2. So by creating a table for each function dependency, we manage to eliminate some of the violations and with smaller tables, all the violations are now fine. So therefore the 3NF decomposition process produce tables which are in 3NF. The next thing we notice that the minimal basis is not always unique. For example, if we have a table R containing ABC and then there are many function dependencies depending on the order in which we perform the three steps to derive the minimal basis, we may get different sets of minimal basis. So minimal basis is not unique. Now let's compare the Boyce-Codd normal form and the 3rd normal form. In the Boyce-Codd normal form, we say that for any non-trivial FD in a table, its left-hand side is a super-key. Of course, the left-hand side may also be a key. But if all the function dependencies are such that the left-hand side is a super-key, it means that whatever attributes that depend on them, whatever attributes, meaning whichever right-hand side are the attributes in the functional dependencies, whether the right-hand side attributes are key attributes or non-key attributes, all attributes are dependent on an entire key or a super-key. In a case of 3NF, well, the condition where its left-hand side is a super-key is essentially the Boyce-Codd normal form. In case the table is not in the Boyce-Codd normal form, the 3rd NF still requires that the right-hand side attribute appear in a key. The right-hand side attribute appear in a key. What this means is that the right-hand side attribute depends on a key. Quite clearly, the Boyce-Codd normal form is stricter than the 3rd normal form. Therefore, a table that satisfies the Boyce-Codd normal form must satisfy 3rd NF, but not the other way around. And a table that violates 3rd NF must definitely violate BCNF, and not the other way around. Let us compare the tables formed from Boyce-Codd normal form and 3rd NF decomposition processes. Tables which are formed from Boyce-Codd normal form decomposition will have no anomalies, so all the anomalies will be gone. Most redundancies are eliminated except for multi-attribute keys. However, the tables may not preserve functional dependencies as we have seen earlier. For 3rd NF, tables also have no anomalies, however, there may be a little bit more redundancy than Boyce-Codd normal form. Why is this the case? In Boyce-Codd normal form, when an FD is not violating, a new table is not formed. But in 3rd NF, whether an FD is violating or not violating, each one of them will become a new table. So therefore, you may have attributes repeated in more than one table, which is why we say that there is a little bit more redundancy than tables produced using Boyce-Codd normal form. However, the good thing is, all the tables in 3rd NF decomposition process preserve all the FDs, as we will see in the next slide. So between the Boyce-Codd normal form and the 3rd NF, which one do we use? Our logical approach is to go for the strictest criteria first, which is the Boyce-Codd normal form. If all the FDs are preserved in the tables produced from the BCNF decomposition, then that's good. We are done. Otherwise, we will relax a little bit and go for 3rd NF decomposition instead. Let us now see why tables produced using the 3rd NF decomposition process preserve all the functional dependencies in the original table. Well this is the 5 steps that we have gone through. In the first step, minimal basis, we notice that the minimal basis preserves all the functional dependencies as much as possible, except the redundant ones. And in step 3, for each of the functional dependencies that is preserved, we create a table. So therefore, this guarantees that no original functional dependencies are lost, except those which are redundant. So we have finished our discussion on the 3rd NF, and that's for topic 4. The next lecture, we will discuss topic 5, relational algebra. Have a nice day! 
    '''

# Function to extract and display sentences from .srt file (excluding timestamps and numbers)
def extract_and_display_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        subtitle_content = file.read()

    # Use regular expressions to remove timestamps and numbers
    subtitle_content = re.sub(r'\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+\n', '', subtitle_content)
    subtitle_content = re.sub(r'\d+\n', '', subtitle_content)

    # Split the content into subtitles based on the empty lines
    subtitles = subtitle_content.split('\n\n')

    # Extract sentences from each subtitle
    sentences = []
    for subtitle in subtitles:
        # Use NLTK's sentence tokenizer to extract sentences
        subtitle_sentences = sent_tokenize(subtitle)
        sentences.extend(subtitle_sentences)

    # Display the extracted sentences
    for i, sentence in enumerate(sentences, start=1):
        print(f"{sentence.strip()}")

# Example usage
file_path = 'output_transcript.srt'
extract_and_display_sentences(file_path)



def summarise(article):
    summary = summarizer(article)
    summaries = extract_and_display_sentences(summary)
    return summaries.split('\n')

summarise(s)


