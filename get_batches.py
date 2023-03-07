import os
from transformers import BertTokenizer
import multiprocessing
from tqdm import tqdm

from all_comments import comments

def get_comment_batches(comments: list, max_token: int) -> list:
    # create a pool of worker processes
    pool = multiprocessing.Pool()

    # calculate the token count of each comment
    token_counts = list(tqdm(pool.imap(calculate_num_tokens, comments), total=len(comments)))

    # initialize the batch
    batch = []
    batch_token_count = 0

    # iterate over the comments and their corresponding token counts
    for comment, comment_token_count in tqdm(zip(comments, token_counts), total=len(comments)):
        # if the comment would cause the batch to exceed the maximum token count, yield the batch and start a new one
        if batch_token_count + comment_token_count > max_token:
            yield batch
            batch = []
            batch_token_count = 0

        # add the comment to the batch
        batch.append(comment)
        batch_token_count += comment_token_count

    # yield the final batch
    if batch:
        yield batch

    # close the pool of worker processes
    pool.close()
    pool.join()


def calculate_num_tokens(text_list: list) -> int:
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    num_tokens = 0
    for text in text_list:
        tokenized_text = tokenizer.tokenize(text)
        num_tokens += len(tokenized_text)
    return num_tokens


print(f"analyzing {len(comments)} comments...")
batches = get_comment_batches(comments, 3000)
result = [batch for batch in batches]
print(result)
 