import torch
from config import model,tokenizer,model_path

def generate_text(input_text,device = 'cuda',max_len = 300):
  pad_tok = tokenizer.encode(['<|pad|>'])[0]
  model.load_state_dict(torch.load(model_path))
  model.to(device)
  model.eval()

  input_ids = tokenizer.encode(input_text)

    
  ids = torch.tensor(input_ids,dtype = torch.long).to(device).unsqueeze(0)
  
  sample_out = model.generate(ids, min_length = 30,max_length=max_len, pad_token_id=pad_tok,
                              top_k = 1000,
                              top_p=0.95, early_stopping=True, 
                              do_sample=True, num_beams = 5, 
                              no_repeat_ngram_size = 2,num_return_sequences=1,
                              temperature = 1)
  
  out = tokenizer.decode(sample_out[0],skip_special_tokens = True)
  return out

torch.random.seed = 55


input_texts = ['After years','When the night','This is the story', 'Spoon was','In the year','During the war','A young man', 'A long time ago, in a galaxy far, far away...']

for input_text in input_texts:
    generated_e = generate_text(input_text,device = 'cpu')
    print(generated_e,'\n\n----------------------------------\n\n')

    # saving 
    file = open('Generated Examples.txt','a')
    file.write(f'{generated_e}\n----------------------------------\n')
file.close()