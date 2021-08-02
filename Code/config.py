import transformers

batch_size = 2
model_path = 'gpt2_model.bin'
max_seq_len = 300
epochs = 6
data_path = 'data.csv'
tokenizer = transformers.GPT2Tokenizer.from_pretrained('gpt2')
model = transformers.GPT2LMHeadModel.from_pretrained('gpt2')